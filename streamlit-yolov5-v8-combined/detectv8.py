import cv2
from ultralytics import YOLO
import cv2
import onnxruntime
import numpy as np
# from ultralytics import YOLOv5
# from yolov5 import YOLOv5


# def onButtonPressv5(frame):
#     """Performs object detection, extracts unique labels, and writes them to a text file."""
#     cap = cv2.VideoCapture(0)  # Assuming webcam stream at index 0
#     model = YOLO("D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/bestv5.pt")
#     unique_classes_v5 = set()  # Create a set to store unique classes
#     last_label = None  # Variable to keep track of the last label encountered

#     with open("unique_labels_v5.txt", "w") as labels_file:  # Open file with write mode
#         while True:
#             ret, image = cap.read()
#             if not ret:
#                 break
 
#             # Perform object detection
#             results = model.predict(source=image, show=False)


#             # Extract and store unique labels
#             for result in results:
#                 for box in result.boxes:
#                     x1, y1, x2, y2 = map(int, box.xyxy[0])
#                     cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 1)
#                     label = result.names[int(box.cls)]
#                     confidence = box.conf[0]
#                     cv2.putText(image, f"{label}: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
#                     # Check if the current label is different from the last one
#                     if label != last_label:
#                         unique_classes_v5.add(label)
#                         labels_file.write(f"{label}\n")  # Write each label to the file
#                         last_label = label  # Update last_label

#             # Update frame in Streamlit (optional, comment out if not needed)
#             frame.image(image, channels="BGR")

#     cap.release()






def onButtonPressv8(frame):
    """Performs object detection, extracts unique labels, and writes them to a text file."""
    cap = cv2.VideoCapture(0)  # Assuming webcam stream at index 0
    model = YOLO("D:/ENGG/SEM 8/B.TECH PROJECT/yolov5v8streamlit/bestv8.pt")
    unique_classes_v8 = set()  # Create a set to store unique classes
    last_label = None  # Variable to keep track of the last label encountered

    with open("unique_labels_v8.txt", "w") as labels_file:  # Open file with write mode
        while True:
            ret, image = cap.read()
            if not ret:
                break

            # Perform object detection
            results = model.predict(source=image, show=False)


            # Extract and store unique labels
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 1)
                    label = result.names[int(box.cls)]
                    confidence = box.conf[0]
                    cv2.putText(image, f"{label}: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                    # Check if the current label is different from the last one
                    if label != last_label:
                        unique_classes_v8.add(label)
                        labels_file.write(f"{label}\n")  # Write each label to the file
                        last_label = label  # Update last_label

            # Update frame in Streamlit (optional, comment out if not needed)
            frame.image(image, channels="BGR")

    cap.release()




# import cv2
# from ultralytics import YOLO


# def onButtonPress(frame):
#     """Performs object detection, extracts unique labels, and writes them to a text file."""
#     cap = cv2.VideoCapture(0)  # Assuming webcam stream at index 0
#     model = YOLO("D:/YOLOV8new/best.pt")
#     unique_classes = set()  # Create a set to store unique classes

#     with open("unique_labels.txt", "w") as labels_file:  # Open file with write mode
#         while True:
#             ret, image = cap.read()
#             if not ret:
#                 break

#             # Perform object detection
#             results = model.predict(source=image, show=False)

#             # Extract and store unique labels
#             for result in results:
#                 for box in result.boxes:
#                     label = result.names[int(box.cls)]
#                     unique_classes.add(label)
#                     labels_file.write(f"{label}\n")  # Write each label to the file

#             # Update frame in Streamlit (optional, comment out if not needed)
#             frame.image(image, channels="BGR")

#     cap.release()





# import cv2
# from ultralytics import YOLO


# def onButtonPress(frame):
#     """Performs object detection, extracts unique labels, and writes them to a text file."""
#     cap = cv2.VideoCapture(0)  # Assuming webcam stream at index 0
#     model = YOLO("D:/YOLOV8new/best.pt")
#     unique_classes = set()  # Create a set to store unique classes

#     with open("unique_labels.txt", "w") as labels_file:  # Open file with write mode
#         while True:
#             ret, image = cap.read()
#             if not ret:
#                 break

#             # Perform object detection
#             results = model.predict(source=image, show=False)

#             #  Display bounding boxes on the frame (optional)
#             # labels = []
#             for result in results:
#                 for box in result.boxes:
#                     x1, y1, x2, y2 = map(int, box.xyxy[0])
#                     cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 1)

#                     # Display label and confidence (optional)
#                     label = result.names[int(box.cls)]
#                     unique_classes.add(label)
#                     labels_file.write(f"{label}\n")  # Write each label to the file
#                     confidence = box.conf[0]
#                     cv2.putText(image, f"{label}: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


#             # Extract and store unique labels
#             # for result in results:
#             #     for box in result.boxes:
#             #         label = result.names[int(box.cls)]
#             #         unique_classes.add(label)
#             #         labels_file.write(f"{label}\n")  # Write each label to the file

#             # Update frame in Streamlit (optional, comment out if not needed)
#             frame.image(image, channels="BGR")

#             # Consider adding a delay for smoother video (adjust as needed)
#             if cv2.waitKey(1) == ord('q'):
#                 break

#     cap.release()








# put labels in text file
# import cv2
# from ultralytics import YOLO


# def onButtonPress(frame):
#     """Performs object detection, extracts labels, and updates the frame."""
#     cap = cv2.VideoCapture(0)  # Assuming webcam stream at index 0
#     model = YOLO("D:/YOLOV8new/best.pt")
#     labels_file = open("detected_labels.txt", "w")  # Open file for writing

#     while True:
#         ret, image = cap.read()
#         if not ret:
#             break

#         # Perform object detection
#         results = model.predict(source=image, show=False)


#         #  Display bounding boxes on the frame (optional)
#         labels = []
#         for result in results:
#             for box in result.boxes:
#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 1)

#                 # Display label and confidence (optional)
#                 label = result.names[int(box.cls)]
#                 labels.append(label)
#                 labels_file.write(f"{label}\n")
#                 confidence = box.conf[0]
#                 cv2.putText(image, f"{label}: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


#         # Update frame in Streamlit (optional, comment out if not needed)
#         frame.image(image, channels="BGR")


#     labels_file.close()
#     cap.release()



# live feed inside streamlit- working properly 1
# import cv2
# from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor


# def onButtonPress(frame):
#     """Performs object detection and updates the frame with results."""
#     cap = cv2.VideoCapture(0)  # Assuming webcam stream at index 0
#     model = YOLO("D:/YOLOV8new/best.pt")

#     while True:
#         ret, image = cap.read()
#         if not ret:
#             break

#         # Perform object detection (consider adding logic if needed)
#         results = model.predict(source=image, show=False)

#         # Display bounding boxes on the frame (optional)
#         for result in results:
#             for box in result.boxes:
#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 1)

#                 # Display label and confidence (optional)
#                 label = result.names[int(box.cls)]
#                 confidence = box.conf[0]
#                 cv2.putText(image, f"{label}: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

#         # Update the frame in Streamlit
#         frame.image(image, channels="BGR")

#     cap.release()




#old code 

# from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor

# def onButtonPress(placeholder):
#     main()

# def main():
    
#     model = YOLO("D:/YOLOV8new/best.pt") 

#     results = model.predict(source="0", show=True)

#     print(results)

# if __name__ == "__main__":
#     main()