import pyautogui
import time
import random

num = int(input('巡回人数？'))

for i in range(num):
    # 画像が出るまでtabを押す
    while pyautogui.locateOnScreen('/Users/kitaguchi/VScode/Scraping/image.png', confidence=0.9) is None:
        pyautogui.press('tab')
        time.sleep(0.1*random.random())
    x, y = pyautogui.locateCenterOnScreen(
        '/Users/kitaguchi/VScode/Scraping/image.png', confidence=0.9)
    pyautogui.click(0.5*x, 0.5*y)
    time.sleep(3+random.random())
    pyautogui.hotkey('command', 'left')
    time.sleep(1+8*random.random())
    pyautogui.press('tab')

    print(str(i))
    pyautogui.press('down')
    pyautogui.press('down')

    # 2%の確率で10          分休む
    a = random.randint(0, 50)
    if a == 0:
        time.sleep(600)
