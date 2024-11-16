from core.game_object import GameObject
from panda3d.bullet import BulletSphereShape

class Enemy(GameObject):
    def __init__(self, model_path, animations = None, position=(0, 0, 0), scale=1.0):
        super().__init__(model_path, animations, position, scale)
        self.health = 100
        
        shape = BulletSphereShape(1.0)
        self.add_rigid_body(shape, mass=1)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.destroy()
