import pyautogui, time
time.sleep(5)
f = open("words.txt", 'r')
print("You have 5 seconds to click on target text box!")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")