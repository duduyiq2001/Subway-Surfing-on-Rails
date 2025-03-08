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
    return recognizer
# implemented as a generator running on another thread
def run_model_on_cam(queue, logfile):
    print("wefbewjfbewjkfnbwekfenfkewnfkewnfknfewkf")
    ## setup video cam
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Camera failed to open.")
        return
    ## fetch model
    recognizer = get_model()
    try:
        with open(logfile, 'a') as f:
            f.write("run_model_on_cam started")
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
                        log_entry = f" Gesture detected: {name}, Score: {score}"
                        print(f" Gesture detected: {name}, Score: {score}")
                    
                        f.write(log_entry)
                        ## put gesture into queue
                        queue.put((name, score))
    except Exception as e:
        print(f"Error in run_model_on_cam: {e}")


    finally:
        # Release resources
        cam.release()
    # cv2.destroyAllWindows()
# queue = Queue()
# run_model_on_cam(queue,"a.txt")