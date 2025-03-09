import websocket
import json
import logging
import time
import threading
import argparse
from functools import partial
# Disable websocket trace
websocket.enableTrace(False)


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def send_test_messages(ws, player_id):
    """Continuously send position updates using the provided player_id."""
    while True:
    # Construct a message according to Action Cable protocol.
        message = {
            "command": "message",
            "identifier": json.dumps({"channel": "GameChannel"}),
            "data": [json.dumps({
                "player_id": player_id,
                "x": 100,  # Replace with dynamic position if needed
                "y": 200
            }), json.dumps({
                "player_id": player_id,
                "x": 100,  # Replace with dynamic position if needed
                "y": 200
            }) ]
        }
        ws.send(json.dumps(message))
        time.sleep(0.1)  # Adjust the frequency as needed
def send_register(ws, player_id):

    message = {
            "command": "message",
            "identifier": json.dumps({"channel": "GameChannel"}),
            "data": [json.dumps({
                "player_id": player_id,
                "x": 100,  # Replace with dynamic position if needed
                "y": 200
            }), json.dumps({
                "player_id": player_id,
                "x": 100,  # Replace with dynamic position if needed
                "y": 200
            })]
        }
    ws.send(json.dumps(message))

def on_message(ws, message):
    data = json.loads(message)
    # Data should include a "players" key with a dict of all players.
    # Check if the message is a ping and ignore it if so.
    if data.get("type") == "ping":
        return
    print("Received update:", data)

def on_error(ws, error):
    logging.error("Error: %s", error)

def on_close(ws, close_status_code, close_msg):
    logging.info("Connection closed: %s, %s", close_status_code, close_msg)

def on_open(ws, player_id):
    logging.info("Connection opened")
    # Subscribe to the GameChannel
    subscribe_message = {
        "command": "subscribe",
        "identifier": json.dumps({"channel": "GameChannel"})
    }
    ws.send(json.dumps(subscribe_message))
    logging.info("Subscribed to GameChannel")
    
    # Start a thread to send test messages repeatedly with the given player_id
    thread = threading.Thread(target=send_register, args=(ws, player_id))
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    # Parse the player_id from the command line
    parser = argparse.ArgumentParser(description="Test WebSocket connection with player_id.")
    parser.add_argument("--player_id", required=True, help="The player id to send to the server.")
    args = parser.parse_args()
    player_id = args.player_id

    # Enable WebSocket trace for debugging (optional)
    websocket.enableTrace(True)
    
    # Replace with your Action Cable URL
    ws_url = "ws://127.0.0.1:3000/cable"
    
    # Create the WebSocketApp with a partial function to pass in player_id
    ws_app = websocket.WebSocketApp(
        ws_url,
        on_open=partial(on_open, player_id=player_id),
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    
    # Run the connection indefinitely
    ws_app.run_forever()
