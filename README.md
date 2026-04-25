# VisionGuard-AI: Smart Intrusion Detection System 🛡️🤖

**VisionGuard-AI** is a real-time computer vision system designed to enhance security and monitoring through intelligent object detection and spatial logic. The system is optimized for high-performance inference to detect and alert against unauthorized access in predefined restricted areas.

## 🌟 Key Features
* **Real-Time Intrusion Detection:** Leverages **YOLOv8** to monitor a specific "Danger Zone".
* **Automated Security Alerts:** Triggers a visual "INTRUDER" alert and logs a timestamped security message when a violation occurs.
* **Spatial Logic:** Uses geometric centroid calculations to determine if a detected person has crossed the boundary constraints.
* **High-Speed Performance:** Built using the **YOLOv8-Nano** model, ensuring smooth, real-time FPS even on standard hardware.

## 🛠️ Tech Stack
* **Language:** Python 🐍
* **AI Model:** YOLOv8 (Ultralytics)
* **Computer Vision:** OpenCV
* **Utilities:** Cvzone, Datetime

## 🚀 Installation & Setup

1. **Clone the repository:**
   git clone https://github.com/Zainabalmousa212/vision-guard-ai.git

2. **Navigate to the project directory:**
   cd vision-guard-ai
   
4. **Install the required dependencies:**
   pip install ultralytics opencv-python cvzone
5. **Run the application:**
   python main.py

## 📊 How it Works
1. **Frame Acquisition:** Captures live feed and adjusts orientation (Rotate/Flip) for accuracy.
2. **Detection:** YOLOv8 identifies humans (Class 0) in the frame.
3. **Logic:** The system calculates the **Centroid** (center point) of the detected person.
4. **Validation:** If the Centroid enters the `danger_zone` coordinates, the system switches the status from "Safe" (Green) to "Intruder" (Red) and logs the event.


