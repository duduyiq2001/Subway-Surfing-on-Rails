import socketio
import time
import queue
from socketio.exceptions import TimeoutError






def get_ws_connection(queue):
    sio = socketio.Client()
    sio.connect('http://10.60.0.152:3000')
    @sio.event
    def connect():
        print("Connected to Socket.IO server")

    @sio.event
    def disconnect():
        print("Disconnected from server")

    @sio.on('message')
    def on_message(data):
        print("Received message:", data)
        queue.put(data)

    @sio.on('update')
    def on_update(data):
        print("Received update:", data)
        queue.put(data)

    @sio.on('game_start')
    def on_game_start(data):
        print("Game started:", data)
        queue.put(data)

    
    return sio
def run_client(sio):
    sio.wait()



# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Socket.IO Game Client")
#     parser.add_argument("--player_id", required=True, help="Player ID to use")
#     parser.add_argument("--initial", required=True, help="initial y")

#     args = parser.parse_args()
#     player_id = args.player_id
#     i_y = int(args.initial)

#     sio.connect('http://localhost:3000')
    
#     # # Start sending updates in a loop (in the main thread or a separate thread)
#     # send_one_update(player_id)

#     thread = threading.Thread(target=send_updates, args=(player_id, i_y))
#     thread.daemon = True
#     thread.start()

     
#     sio.wait()