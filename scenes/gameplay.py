from core.scene import Scene

from entities.player import Player
from entities.enemy import Enemy
from entities.scenery import Scenery

class GameScene(Scene):
    def load(self):
        super().load()
        
        self.player = Player("assets/models/player/panda", None, position=(0, 0, 0), scale=1)
        self.player.node.reparentTo(render)

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
            self.game.paused = True
            self.game.scene_manager.change_scene(self.game.main_menu_scene)

    def update(self, task):
        # code here
        return super().update(task)