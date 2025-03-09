import random
from obstacle import Obstacle

class ObstacleManager:
    """
    Manages the spawning and updating of obstacles.
    """
    
    def __init__(self, track_positions, seg_length, objs):
        self.track_positions = track_positions
        self.tracks = len(track_positions)
        self.obstacles = objs
        self.seg_length = seg_length

        
    def update(self, p_world, pcanva, seg_length):
        """
        Updates all obstacles and spawns new ones if necessary.
        """
        for obstacle in self.obstacles:
            obstacle.update(p_world, pcanva,seg_length)
                    
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