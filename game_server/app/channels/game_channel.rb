class GameChannel < ApplicationCable::Channel
  # Use a class variable to store player positions.
  # For production use, consider a persistent store like Redis.
  @@players = {}

  def subscribed
    stream_from "game_channel"
    # Optionally notify the client that it has subscribed successfully.
    transmit({ message: "Welcome to the game!" })
  end

  def unsubscribed
    # Optionally remove a player's data when they disconnect.
    # You might need to know the player id from the connection or a parameter.
    # For example, if you set current_player_id in connection:
    # @@players.delete(current_player_id)
  end

  # This method is called when the server receives a message from the client.
  def receive(data)
    # Expected data format: {"player_id": "player1", "x": 100, "y": 200}
    player_id = data["player_id"]
    x = data["x"]
    y = data["y"]

    # Update the player's position in the shared hash.
    @@players[player_id] = { x: x, y: y }

    # Option 1: Immediately broadcast the full players hash to all subscribers.
    ActionCable.server.broadcast("game_channel", players: @@players)

    # Option 2: Alternatively, you could broadcast on a fixed interval using a scheduled task.
  end
end

