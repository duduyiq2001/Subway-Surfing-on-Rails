import unittest
import websocket
import json
import threading
import time
import logging

# Set up logging to see what's happening during the test.
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

class TestGameStartBroadcast(unittest.TestCase):
    WS_URL = "ws://127.0.0.1:3000/cable"
    NUM_CLIENTS = 3

    def setUp(self):
        # This list will collect all messages received by all clients.
        self.received_messages = []
        # We'll use a lock to protect access to self.received_messages.
        self.lock = threading.Lock()

    def subscribe_and_send(self, player_id):
        # Create and connect a WebSocket.
        ws = websocket.WebSocket()
        ws.connect(self.WS_URL)
        
        # Subscribe to the GameChannel.
        subscribe_message = {
            "command": "subscribe",
            "identifier": json.dumps({"channel": "GameChannel"})
        }
        ws.send(json.dumps(subscribe_message))
        logging.info(f"Client {player_id} subscribed to GameChannel.")
        
        # Give the server a moment to process the subscription.
        time.sleep(0.5)
        
        # Send a player update.
        update_message = {
            "command": "message",
            "identifier": json.dumps({"channel": "GameChannel"}),
            "data": json.dumps({"player_id": player_id, "x": 100, "y": 200})
        }
        ws.send(json.dumps(update_message))
        logging.info(f"Client {player_id} sent update.")
        
        # Listen for messages for a fixed period (e.g., 5 seconds).
        start_time = time.time()
        while time.time() - start_time < 5:
            try:
                msg = ws.recv()
                if msg:
                    logging.info(f"Client {player_id} received: {msg}")
                    with self.lock:
                        self.received_messages.append(msg)
            except Exception as e:
                logging.error(f"Client {player_id} encountered error: {e}")
                break
        
        ws.close()

    def test_game_start_broadcast(self):
        threads = []
        # Start NUM_CLIENTS connections.
        for i in range(1, self.NUM_CLIENTS + 1):
            t = threading.Thread(target=self.subscribe_and_send, args=(f"player{i}",))
            threads.append(t)
            t.start()
        
        # Wait for all threads to complete.
        for t in threads:
            t.join()
        
        # Check if any received message contains "Game Start".
        with self.lock:
            game_start_received = any("Game Start" in msg for msg in self.received_messages)
        logging.info("All received messages: " + str(self.received_messages))
        self.assertTrue(game_start_received, "Game Start message was not received by any client.")

if __name__ == '__main__':
    unittest.main()
