from panda3d.core import loadPrcFile
loadPrcFile('config/config.prc')
from direct.showbase.ShowBase import ShowBase
from core.scene_manager import SceneManager
from states.keys import keys
from config.inputs import accept_inputs

from scenes.main_menu import MainMenuScene
from scenes.gameplay import GameScene

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        
        self.paused = False
        
        self.scene_manager = SceneManager(self)
        
        # init scene instances
        self.main_menu_scene = MainMenuScene(self)
        self.game_scene = GameScene(self)
        # end scene instances

        self.scene_manager.change_scene(self.main_menu_scene)

        accept_inputs(self)
        self.taskMgr.add(self.scene_manager.update, "scene_update")
        
    def handle_input(self, key, value):
        keys[key] = value
        self.scene_manager.input(key)

game = Game()
game.run()
