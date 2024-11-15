from core.game_object import GameObject

class Enemy(GameObject):
    def __init__(self, model_path, animations = None, position=(0, 0, 0), scale=1.0):
        super().__init__(model_path, animations, position, scale)
        self.health = 100

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.destroy()
            
    def handle_collision(self, other):
        print(f"Enemy collision in {other}")
