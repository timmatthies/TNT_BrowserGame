# TNT_BrowserGame

A Python program that automates playing the Chrome Dino game by detecting obstacles and pressing spacebar to jump.

## Features

- **Screen Capture**: Reads the displayed browser content
- **Obstacle Detection**: Monitors specific pixels to detect obstacles (dark pixels)
- **Automatic Jump**: Presses spacebar when an obstacle is detected

## Requirements

- Python 3.6 or higher
- Chrome browser
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/timmatthies/TNT_BrowserGame.git
cd TNT_BrowserGame
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Open Chrome browser and navigate to the Dino game:
   - Type `chrome://dino` in the address bar, OR
   - Disconnect your internet and try to load any webpage

2. Position the game window where you want it on your screen

3. Run the automation script:
```bash
python dino_game.py
```

4. The script will start monitoring after a 3-second countdown
5. Press `Ctrl+C` to stop the automation

## Configuration

You can customize the detection settings by modifying the constants in `dino_game.py`:

- `OBSTACLE_DETECTION_X`: X coordinate to monitor for obstacles (default: 300)
- `OBSTACLE_DETECTION_Y`: Y coordinate to monitor for obstacles (default: 400)
- `DARK_PIXEL_THRESHOLD`: RGB value below which a pixel is considered dark (default: 127)
- `CHECK_INTERVAL`: Time between checks in seconds (default: 0.01)

You can also pass custom values when running:
```python
from dino_game import play_dino_game

# Custom coordinates and threshold
play_dino_game(x=350, y=450, threshold=100)
```

## How It Works

1. **Screen Capture**: The script continuously captures screenshots of your screen using `PIL.ImageGrab`
2. **Pixel Detection**: It checks the RGB value of a specific pixel location where obstacles would appear
3. **Jump Action**: When the pixel becomes dark (indicating an obstacle), it simulates a spacebar press using `pyautogui`

## Tips

- Adjust the `OBSTACLE_DETECTION_X` and `OBSTACLE_DETECTION_Y` coordinates based on your screen resolution and game window position
- Fine-tune the `DARK_PIXEL_THRESHOLD` if the detection is too sensitive or not sensitive enough
- The script includes a small delay after jumping to prevent double jumps

## Troubleshooting

- **No jumps happening**: The pixel coordinates might not be correct for your setup. Try adjusting `OBSTACLE_DETECTION_X` and `OBSTACLE_DETECTION_Y`
- **Too many jumps**: The threshold might be too high. Try lowering `DARK_PIXEL_THRESHOLD`
- **Game not responding**: Make sure the Chrome window is in focus and the game is active

## License

This project is open source and available under the MIT License.