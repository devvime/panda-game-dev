class SceneManager:
    def __init__(self, game):
        self.game = game
        self.current_scene = None

    def change_scene(self, new_scene):
        if self.current_scene:
            self.current_scene.unload()

        self.current_scene = new_scene
        self.current_scene.load()

    def update(self, task):
        if self.current_scene and self.current_scene.is_loaded:
            self.current_scene.update(task)
        return task.cont

    def input(self, key):
        if self.current_scene:
            self.current_scene.input(key)
