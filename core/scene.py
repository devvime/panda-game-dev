from panda3d.core import Vec3
from panda3d.bullet import BulletWorld, BulletDebugNode
from states.game import game_states

class Scene:
    def __init__(self, game):
        self.game = game
        self.is_loaded = False
        
        self.physics_world = BulletWorld()
        self.physics_world.setGravity(game_states['gravity'])

    def load(self):
        self.is_loaded = True

    def unload(self):
        self.is_loaded = False

    def update(self, task):
        self.dt = globalClock.getDt()
        self.physics_world.doPhysics(self.dt)
        return task.cont

    def input(self, key):
        pass
    
    def debug(self):
        debug_node = BulletDebugNode('Debug')
        debug_node.showWireframe(True)
        debug_node.showConstraints(True)
        debug_node.showBoundingBoxes(False)
        debug_node.showNormals(False)
        self.debug_np = render.attachNewNode(debug_node)
        self.physics_world.setDebugNode(self.debug_np.node())
        self.debug_np.show()
