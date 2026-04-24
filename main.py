import cv2
import datetime
from ultralytics import YOLO
import cvzone

# 1. Load the pre-trained YOLOv8 model (Nano version for high performance/speed)
model = YOLO("yolov8n.pt") 

# 2. Initialize Video Capture (0 is for the default webcam)
cap = cv2.VideoCapture(0)

# 3. Define the Forbidden Zone coordinates [x1, y1, x2, y2]
# Adjust these values based on camera view
danger_zone = [100, 100, 400, 400] 

print("AI Surveillance System is running...")

while True:
    # Capture frame-by-frame
    success, img = cap.read()
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if not success:
        break

    # 4. Run Object Detection on the current frame
    # stream=True is more memory-efficient for real-time video
    results = model(img, stream=True)

    # 5. Draw the Danger Zone rectangle on the screen
    cv2.rectangle(img, (danger_zone[0], danger_zone[1]), 
                  (danger_zone[2], danger_zone[3]), (0, 0, 255), 2)
    cvzone.putTextRect(img, "FORBIDDEN AREA", (110, 90), scale=1, thickness=1, colorR=(0, 0, 255))

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Check class ID (Class 0 in COCO dataset is 'Person')
            cls = int(box.cls[0])
            
            if cls == 0:
                # Extract Bounding Box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                # Calculate the center point of the person
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                # 6. Logical Check: Is the person's center inside the danger zone?
                if danger_zone[0] < cx < danger_zone[2] and danger_zone[1] < cy < danger_zone[3]:
                    # Alert logic
                    current_time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"SECURITY ALERT: Intrusion detected at {current_time}")
                    
                    color = (0, 0, 255) # Red for danger
                    cvzone.putTextRect(img, "INTRUDER", (x1, y1 - 10), scale=1.5, thickness=2, colorR=(0, 0, 255))
                else:
                    color = (0, 255, 0) # Green for safe

                # Draw the bounding box around the detected person
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

    # 7. Display the output window
    cv2.imshow("Smart Security System", img)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()