"""
Chrome Dino Game Automation Script

This script automates playing the Chrome Dino game by:
1. Capturing the screen to detect obstacles
2. Pressing spacebar when an obstacle is detected (dark pixel)
"""

import time
from PIL import ImageGrab
import pyautogui
import argparse
import keyboard

# Configuration
OBSTACLE_DETECTION_X = 830  # X coordinate to check for obstacle
OBSTACLE_DETECTION_Y = 248  # Y coordinate to check for obstacle   
BIRD_DETECTION_X = 835  # X coordinate to check for flying bird obstacle
BIRD_DETECTION_Y = 215  # Y coordinate to check for flying bird obstacle
DARK_PIXEL_THRESHOLD = 127  # Threshold below which a pixel is considered dark (0-255)
CHECK_INTERVAL = 0.01  # Time between checks in seconds
DINO_X = 703
DINO_Y = 252


def capture_screen():
    """
    Capture the current screen.
    
    Returns:
        PIL.Image: Screenshot of the screen
    """
    return ImageGrab.grab()


def is_pixel_dark(image, x, y, threshold=DARK_PIXEL_THRESHOLD): 
    """
    Check if a pixel at given coordinates is dark.
    
    Args:
        image (PIL.Image): The image to check
        x (int): X coordinate
        y (int): Y coordinate
        threshold (int): RGB value below which pixel is considered dark
        
    Returns:
        bool: True if pixel is dark, False otherwise
    """
    try:
        for i in range(3):
            for j in range(3):
                pixel = image.getpixel((x + i, y + j))
                brightness = sum(pixel[:3]) / 3
                if brightness < threshold:
                    return True
        return False
        # For RGB, check if all channels are below threshold
        # if isinstance(pixel, tuple):
        #     # Calculate average brightness
        #     brightness = sum(pixel[:3]) / 3
        #     return brightness < threshold
        # else:
        #     # Grayscale
        #     return pixel < threshold
    except Exception as e:
        print(f"Error checking pixel: {e}")
        return False


def press_spacebar():
    """
    Press the spacebar to make the dino jump.
    """
    pyautogui.press('space')


def dino_at_pos(image, x, y, threshold=DARK_PIXEL_THRESHOLD):
    """
    Check if the dino is at the given position (not jumped).
    
    Args:
        image (PIL.Image): The image to check
        x (int): X coordinate
        y (int): Y coordinate
        threshold (int): RGB value below which pixel is considered dark
    Returns:
        bool: True if dino is at position, False otherwise
    """
    try:
        for i in range(10):
            for j in range(3):
                pixel = image.getpixel((x + i, y + j))
                brightness = sum(pixel[:3]) / 3
                if brightness < threshold:
                    return True
        return False
    except Exception as e:
        print(f"Error checking dino position: {e}")
        return False

def play_dino_game(x=OBSTACLE_DETECTION_X, y=OBSTACLE_DETECTION_Y, bird_x=BIRD_DETECTION_X, bird_y=BIRD_DETECTION_Y,
                   threshold=DARK_PIXEL_THRESHOLD, interval=CHECK_INTERVAL, dino_x=DINO_X, dino_y=DINO_Y):
    """
    Main game loop that monitors the screen and presses spacebar when obstacle detected.
    
    Args:
        x (int): X coordinate to check for obstacle
        y (int): Y coordinate to check for obstacle
        threshold (int): RGB threshold for dark pixel detection
        interval (float): Time between checks in seconds
    """
    print("Starting Dino Game Automation...")
    print(f"Monitoring pixel at ({x}, {y})")
    print(f"Monitoring bird at ({bird_x}, {bird_y})")
    print(f"Dark pixel threshold: {threshold}")
    print("Press Ctrl+C to stop")
    print("Starting in 3 seconds...")
    time.sleep(3)
    isflying = False
    shouldjump = False
    
    try:
        while True:
            # Capture screen
            screen = capture_screen()
            if shouldjump and not isflying:
                time.sleep(0.2)
                press_spacebar()
                shouldjump = False    

            # If p is pressed
            if keyboard.is_pressed('p'):
                print("HIHIHIHIHI")
                shouldjump = True  
            
            # Check if pixel is dark (obstacle present)
            if is_pixel_dark(screen, x, y, threshold):
                if isflying:
                    shouldjump = True
                    print("Should jump after landing")
                
                press_spacebar()
                print(f"Obstacle detected! Jumping...")
                # Small delay after jump to avoid double jumps
                time.sleep(0.1)



            # Check if bird is present
            if is_pixel_dark(screen, bird_x, bird_y, threshold):
                press_spacebar()
                print(f"Bird detected! Jumping...")
                # Small delay after jump to avoid double jumps
                time.sleep(0.3)

            if dino_at_pos(screen, dino_x, dino_y, threshold):
                isflying = False
            else:
                isflying = True

            # Wait before next check
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\nStopping Dino Game Automation...")


if __name__ == "__main__":
    # You can customize these values based on your screen resolution and game position
    # Example usage:
    # play_dino_game(x=300, y=400, threshold=127)

    
    play_dino_game()


    # while True:
    #     print(pyautogui.position())
    #     time.sleep(1)