import random
from obstacle import Obstacle

class ObstacleManager:
    """
    Manages the spawning and updating of obstacles.
    """
    
    def __init__(self, track_positions):
        self.track_positions = track_positions
        self.tracks = len(track_positions)
        self .obstacles = []
        self.spawn_timers = [random.uniform(1, 3) for _ in range(self.tracks)]
        
    def update(self, dt):
        """
        Updates all obstacles and spawns new ones if necessary.
        """
        for obstacle in self.obstacles:
            obstacle.update(dt)
        
        self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.y < 720]

        # Shuffle track order to avoid bias
        track_indices = list(range(self.tracks))
        random.shuffle(track_indices)
        
        for i in track_indices:
            self.spawn_timers[i] -= dt
            if self.spawn_timers[i] <= 0:
                if self._all_tracks_blocked():
                    continue
                self.obstacles.append(Obstacle(i, self.track_positions))
                self.spawn_timers[i] = random.uniform(1, 3)
                    
    def draw(self, screen):
        """
        Draws all obstacles on the screen.
        """
        for obstacle in self.obstacles:
            obstacle.draw(screen)
         
    def check_collision(self, player):
        return any(obstacle.check_collision(player) for obstacle in self.obstacles)  
       
    def _all_tracks_blocked(self):
        """
        Checks if all tracks are blocked by obstacles.
        """
        occupied_tracks = {ob.track_index for ob in self.obstacles}
        return len(occupied_tracks) >= self.tracks-1