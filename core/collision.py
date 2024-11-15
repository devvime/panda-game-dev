from panda3d.core import CollisionTraverser, CollisionHandlerPusher

class Collision:
    def __init__(self):        
        self.collision_traverser = CollisionTraverser()
        self.collision_handler = CollisionHandlerPusher()
        self.collision_traverser.showCollisions(render)
        
    def update(self):
        self.collision_traverser.traverse(render)
        
def set_collision(collision, collider, node):
    collision.collision_traverser.addCollider(collider, collision.collision_handler)
    collision.collision_handler.addCollider(collider, node)