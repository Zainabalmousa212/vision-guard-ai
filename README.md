# VisionGuard-AI: Smart Surveillance & Gesture Analysis 🛡️🤖

**VisionGuard-AI** is a real-time computer vision system designed to enhance safety and monitoring through intelligent object detection and spatial logic. This project demonstrates the seamless integration of two State-of-the-Art (SOTA) frameworks into a single processing pipeline.

## 🌟 Key Features
- **Real-Time Intrusion Detection:** Leverages **YOLOv8** to monitor a predefined "Danger Zone". It triggers a visual alert immediately when a person enters the restricted area.
- **Advanced Hand Tracking:** Integrates **MediaPipe** to map 21 hand landmarks, allowing for detailed gesture analysis alongside global surveillance.
- **Spatial Analysis Logic:** Uses geometric centroid calculations to determine if a detected object violates boundary constraints.
- **Optimized Performance:** Utilizes the YOLOv8-Nano model to ensure high FPS (Frames Per Second) and low latency on standard hardware.

## 🛠️ Tech Stack
- **Language:** Python
- **AI Models:** YOLOv8 (Ultralytics), MediaPipe
- **Computer Vision:** OpenCV
- **Utilities:** Cvzone

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/vision-guard-ai.git](https://github.com/YourUsername/vision-guard-ai.git)
Navigate to the project directory:

Bash
cd vision-guard-ai
Install the required dependencies:

Bash
pip install ultralytics opencv-python cvzone mediapipe
Run the application:

Bash
python main.py