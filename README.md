# subwaysurfers on the rails

## 1. Description

The game is basically like 2D version of subway surfers,  the camera from top to bottom, there are 5 lanes,

player actions:

turning left, right and jump

## 2. Project structure

```bash
my_infinite_runner_game/
├── hand_gestures/
│   ├── __init__.py
│   ├── gesture_controller.py
│   └── gesture_recognizer.py
├── network/
│   ├── __init__.py
│   ├── network_manager.py
│   └── sync_protocols.py
├── resources/
│   ├── images/
│   │   └── ...
│   ├── sounds/
│   │   └── ...
│   └── fonts/
│       └── ...
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── game_loop.py
│   ├── states.py
│   ├── player.py
│   ├── obstacle.py
│   ├── map_generator.py
│   ├── collision.py
│   └── input_mapping.py
└── utils/
    ├── __init__.py
    ├── config.py
    ├── constants.py
    └── logger.py
```

## 1. environment

python 3.9
