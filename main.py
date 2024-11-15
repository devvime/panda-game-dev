from panda3d.core import loadPrcFile
loadPrcFile('config.prc')

from direct.showbase.ShowBase import ShowBase
from core.scene_manager import SceneManager

from scenes.main_menu import MainMenuScene
from scenes.gameplay import GameScene

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        
        self.scene_manager = SceneManager(self)
        
        self.main_menu_scene = MainMenuScene(self)
        self.game_scene = GameScene(self)

        self.scene_manager.change_scene(self.main_menu_scene)

        self.accept("enter", self.handle_input, ["enter"])
        self.accept("escape", self.handle_input, ["esc"])
        
        self.taskMgr.add(self.scene_manager.update, "scene_update")


    def handle_input(self, key):
        self.scene_manager.input(key)

game = Game()
game.run()
