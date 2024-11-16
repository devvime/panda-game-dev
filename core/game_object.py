from panda3d.core import Vec3, NodePath
from panda3d.bullet import BulletRigidBodyNode
from direct.actor.Actor import Actor

class GameObject:
    def __init__(self, model_path, animations = None, position=(0, 0, 0), scale=1.0):
        self.node = NodePath("GameObject")
        
        if animations == None:        
            self.model = loader.loadModel(model_path)
            self.model.reparentTo(self.node)
        else:
            self.model = Actor(model_path, animations)
            self.model.reparentTo(self.node)
            self.animations = animations
        
        self.node.setPos(*position)
        self.node.setScale(scale)
        
        self.physics_node = None
        self.shape = None 

    def set_position(self, position: Vec3):
        self.node.setPos(position)
        
    def set_rotation(self, rotation: Vec3):
        self.node.setHpr(rotation)

    def update(self, task):
        pass

    def destroy(self):
        self.node.removeNode()
        self.model.removeNode()
        self.np.removeNode()
        
    def add_rigid_body(self, shape, mass=0):
        self.shape = shape
        self.physics_node = BulletRigidBodyNode(f"{self.node.getName()}_physics")
        self.physics_node.addShape(shape)
        self.physics_node.setMass(mass)

        self.np = render.attachNewNode(self.physics_node)
        self.np.setPos(self.node.getPos())
        self.model.reparentTo(self.np)
        self.model.setZ(-self.np.getZ()/1.6)

        return self.np

    def add_to_physics_world(self, physics_world):
        if self.physics_node:
            physics_world.attachRigidBody(self.physics_node)

    def remove_from_physics_world(self, physics_world):
        if self.physics_node:
            physics_world.removeRigidBody(self.physics_node)
