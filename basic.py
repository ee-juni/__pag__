# Props to https://wikidocs.net/85581

import pyautogui
import keyboard
from time import sleep as wait

def cur_pos():
    a=pyautogui.position()
    print(a)
    return a

def move_to(x,y):
    pyautogui.moveTo(x, y)
    print(f"Moved to:{x},{y}")

def L():
    pyautogui.click()

def R():
    pyautogui.click(button='right')


dummies = []
for i in range(3):
    dummies.append((i,i))


# Set target spots, waiting time, then execute

targets = []
waits = []

n = int(input("\nHow many target spots?: "))
while n:
    wait(1)
    dummies.append(cur_pos())
    if dummies[-1]==dummies[-2] and dummies[-2]==dummies[-3]:
        targets.append(cur_pos())
        waits.append(float(input("\nWait how many minutes?: "))*60)
        n-=1
        dummies=dummies[:-3]

print("Starting in 3 seconds...")
wait(3)

while True:
    if keyboard.is_pressed('q'): #only neccessary when mouse moves fast
        break
    for idx, el in enumerate(targets):
        x,y = el
        move_to(x,y)
        L()
        wait(waits[idx])
    