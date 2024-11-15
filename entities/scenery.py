from core.game_object import GameObject

class Scenery(GameObject):
    def __init__(self, model_path, position=(0, 0, 0), scale=1.0):
        super().__init__(model_path, position, scale)

    def update(self, task):
        return super().update(task)
