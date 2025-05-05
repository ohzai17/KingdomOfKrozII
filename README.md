# Kingdom of Kroz II Pygame Port

A Pygame-based reimagining of the classic ASCII game, Kingdom of Kroz II.

---

## Features
- Pixel art platforming
- Multiple challenging levels
- Save and load system
- Adjustable settings (screen size, controls)

---

## Controls
|   Action   |    Key    |
|:----------:|:---------:|
| Move Left  | ← |,| J |
| Move Right | → |,| L |
| Move Up    | ↑ |,| I |
| Move Down  | ↓ |,| M |
| Up-Left    | U |*↖*
| Up-Right   | O |*↗*
| Down-Left  | N |*↙*
| Down-Right | , |*↘*

Other commands you can invoke in the game:
|            Action              |         Key        |
|:------------------------------:|:------------------:|
| Pause/Unpause                  | P/Any Key          |
| Save                           | S                  |
| Restore                        | R                  |
| Teleport                       | T                  |
| Whip                           | W                  |
| Cloak                          | C                  |
| Quit                           | Q, Esc             |
| Reset found-item descriptions  | +                  |
| Inhibit found-item descriptions| -                  |
| Spawn level-skip stairs        | ( (SECRET mode)    |
| Give extra items               | ) (SECRET mode)    |
---

## How to Run

### Install Requirements
First install the needed libraries:
```bash, cmd, powershell
pip install -r requirements.txt
```
```
Project Structure:

KingdomOfKrozII
│
├── README.md
├── requirements.txt
├── run_game.py
├── run_game.spec
├── __init__.py
│
├── build
│
├── dist
│   ├── run_game.exe # Executable
│   └── src
│       ├── assets
│       │   ├── audio
│       │   │   └── example.wav
│       │   ├── screens_assets
│       │   │   └── example.png
│       │   └── sprites
│       │       └── example.png
│       └── saves
│
└── src
    ├── audio.py
    ├── gameplay.py
    ├── main.py
    ├── screens.py
    ├── utils.py
    │
    ├── assets
    │   ├── audio
    │   │   ├── example.wav
    │   ├── screens_assets
    │   │   └── example.png
    │   └── sprites
    │       └── example.png
    │
    ├── levels
    │   └── maps.py
    │
    ├── ui
    │   └── screens.py
    │
    └── utils
        ├── draw_text.py
        ├── game_text.py
        └── texts.py
```

This project is licensed under the MIT License.

Credits
Contributors: Edward Campion III, Hender Hernandez Caba, Au Sein, Erik Vodanovic

Sound Effects: numpy