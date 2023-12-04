import time
import pyautogui
import keyboard


# Function to save the current screen as an image
def save_image_with_number(number):

    pyautogui.moveTo(40, 40, duration=0.25)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(40, 250, duration=0.25)
    pyautogui.click()
    pyautogui.moveTo(300, 250, duration=0.5)
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.click()
    
    # Wait for the "Save As" dialog to appear
    time.sleep(0.5)
    
    # Enter the desired file name (you may need to adjust these coordinates)
    pyautogui.write(f"four_{number}.png")
    
    # Press Enter to save the image
    pyautogui.press('enter')
    print(f"Saved image {number}")

    # reset the canvas
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.press('ctrl+z')
    pyautogui.moveTo(800, 600, duration=0.25)
# Example usage
for number in range(100):
    
    keyboard.wait('q')

    # Save the image with the corresponding number
    save_image_with_number(number)
    
    