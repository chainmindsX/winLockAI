import os
import time
import platform
import joblib
import numpy as np
from sklearn.ensemble import IsolationForest
from pynput import mouse
from collections import deque

# ----------------------- Constants -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "user_behavior_model.pkl")
TRAINING_DATA_PATH = os.path.join(BASE_DIR, "..", "models", "training_data.npy")
TRAINING_DURATION = 180  # 3 minutes
recent_predictions = deque(maxlen=5)
model = None

# ----------------------- Core Logic -----------------------
def collect_feature_data():
    return np.random.rand(50)

def collect_training_data(duration=180):
    print(f"[INFO] Collecting training data for {duration} seconds...")
    data = []
    end_time = time.time() + duration
    while time.time() < end_time:
        data.append(collect_feature_data())
        time.sleep(1)
    data = np.array(data)
    np.save(TRAINING_DATA_PATH, data)
    print("[INFO] Training data collection complete.")
    return data

def train_model(data):
    print("[INFO] Training Isolation Forest model...")
    model = IsolationForest(contamination=0.02, random_state=42)
    model.fit(data)
    joblib.dump(model, MODEL_PATH)
    print("[INFO] ✅ Model trained and saved.")
    return model

def load_or_train_model():
    global model
    if os.path.exists(MODEL_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            print("[DEBUG] ✅ Model loaded successfully.")
            return model
        except Exception as e:
            print(f"[ERROR] Failed to load model: {e}")
    data = collect_training_data(duration=TRAINING_DURATION)
    return train_model(data)

def lock_system():
    system = platform.system()
    if system == "Windows":
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif system == "Linux":
        os.system("gnome-screensaver-command -l")
    elif system == "Darwin":
        os.system("/System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -suspend")
    else:
        print("[WARN] Locking not supported on this OS.")

def analyze_and_act():
    global model
    features = collect_feature_data().reshape(1, -1)
    prediction = model.predict(features)[0]
    recent_predictions.append(prediction)

    abnormal_count = recent_predictions.count(-1)
    print(f"[DEBUG] Recent predictions: {list(recent_predictions)}")

    if abnormal_count >= 3:
        print("[⚠️] Consistent abnormal behavior detected! Locking system.")
        lock_system()
        recent_predictions.clear()
    else:
        print("[DEBUG] Normal behavior.")

def on_click(x, y, button, pressed):
    if pressed:
        try:
            analyze_and_act()
        except Exception as e:
            print(f"⚠️ Error in mouse click handler: {e}")

def start_monitoring():
    print("🛡️ WinLockAI is running...")
    print("👀 Monitoring user behavior...")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def stop_monitoring():
    global listener
    if listener and listener.running:
        listener.stop()
        print("[INFO] 🛑 Monitoring stopped.")

def threaded_monitoring():
    global model
    model = load_or_train_model()
    start_monitoring()
