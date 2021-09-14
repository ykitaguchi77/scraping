import pyautogui
import time
import random
import sys

num = int(input('巡回人数？'))
print("カーソルが出た状態からスタート")
time.sleep(10)

l=0
for i in range(num):
    # 画像が出るまでtabを押す
    k=0

    while pyautogui.locateOnScreen('C://Users//ykita//vscode//scraping//image_win.png', confidence=0.95) is None:
        pyautogui.press('tab')
        time.sleep(0.1*random.random())
        k+=1
        print("tab: "+str(k))
        #100回押しても切り替わらない時は、シャットダウンする
        if k==100:
            pyautogui.hotkey('alt', 'f4')
            sys.exit("Exit because no image found")


    try:
        x, y = pyautogui.locateCenterOnScreen(
            'C://Users//ykita//vscode//scraping//image_win.png', confidence=0.95)
        pyautogui.click(x, y)
        time.sleep(3 + random.random())

        interest = random.randint(0,1)
        if interest == 0:                       
            time.sleep(0.1)
        elif interest ==1:
            scroll = random.randint(10, 20)
            for i in range(scroll):
                pyautogui.scroll(-200)  # 下スクロールする
                time.sleep(0.5 * random.random())
        time.sleep(1 + 3 * random.random())
        pyautogui.hotkey('alt', 'left')  # windowsの戻る

        time.sleep(1 + 3 * random.random())
        pyautogui.scroll(-200)  # 下スクロールする
        time.sleep(0.5 + random.random())
        pyautogui.press('tab')

        print(str(i))

        l=0

    except:
        pass
        l+=1
        pyautogui.press('tab')
        print("notFoundError: "+str(l))
        if l == 100:
            pyautogui.hotkey('alt', 'f4')


    # 2%の確率で1分休む
    a = random.randint(0, 50)
    if a == 0:
        time.sleep(60*random.random())

    # 0.2%の確率で30分休む
    a = random.randint(0, 500)
    if a == 0:
        time.sleep(1800*random.random())


#ノルマを終えたらシャットダウン
pyautogui.hotkey('alt', 'f4')