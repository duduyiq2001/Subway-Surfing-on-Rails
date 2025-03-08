import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2

# STEP 2: Create an GestureRecognizer object.
base_options = python.BaseOptions(model_asset_path="gesture_recognizer.task")
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)


## setup video cam
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break  # Stop if the camera fails

    # Convert OpenCV frame to RGB (MediaPipe expects RGB input)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert to MediaPipe Image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

    # Run Gesture Recognition
    gesture_result = recognizer.recognize(mp_image)

    # Draw recognized gestures on the frame
    if gesture_result.gestures:
        for gesture in gesture_result.gestures:
            name = gesture[0].category_name  # Gesture name
            score = gesture[0].score  # Confidence score
            # cv2.putText(frame, f'{name} ({score:.2f})', (50, 50),
            #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            # logging
            print(f"gesture detected {name} with score: {score}")

    # # Display the frame
    # cv2.imshow("Gesture Recognition", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cam.release()
# cv2.destroyAllWindows()
