class GameChannel < ApplicationCable::Channel
  def subscribed
    stream_from "game_channel"
    Rails.logger.info "Client subscribed to GameChannel"
  end

  def unsubscribed
    # Any cleanup needed when channel is unsubscribed
    Rails.logger.info "Client unsubscribed from GameChannel"
  end

  # This method handles messages received from clients.
  def receive(data)
    Rails.logger.info "Received data in GameChannel: #{data.inspect}"
    # Echo the data back to all clients (including the sender)
    ActionCable.server.broadcast("game_channel", data)
  end
end
