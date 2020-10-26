import pyautogui
import time
import random

num = int(input('巡回人数？'))

for i in range(num):
    # 画像が出るまでtabを押す
    while pyautogui.locateOnScreen('C://Users//ykita//vscode//scraping//image_win.png', confidence=0.9) is None:
        pyautogui.press('tab')
        time.sleep(0.1*random.random())
        print('aaa')
    x, y = pyautogui.locateCenterOnScreen(
        'C://Users//ykita//vscode//scraping//image_win.png', confidence=0.9)
    pyautogui.click(x, 0.8*y)
    print('clicked')
    time.sleep(3+random.random())
    pyautogui.hotkey('alt', 'left') #windowsの戻る
    time.sleep(1+8*random.random())
    pyautogui.press('tab')

    print(str(i))
    pyautogui.press('down')
    pyautogui.press('down')

    # 2%の確率で10          分休む
    a = random.randint(0, 50)
    if a == 0:
        time.sleep(600)
