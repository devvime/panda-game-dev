from core.game_object import GameObject

class Player(GameObject):
    def __init__(self, model_path, animations = None, position=(0, 0, 0), scale=1.0):
        super().__init__(model_path, animations, position, scale)
        self.speed = 5

    def move(self, direction):
        dx, dy, dz = direction
        self.node.setPos(self.node.getX() + dx * self.speed,
                         self.node.getY() + dy * self.speed,
                         self.node.getZ() + dz * self.speed)

    def update(self, task):
        return super().update(task)
    
    def handle_collision(self, other):
        print(f"Player collision in {other}")
