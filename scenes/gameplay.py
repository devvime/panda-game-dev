from core.scene import Scene
from states.game import game_states

from entities.player import Player
from entities.enemy import Enemy
from entities.scenery import Scenery

class GameScene(Scene):    
    def load(self):
        super().load()
        
        self.debug()
        
        # self.game.disableMouse()
        # self.game.camera.setPos(90, 144, 80)
        # self.game.camera.setHpr(143, -20, 10)
        base.useDrive()
        
        self.player = Player("assets/models/player/panda", None, position=(-50, 0, 10), scale=1)
        self.player.add_to_physics_world(self.physics_world)
        self.player.node.reparentTo(render)

        self.enemy = Enemy("assets/models/enemy/jack", None, position=(5, 5, 0), scale=1)
        self.enemy.node.reparentTo(render)

        self.scenery = Scenery("assets/models/scenery/environment", None, position=(0, 0, -1), scale=1)
        self.scenery.add_to_physics_world(self.physics_world)
        self.scenery.node.reparentTo(render)
        
    def unload(self):
        self.player.destroy()
        self.player.remove_from_physics_world(self.physics_world)        
        self.enemy.destroy()        
        self.scenery.destroy()
        self.scenery.remove_from_physics_world(self.physics_world)
        super().unload()
    
    def input(self, key):
        if key == 'esc':
            game_states['paused'] = True
            self.game.scene_manager.change_scene(self.game.main_menu_scene)

    def update(self, task):
        # code here
        return super().update(task)