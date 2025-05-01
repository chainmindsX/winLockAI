import sys
import os
import tkinter as tk
from tkinter import messagebox
import threading
from core import main  # Import the main module from core

def launch_gui():
    def start_monitoring_thread():
        start_monitoring_button.config(state=tk.DISABLED)
        stop_monitoring_button.config(state=tk.NORMAL)
        status_label.config(text="🧠 Starting Monitoring...")
        threading.Thread(target=main.threaded_monitoring, daemon=True).start()

    def stop_monitoring_action():
        main.stop_monitoring()
        status_label.config(text="🛑 Monitoring stopped.")
        start_monitoring_button.config(state=tk.NORMAL)
        stop_monitoring_button.config(state=tk.DISABLED)

    def start_training_thread():
        start_training_button.config(state=tk.DISABLED)
        status_label.config(text="🔁 Starting Fresh Training...")
        threading.Thread(target=training_sequence, daemon=True).start()

    def training_sequence():
        if os.path.exists(main.MODEL_PATH):
            os.remove(main.MODEL_PATH)
            print("[INFO] Old model deleted.")
        if os.path.exists(main.TRAINING_DATA_PATH):
            os.remove(main.TRAINING_DATA_PATH)
            print("[INFO] Old training data deleted.")
        data = main.collect_training_data()
        main.model = main.train_model(data)
        status_label.config(text="✅ Training complete. Ready for monitoring.")
        start_training_button.config(state=tk.NORMAL)

    root = tk.Tk()
    root.title("WinLockAI")
    root.geometry("420x300")
    root.configure(bg="#f5f5f5")

    title = tk.Label(root, text="🛡️ WinLockAI Launcher", font=("Segoe UI", 14, "bold"), bg="#f5f5f5")
    title.pack(pady=20)

    start_monitoring_button = tk.Button(root, text="▶️ Start Monitoring", font=("Segoe UI", 12),
                                        bg="#4CAF50", fg="white", width=25, command=start_monitoring_thread)
    start_monitoring_button.pack(pady=10)

    stop_monitoring_button = tk.Button(root, text="⛔ Stop Monitoring", font=("Segoe UI", 12),
                                       bg="#f44336", fg="white", width=25, command=stop_monitoring_action, state=tk.DISABLED)
    stop_monitoring_button.pack(pady=5)

    start_training_button = tk.Button(root, text="🔄 Start Fresh Training", font=("Segoe UI", 12),
                                      bg="#2196F3", fg="white", width=25, command=start_training_thread)
    start_training_button.pack(pady=10)

    status_label = tk.Label(root, text="", bg="#f5f5f5", fg="gray", font=("Segoe UI", 10))
    status_label.pack(pady=10)

    root.mainloop()
