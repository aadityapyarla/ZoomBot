import pyautogui
import subprocess
from time import sleep
import pandas as pd
from datetime import datetime


def sign_in(meeting_id, meeting_pswd, meeting_name):
    subprocess.call(['/usr/bin/open', '/Applications/zoom.us.app'])
    sleep(15)
    # Join Button 1
    pyautogui.moveTo(586, 381)
    pyautogui.click()
    sleep(2)
    # Meeting Id
    pyautogui.moveTo(630, 401)
    pyautogui.click()
    pyautogui.write(meeting_id)
    sleep(2)
    # Checking media box 2
    pyautogui.moveTo(560, 540)
    pyautogui.click()
    sleep(2)
    # Join button 2
    pyautogui.moveTo(860, 597)
    pyautogui.click()
    sleep(4)
    # Meeting Pswd
    pyautogui.moveTo(724, 405)
    pyautogui.click()
    pyautogui.write(meeting_pswd)
    sleep(2)
    # Join button 3
    pyautogui.moveTo(847, 582)
    pyautogui.click()
    print("Signed In", " - ", meeting_name, " - ", datetime.now().strftime("%H:%M"))
    sleep(2400)
    # Leave Meeting
    pyautogui.moveTo(1396, 873)
    pyautogui.click()


df = pd.read_csv(r'/Users/aaruaadi/Desktop/Python/ZoomBot/schedule.csv')

while True:
    now = datetime.now().strftime("%H:%M")
    if now in str(df['Timings']):
        row = df.loc[df['Timings'] == now]
        m_id = str(row.iloc[0, 2])
        m_pswd = str(row.iloc[0, 3])
        m_name = str(row.iloc[0, 1])
        print("Signing In", " - - ", m_name, " - -  ", now)
        sign_in(m_id, m_pswd, m_name)
    else:
        print("Waiting", " - - ", now)
