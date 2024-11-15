from panda3d.core import CollisionCapsule, CollisionSphere, CollisionBox, CollisionInvSphere
from core.scene import Scene
from core.collision import Collision, set_collision
from states.game import game_states

from entities.player import Player
from entities.enemy import Enemy
from entities.scenery import Scenery

class GameScene(Scene):    
    def load(self):
        super().load()
        
        self.game.disableMouse()
        self.game.camera.setPos(90, 144, 80)
        self.game.camera.setHpr(143, -20, 10)
        
        self.collision = Collision()
        
        self.player = Player("assets/models/player/panda", None, position=(-50, 0, 0), scale=1)
        self.player.node.reparentTo(render)
        self.player_collider = self.player.add_collider(CollisionCapsule(0, 0, 0, 0, 0, 0, 0.2), "player")
        self.player_collider.show()
        set_collision(self.collision, self.player_collider, self.player.node)

        self.enemy = Enemy("assets/models/enemy/jack", None, position=(5, 5, 0), scale=1)
        self.enemy.node.reparentTo(render)

        self.scenery = Scenery("assets/models/scenery/environment", None, position=(0, 0, -1), scale=1)
        self.scenery.node.reparentTo(render)
        
    def unload(self):
        self.player.destroy()
        self.enemy.destroy()
        self.scenery.destroy()
        super().unload()
    
    def input(self, key):
        if key == 'esc':
            game_states['paused'] = True
            self.game.scene_manager.change_scene(self.game.main_menu_scene)

    def update(self, task):
        # code here
        self.collision.update()
        return super().update(task)