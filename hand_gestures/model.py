import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from queue import Queue
import cv2

# STEP 2: Create an GestureRecognizer object.
def get_model():
    base_options = python.BaseOptions(model_asset_path="gesture_recognizer.task")
    options = vision.GestureRecognizerOptions(base_options=base_options)
    recognizer = vision.GestureRecognizer.create_from_options(options)
# implemented as a generator running on another thread
def run_model_on_cam(cam, recognizer, queue):
    try:
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
                    # logging
                    print(f"gesture detected {name} with score: {score}")
                    ## put gesture into queue
                    queue.put((name, score))


    finally:
        # Release resources
        cam.release()
    # cv2.destroyAllWindows()
## setup video cam
cam = cv2.VideoCapture(0)
## fetch model
model = get_model()
## initializing the queue
gesture_queue = Queue()
## running