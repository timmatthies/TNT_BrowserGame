# Quick Start Guide

## Installation
```bash
pip install -r requirements.txt
```

## Running the Game Automation

### Step 1: Open Chrome Dino Game
- Method 1: Go to `chrome://dino` in Chrome browser
- Method 2: Disconnect internet and try to load any webpage

### Step 2: Run the Script
```bash
python dino_game.py
```

### Step 3: Position and Calibrate
The script uses default coordinates (x=300, y=400) to detect obstacles. You may need to adjust these based on:
- Your screen resolution
- Browser window position
- Game size

### Adjusting Detection Coordinates
Edit `dino_game.py` and change:
```python
OBSTACLE_DETECTION_X = 300  # Adjust based on where obstacles appear
OBSTACLE_DETECTION_Y = 400  # Height where cactus/bird appears
DARK_PIXEL_THRESHOLD = 127  # How dark must pixel be to trigger jump
```

## How It Works

1. **Screen Reading**: Uses `PIL.ImageGrab.grab()` to capture screen
2. **Pixel Check**: Examines pixel at (x,y) coordinate
3. **Dark Detection**: If pixel RGB average < threshold, it's considered "dark" (obstacle)
4. **Jump Action**: `pyautogui.press('space')` makes dino jump

## Troubleshooting

**Game not jumping?**
- Check if coordinates are correct for your setup
- Try the example_usage.py script to test pixel detection
- Run: `python example_usage.py` and select option 2

**Too many jumps?**
- Increase DARK_PIXEL_THRESHOLD value
- Increase CHECK_INTERVAL for slower checking

**No response?**
- Make sure Chrome window is visible and in focus
- Verify the game is running at the expected position

## Testing Individual Components

Run the example script:
```bash
python example_usage.py
```

Choose options:
1. Test screen capture
2. Test pixel detection
3. Test spacebar press
4. See custom game settings
5. Run full game with default settings
