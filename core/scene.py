class Scene:
    def __init__(self, game):
        self.game = game
        self.is_loaded = False

    def load(self):
        self.is_loaded = True

    def unload(self):
        self.is_loaded = False

    def update(self, task):
        return task.cont

    def input(self, key):
        pass
