# Panda Game Dev
Game dev template for Panda3D

### Project structure

```
/my_game
│
├── /assets
│   ├── /models                   # 3D Models (.egg, .gltf, .glb)
│   ├── /textures                 # Textures images
│   ├── /audio                    # Sound files
│
├── /config
│   ├── /config.prc               # Panda configuration file
│   ├── /inputs.py                # Input keys config
│
├── /core                         
│   ├── game_object.py            # Base Class for all Game Objects
│   ├── scene_manager.py          # Manager for all scenes
│   ├── scene.py                  # Base Class for all scenes
│
├── /entities                     # Game object classes
│   ├── player.py
│   ├── enemy.py
│   ├── environment.py
│
├── /scenes                       # Game scenes, each in a separate file
│   ├── main_menu.py
│   ├── game.py
│
├── /states                       # Game states
│   ├── keys.py                   # Input keys
│
├── main.py                       # Init game
```