# **WinLockAI - 🔒 Smart Behavioral Monitoring & System Locking Solution** 

**WinLockAI** is a behavioral monitoring system designed to enhance security by automatically locking the system when suspicious activity is detected. The system uses machine learning techniques to analyze user behavior, including both **mouse clicks** 🖱️ and **keyboard actions** ⌨️, and responds promptly by locking the system if abnormal patterns are identified. This README will guide you through the folder structure, how to run the project, training the model, and the functionality of the system. 🚀

---

## **🧠 How the Model is Trained**

The **WinLockAI** model is specifically trained to detect abnormal behavior based on the following actions:

- **Keyboard Behavior** ⌨️:
  - Tracks keyboard activity such as typing speed, key press patterns, and intervals between key presses.
  
- **Mouse Behavior** 🖱️:
  - Monitors mouse clicks, movement speed, and patterns of clicking (e.g., repeated or erratic movements).

### **Training Process**:
- **Data Collection**:  
  - The system collects data for a default training period of **3 minutes**. During this time, it tracks user interactions like **mouse clicks** and **keyboard typing patterns**.
  - The training duration can be **adjusted** or **extended** as needed for better accuracy.
  
- **Feature Extraction**:  
  - After the training duration, the system extracts features from the recorded actions (e.g., how often and how fast keys or mouse buttons are pressed).
  
- **Model Training**:  
  - The system uses the **Isolation Forest** algorithm from **scikit-learn** to learn patterns from the collected data.
  - The trained model is saved as `user_behavior_model.pkl` for future use.

- **Model Deployment**:  
  - Once trained, the model is used to monitor real-time user activity and lock the system if abnormal behavior is detected.

---

## **📂 Folder Structure**

Here’s an overview of the project folder structure:

```
WinLockAI/
├── core/
│   ├── gui.py               # Graphical User Interface 🖥️
│   └── main.py              # Core functionality for monitoring and system locking 🔒
├── model/
│   ├── model.py             # Contains the model architecture (Isolation Forest) 🤖
│   └── training_data.npy    # File to store the training data (features collected for model) 📊
├── requirements.txt         # Project dependencies 📄
├── run.py                   # Script to run the application ▶️
├── winLOCKAI README.txt               # Project documentation 📑
└── .gitignore               # Git ignore file (if using Git) 🚫
```

---

## **⚙️ Dependencies**

To install the necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
```

This will install all required packages including:
- `numpy` 🧮
- `scikit-learn` 📚
- `pynput` 🖱️
- `joblib` 🗃️
- `tkinter` 🖥️

---

## **🚀 How to Run the Project**

### **1. Run the Application**

To run **WinLockAI**, simply execute the following command:

```bash
python run.py
```

This will start the GUI, and you will see three available options:

### **2. Available Options in the GUI**:

- **Start Monitoring** 🕵️‍♂️  
  - Starts the system monitoring process. The application begins tracking user behavior (mouse clicks and keyboard actions) and will lock the system if abnormal behavior is detected.

- **Start Training** 🏋️‍♂️  
  - This option allows you to retrain the model. It will delete any pre-existing trained model file and begin collecting new data based on your behavior over a specified duration (default 3 minutes). 
  - The duration of the training can be **adjusted** or **extended** as per your preference.

- **Stop Monitoring** ⏹️  
  - This stops the monitoring process and ends the system lock functionality. Use this option if you want to pause the monitoring session.

---

## **🤖 Model Used in the Project**

### **Isolation Forest**

**WinLockAI** uses the **Isolation Forest** algorithm from **scikit-learn** to detect anomalies in user behavior. The model works by isolating observations through random partitions. Since outliers are few and different, they tend to be isolated faster than normal points, making it effective in detecting anomalous behavior. 

#### **How the Model Works**:
- The system captures feature data from user actions, including **mouse movements**, **mouse clicks**, and **keyboard interactions**.
- This feature data is fed into the **Isolation Forest** model, which then classifies each sample as "normal" or "abnormal."
- If abnormal behavior (e.g., erratic mouse movements, unusual typing patterns) is detected, the system locks the computer to prevent unauthorized access.

---

## **🛠️ Training the Model**

The training process involves collecting data from the user’s normal behavior to establish a baseline. Here’s how the training works:

1. **Data Collection**:
   - When you choose **Start Training**, the application collects feature data over a period (default 3 minutes, but can be adjusted).
   - The features collected include **mouse movements**, **mouse clicks**, and **keyboard interactions**, which are stored in the file `training_data.npy`.

2. **Model Training**:
   - The training data is used to train the **Isolation Forest** model. This model is saved as `user_behavior_model.pkl` using **joblib** for later use.
   - The model is trained to recognize patterns in user behavior and identify anomalies based on deviations from the norm.

3. **Model Testing & Deployment**:
   - Once the model is trained, it is used in the **Start Monitoring** phase to track real-time behavior and take action if abnormal behavior is detected.
   
4. **How to Retrain**:
   - To retrain the model, simply use the **Start Training** option again. It will delete the old model and retrain it using newly collected data.

---

## **🔮 Future Improvements**

While **WinLockAI** is functional and secure, there are several areas for improvement and additional features to be added in future versions:

- **Multi-User Support** 👥:
  - Support for multiple users on the same system, allowing different profiles and personalized models for each user.

- **Improved Anomaly Detection** 🚨:
  - Enhance the anomaly detection capabilities by using more advanced machine learning models or incorporating more data sources (keyboard activity, for instance).

- **Real-Time Notifications** 📲:
  - Add a notification system that alerts users when their system is locked or when suspicious behavior is detected.

- **Mobile App Version** 📱:
  - Develop a mobile app that can monitor and lock devices remotely, enhancing security even when you're away from your desktop.

- **Detailed Reporting** 📑:
  - Introduce detailed logs and reports that show the detected anomalies, the actions taken by the system, and the reason for locking.

- **Enhanced GUI** 🎨:
  - Improve the GUI with additional controls for managing security settings, model training, and more detailed system statistics.

---

## **📞 Get in Touch**

If you have any questions, feedback, or suggestions, feel free to reach out:

- **LinkedIn**: [Muhammad Farooq](https://www.linkedin.com/in/muhammad-farooq-058b76195/)  
- **Email**: [4faroq@gmail.com](mailto:4faroq@gmail.com)  
- **WhatsApp**: +923158304046  

I’m always open to discussions and collaboration opportunities! 😊

---

