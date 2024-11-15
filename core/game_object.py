from panda3d.core import Vec3, NodePath, CollisionNode, CollisionSphere, CollisionHandlerPusher
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
        
        self.collision_node = None
        self.collision_handler = None

    def set_position(self, position: Vec3):
        self.node.setPos(position)
        
    def set_rotation(self, rotation: Vec3):
        self.node.setHpr(rotation)

    def update(self, task):
        pass

    def destroy(self):
        self.node.removeNode()
        
    def add_collider(self, shape, tag):
        self.collision_node = CollisionNode(f"{tag}_collider")
        self.collision_node.addSolid(shape)
        collider_path = self.node.attachNewNode(self.collision_node)
        collider_path.setTag("type", tag)
        return collider_path
