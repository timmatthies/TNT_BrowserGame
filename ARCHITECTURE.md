# Architecture Diagram

## Chrome Dino Game Automation Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                       CHROME BROWSER                            │
│  ┌───────────────────────────────────────────────────────┐     │
│  │                  Dino Game                             │     │
│  │                                                        │     │
│  │    ╔══╗                                               │     │
│  │    ║  ║          Sky (light pixels)                   │     │
│  │   ╔╝  ╚╗  ────────────────────────────────            │     │
│  │   ║    ║         Detection Point (x,y)                 │     │
│  │   ╚════╝              ↓                                │     │
│  │  ────────────────  🌵  ──────────────                 │     │
│  │      Ground                                            │     │
│  └───────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    [ SCREEN CAPTURE ]
                    PIL.ImageGrab.grab()
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   PYTHON AUTOMATION SCRIPT                       │
│                       (dino_game.py)                             │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  1. CAPTURE SCREEN                                     │    │
│  │     capture_screen() → PIL.Image                       │    │
│  └────────────────────────────────────────────────────────┘    │
│                              ↓                                   │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  2. GET PIXEL AT (x, y)                                │    │
│  │     image.getpixel((300, 400))                         │    │
│  │     → (R, G, B) tuple                                  │    │
│  └────────────────────────────────────────────────────────┘    │
│                              ↓                                   │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  3. CALCULATE BRIGHTNESS                               │    │
│  │     brightness = (R + G + B) / 3                       │    │
│  └────────────────────────────────────────────────────────┘    │
│                              ↓                                   │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  4. CHECK IF DARK                                      │    │
│  │     is_pixel_dark(image, x, y)                         │    │
│  │     → brightness < 127 ?                               │    │
│  └────────────────────────────────────────────────────────┘    │
│                              ↓                                   │
│               ┌──────────────┴──────────────┐                   │
│               │                             │                   │
│          [YES: DARK]                   [NO: LIGHT]              │
│               │                             │                   │
│               ↓                             ↓                   │
│  ┌─────────────────────────┐    ┌─────────────────────────┐   │
│  │  5a. PRESS SPACEBAR     │    │  5b. CONTINUE LOOP      │   │
│  │  pyautogui.press('space')│    │  (no action)            │   │
│  │  → Dino jumps!          │    │                         │   │
│  └─────────────────────────┘    └─────────────────────────┘   │
│               │                             │                   │
│               └──────────────┬──────────────┘                   │
│                              ↓                                   │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  6. WAIT & REPEAT                                      │    │
│  │     time.sleep(0.01)                                   │    │
│  │     → Loop back to step 1                              │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

## Configuration Parameters

| Parameter              | Default | Description                           |
|------------------------|---------|---------------------------------------|
| OBSTACLE_DETECTION_X   | 300     | X coordinate to monitor               |
| OBSTACLE_DETECTION_Y   | 400     | Y coordinate to monitor               |
| DARK_PIXEL_THRESHOLD   | 127     | Brightness threshold (0-255)          |
| CHECK_INTERVAL         | 0.01    | Seconds between checks                |

## Dependencies

```
pillow (PIL)    → Screen capture via ImageGrab
pyautogui       → Keyboard automation (spacebar press)
```

## Key Algorithm

```python
while game_running:
    screen = capture_screen()
    pixel = screen.getpixel((x, y))
    brightness = sum(pixel[:3]) / 3
    
    if brightness < THRESHOLD:
        press_spacebar()
        sleep(0.3)  # Prevent double jumps
    
    sleep(0.01)
```

## Usage Flow

```
User → Open Chrome Dino → Position window → Run script → Auto-play!
```
