from core.scene import Scene

from direct.gui.DirectGui import DirectButton

class MainMenuScene(Scene):
    def load(self):
        super().load()
        
        self.start_button = DirectButton(
            text="Start Game",
            scale=0.1,
            pos=(0, 0, 0.1),
            command=self.start_game
        )
        
        self.exit_button = DirectButton(
            text="Exit",
            scale=0.1,
            pos=(0, 0, -0.1),
            command=self.exit_game
        )

    def unload(self):
        self.start_button.destroy()
        self.exit_button.destroy()
        super().unload()

    def input(self, key):
        pass
    
    def update(self, task):
        # code here
        return super().update(task)
    
    def start_game(self):
        self.game.scene_manager.change_scene(self.game.game_scene)

    def exit_game(self):
        self.game.userExit()