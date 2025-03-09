import websocket
import json
import logging
import time
import threading

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
def send_test_messages(ws):
   while True:
            # For example, sending a dummy position update for player 'player1'
            update = {
                "player_id": "player1",
                "x": 100,  # Replace with your dynamic position value
                "y": 200
            }
            ws.send(json.dumps(update))
            time.sleep(0.1)
def on_message(ws, message):
    data = json.loads(message)
    # data should include a "players" key with a dict of all players.
    print("Received update:", data)

def on_error(ws, error):
    logging.error("Error: %s", error)

def on_close(ws, close_status_code, close_msg):
    logging.info("Connection closed: %s, %s", close_status_code, close_msg)

def on_open(ws):
    logging.info("Connection opened")
    # Subscribe to the GameChannel (adjust channel name as needed)
    subscribe_message = {
        "command": "subscribe",
        "identifier": json.dumps({"channel": "GameChannel"})
    }
    ws.send(json.dumps(subscribe_message))
    logging.info("Subscribed to GameChannel")
    
    # Start a thread to send test messages repeatedly
    thread = threading.Thread(target=send_test_messages, args=(ws,))
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    # Enable WebSocket trace for debugging (optional)
    websocket.enableTrace(True)
    
    # Replace with your Action Cable URL
    ws_url = "ws://127.0.0.1:3000/cable"
    
    # Create the WebSocketApp and assign callbacks
    ws_app = websocket.WebSocketApp(
        ws_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    
    # Run the connection indefinitely
    ws_app.run_forever()
