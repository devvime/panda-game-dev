from panda3d.core import NodePath
from direct.actor.Actor import Actor

class GameObject:
    def __init__(self, model_path, position=(0, 0, 0), scale=1.0):
        self.node = NodePath("GameObject")
        
        self.model = loader.loadModel(model_path)
        self.model.reparentTo(self.node)
        
        self.node.setPos(*position)
        self.node.setScale(scale)
        
        if isinstance(self.model, Actor):
            self.animations = {}
        else:
            self.animations = None

    def set_position(self, x, y, z):
        self.node.setPos(x, y, z)

    def update(self, task):
        pass

    def destroy(self):
        self.node.removeNode()
