import pyautogui

#pyautogui will raise a fail safe exception if the cursor is at 0, 0 position

width, height = pyautogui.size()
print(width, height)

# pyautogui.displayMousePosition() - can be run from the terminal to display current mouse position

pyautogui.KEYBOARD_KEYS #show all the key mapping
pyautogui.press('f1') # presses a single key
pyautogui.hotkey('ctrl', 'a') # used for keyboard shortcuts

