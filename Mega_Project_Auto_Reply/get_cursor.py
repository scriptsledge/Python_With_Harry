import pyautogui

# Continuously print the current mouse cursor position
while True:
    position = pyautogui.position()
    print(position)

# Reference coordinates (for specific actions):
# - Open Chrome: 1639, 1412
# - Drag area: From (1003, 237) to (2187, 1258)
# - Copy selection: From (1026, 244) to (1131, 1321)
