from core.game_object import GameObject
from panda3d.bullet import BulletBoxShape
from panda3d.core import Vec3

class Player(GameObject):
    def __init__(self, model_path, animations = None, position=(0, 0, 0), scale=1.0):
        super().__init__(model_path, animations, position, scale)
        self.speed = 5
        
        self.rb = self.add_rigid_body(BulletBoxShape(Vec3(2.5, 2.5, 6)), mass=1)

    def move(self, direction):
        if self.physics_node and self.physics_node.isDynamic():
            velocity = Vec3(*direction) * self.speed
            self.physics_node.setLinearVelocity(velocity)

    def update(self, task):
        return super().update(task)
