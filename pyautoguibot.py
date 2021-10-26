import pyautogui
pyautogui.PAUSE = 1.0

pyautogui.alert("Codigo executando")
pyautogui.press("Winleft")
pyautogui.write('Bloco de notas')
pyautogui.press("enter")
pyautogui.write('Ola Mundo')
pyautogui.press('arquivo')
pyautogui.hotkey('ctrl', 's')
pyautogui.write('testerobo')
pyautogui.press("enter")
pyautogui.hotkey('tab')
pyautogui.press("enter")