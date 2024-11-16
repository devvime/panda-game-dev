from core.game_object import GameObject
from panda3d.bullet import BulletBoxShape
from panda3d.core import Vec3

class Scenery(GameObject):
    def __init__(self, model_path, animations = None, position=(0, 0, 0), scale=1.0):
        super().__init__(model_path, animations, position, scale)
        
        shape = BulletBoxShape(Vec3(100, 100, 1))
        self.add_rigid_body(shape, mass=0)

    def update(self, task):
        return super().update(task)
