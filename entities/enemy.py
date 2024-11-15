from core.game_object import GameObject

class Enemy(GameObject):
    def __init__(self, model_path, position=(0, 0, 0), scale=1.0):
        super().__init__(model_path, position, scale)
        self.health = 100

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.destroy()
