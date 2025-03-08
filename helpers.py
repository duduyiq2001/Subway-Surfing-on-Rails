from queue import Empty
import pygame

### generate a closure call back function with
### error handling
def create_gesture_update(queue, mapping):
    def gesture_update(player):
        try:
            latest = None
            name,score = queue.get_nowait()
            print(f"gesture detected {name} with score: {score}")
            if name != None and name in mapping:
                if mapping[name] == "left":
                    player.move_left()
                if mapping[name] == "right":
                    player.move_right()
        except Empty:
            return latest
    return gesture_update

### callback for keyboard handling
def keyboard_update(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move_left()
    if keys[pygame.K_d]:
        player.move_right()


