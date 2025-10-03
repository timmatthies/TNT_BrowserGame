"""
Example usage and testing script for the Dino Game automation.

This script demonstrates the individual functions and how to use them.
"""

from dino_game import capture_screen, is_pixel_dark, press_spacebar, play_dino_game


def example_screen_capture():
    """Example: Capture and display screen information"""
    print("=== Screen Capture Example ===")
    screen = capture_screen()
    print(f"Screen size: {screen.size}")
    print(f"Screen mode: {screen.mode}")
    print()


def example_pixel_check():
    """Example: Check if a specific pixel is dark"""
    print("=== Pixel Detection Example ===")
    screen = capture_screen()
    
    # Check a few different coordinates
    test_coords = [(100, 100), (300, 400), (500, 500)]
    
    for x, y in test_coords:
        is_dark = is_pixel_dark(screen, x, y)
        pixel = screen.getpixel((x, y))
        print(f"Pixel at ({x}, {y}): {pixel} - Dark: {is_dark}")
    print()


def example_spacebar_press():
    """Example: Press spacebar once"""
    print("=== Spacebar Press Example ===")
    print("Pressing spacebar in 2 seconds...")
    import time
    time.sleep(2)
    press_spacebar()
    print("Spacebar pressed!")
    print()


def example_custom_game():
    """Example: Run game with custom settings"""
    print("=== Custom Game Example ===")
    print("This will run the game with custom coordinates")
    print("(Not executing automatically - uncomment to run)")
    # Uncomment the line below to run with custom settings
    # play_dino_game(x=350, y=450, threshold=100, interval=0.02)
    print()


if __name__ == "__main__":
    print("Chrome Dino Game Automation - Examples\n")
    print("Choose an example to run:")
    print("1. Screen Capture")
    print("2. Pixel Detection")
    print("3. Spacebar Press")
    print("4. Custom Game Settings")
    print("5. Run Full Game (default settings)")
    print()
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        example_screen_capture()
    elif choice == "2":
        example_pixel_check()
    elif choice == "3":
        example_spacebar_press()
    elif choice == "4":
        example_custom_game()
    elif choice == "5":
        play_dino_game()
    else:
        print("Invalid choice. Please run again and select 1-5.")
