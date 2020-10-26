import pyautogui
import time
import random

num = int(input('巡回人数？'))

for i in range(num):
    # 画像が出るまでtabを押す
    k=0
    while pyautogui.locateOnScreen('C://Users//ykita//vscode//scraping//image_win.png', confidence=0.95) is None:
        pyautogui.press('tab')
        time.sleep(0.1*random.random())
        k+=1
        #100回押しても切り替わらない時は、シャットダウンする
        if k==100:
            pyautogui.hotkey('alt', 'f4')

    x, y = pyautogui.locateCenterOnScreen(
        'C://Users//ykita//vscode//scraping//image_win.png', confidence=0.95)
    pyautogui.click(x, y)
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

#ノルマを終えたらシャットダウン        
pyautogui.hotkey('alt', 'f4')