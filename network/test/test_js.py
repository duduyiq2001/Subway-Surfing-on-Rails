import socketio
import time
import argparse
import threading
from socketio.exceptions import TimeoutError

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to Socket.IO server")

@sio.event
def disconnect():
    print("Disconnected from server")

@sio.on('message')
def on_message(data):
    print("Received message:", data)

@sio.on('update')
def on_update(data):
    print("Received update:", data)

@sio.on('game_start')
def on_game_start(data):
    print("Game started:", data)

def send_updates(player_id, initial_y):
    # Send position updates continuously
    i = 0
    while True:
        sio.emit('update', {'player_id': player_id, 'x': 100, 'y': initial_y + 0.1*i })
        time.sleep(2)
        i+=1
def send_one_update(player_id):
    sio.emit('update', {'player_id': player_id, 'x': 100, 'y': 200})
    time.sleep(0.1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket.IO Game Client")
    parser.add_argument("--player_id", required=True, help="Player ID to use")
    parser.add_argument("--initial", required=True, help="initial y")

    args = parser.parse_args()
    player_id = args.player_id
    i_y = int(args.initial)

    sio.connect('http://localhost:3000')
    
    # # Start sending updates in a loop (in the main thread or a separate thread)
    # send_one_update(player_id)

    thread = threading.Thread(target=send_updates, args=(player_id, i_y))
    thread.daemon = True
    thread.start()

     
    sio.wait()