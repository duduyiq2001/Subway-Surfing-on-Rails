from queue import Empty
import pygame


### generate a closure call back function with
### error handling
def create_gesture_update(queue, mapping):
    def gesture_update(player):
        try:
            latest = None
            name, score = queue.get_nowait()
            #print(f"gesture detected {name} with score: {score}")
            if name is not None and name in mapping:
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


## send one position update to socket
def get_send_update(ws):
    def send_update(id,pos):
        try:
            ws.emit('update', {'player_id':id, 'x':pos[0], 'y':pos[1]})
        except Exception:
            print(f'got error')
    return send_update


### block is enabled and timeout = None queue
def wait_on_start(queue):
    msg = ''
    players = None
    while(msg != 'Game Start'):
        msg = queue.get()
        print(f'msg is {msg}')
        players = msg['players']
        msg = msg['message']
    return players

### fetching on pos of other players
def wait_on_pos(queue):
    msg = queue.get_nowait()
    return msg['players']

#### ping the server
def send_one_update(sio, player_id):
    sio.emit('update', {'player_id': player_id, 'x': 0, 'y': 0})
    

def draw_players(players, me, surface):
    """
    Draw the player on the given surface.
    If you have a sprite/image, you can blit it. Otherwise, draw a rectangle as a placeholder.

    :param surface: The pygame surface to draw on.
    """
    # If you have an image:
    # surface.blit(self.image, (self.x, self.y))

    # Using a rectangle placeholder:

    for player in players:
        if player != me.id:
            p = players[player]
            canva_y = me.y - (p['y']- me.world_y )
            pygame.draw.rect(
                surface,
                "red",
                (
                    p['x'] - 25,
                    canva_y - 25,
                    50,
                    50,
                ),
            )

            # draw collision box
            pygame.draw.rect(
                surface,
                (0, 255, 0),
                (
                    p['x'] - 25,
                    canva_y - 25,
                    50,
                    50,
                ),
                1,
            )






