
# **WinLockAI - 🔒 Smart Behavioral Monitoring & System Locking Solution** 

**WinLockAI** is a behavioral monitoring system designed to enhance security by automatically locking the system when suspicious activity is detected. The system uses machine learning techniques to analyze user behavior and responds promptly by locking the system if abnormal patterns are identified. This README will guide you through the folder structure, how to run the project, training the model, and the functionality of the system. 🚀

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
├── README.txt               # Project documentation 📑
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

1. **Start Monitoring** 🕵️‍♂️  
   - Starts the system monitoring process. The application begins tracking user behavior (mouse clicks and movements) and will lock the system if abnormal behavior is detected.

2. **Start Training** 🏋️‍♂️  
   - This option allows you to retrain the model. It will delete any pre-existing trained model file and begin collecting new data based on your behavior over a specified duration (3 minutes by default). This training process refines the model and improves its accuracy in detecting suspicious behavior.

3. **Stop Monitoring** ⏹️  
   - This stops the monitoring process and ends the system lock functionality. Use this option if you want to pause the monitoring session.

---

## **🤖 Model Used in the Project**

### **Isolation Forest**

**WinLockAI** uses the **Isolation Forest** algorithm from **scikit-learn** to detect anomalies in user behavior. The model works by isolating observations through random partitions. Since outliers are few and different, they tend to be isolated faster than normal points, making it effective in detecting anomalous behavior. 

#### **How the Model Works**:
- The system captures feature data from user actions such as mouse movements and clicks.
- This feature data is fed into the **Isolation Forest** model, which then classifies each sample as "normal" or "abnormal."
- If abnormal behavior (e.g., erratic mouse movements) is detected, the system locks the computer to prevent unauthorized access.

---

## **🛠️ Training the Model**

The training process involves collecting data from the user’s normal behavior to establish a baseline. Here’s how the training works:

1. **Data Collection**:
   - When you choose **Start Training**, the application collects feature data over a period (180 seconds by default).
   - The features collected are based on the user’s mouse movements, clicks, and other activities, which are stored in the file `training_data.npy`.

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

1. **Multi-User Support** 👥:
   - Support for multiple users on the same system, allowing different profiles and personalized models for each user.

2. **Improved Anomaly Detection** 🚨:
   - Enhance the anomaly detection capabilities by using more advanced machine learning models or incorporating more data sources (keyboard activity, for instance).

3. **Real-Time Notifications** 📲:
   - Add a notification system that alerts users when their system is locked or when suspicious behavior is detected.

4. **Mobile App Version** 📱:
   - Develop a mobile app that can monitor and lock devices remotely, enhancing security even when you're away from your desktop.

5. **Detailed Reporting** 📑:
   - Introduce detailed logs and reports that show the detected anomalies, the actions taken by the system, and the reason for locking.

6. **Enhanced GUI** 🎨:
   - Improve the GUI with additional controls for managing security settings, model training, and more detailed system statistics.

---

## **📞 Get in Touch**

If you have any questions, feedback, or suggestions, feel free to reach out:

- **LinkedIn**: [Muhammad Farooq](https://www.linkedin.com/in/muhammad-farooq-058b76195/)  
- **Email**: [4faroq@gmail.com](mailto:4faroq@gmail.com)  
- **WhatsApp**: +923158304046  

I’m always open to discussions and collaboration opportunities! 😊
