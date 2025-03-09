class GameChannel < ApplicationCable::Channel
  # Use a class variable to store player positions.
  # For production use, consider a persistent store like Redis.
  NUM_OF_PLAYERS = 3
  @@players = {}
  @@game_started = false
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

    # Update or add the player's position.
    @@players[player_id] = { x: x, y: y }

    # If we haven't started the game yet and the number of players reaches the constant, broadcast a game start message.
    unless @@game_started
      if @@players.keys.size >= NUM_OF_PLAYERS
        
        ActionCable.server.broadcast("game_channel", message: "Game Start", players: @@players)
        # Log when the game start gets triggered.
        Rails.logger.info "Game start triggered with players: #{@@players.inspect}"
        @@game_started = true
      else
        # Still waiting for all players.
        ActionCable.server.broadcast("game_channel", players: @@players)
      end
    else
      # Game has started; broadcast updated positions.
      ActionCable.server.broadcast("game_channel", players: @@players)
    end
  end
end

