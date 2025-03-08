import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


### creating the model object
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)