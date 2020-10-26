import pyautogui
import time
import random

num = 10

for i in range(num):
    # 画像が出るまでtabを押す
    while pyautogui.locateOnScreen('C://Users//ykita//vscode//scraping//image_win.png', confidence=0.9) is None:
        #pyautogui.press('tab')
        time.sleep(1)
        print(pyautogui.position())

    x, y = pyautogui.locateCenterOnScreen(
        'C://Users//ykita//vscode//scraping//image_win.png', confidence=0.9)
    print(str(x)+','+str(y))
    