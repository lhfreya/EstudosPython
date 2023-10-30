import pyautogui
import time

def abrir_e_escrever_no_bloco_de_notas():
    # Abre o menu Iniciar e busca pelo Bloco de Notas
    pyautogui.press('winleft', interval=0.5)
    pyautogui.write('Notepad', interval=0.25)
    pyautogui.press('enter', interval=0.5)

    # Espera o Bloco de Notas abrir
    time.sleep(2)

    # Escreve um texto no Bloco de Notas
    texto_para_escrever = "Olá, Mundo! Este é um teste de automação com pyautogui."
    pyautogui.write(texto_para_escrever, interval=0.05)

    # Pressiona 'Ctrl + S' para abrir a janela de salvar
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)  # Espera a janela de diálogo "Salvar Como" abrir


    pyautogui.press('enter', interval=0.5)

    # Aguarda a possível janela de confirmação de substituição de arquivo
    time.sleep(1)
    pyautogui.press('left')  # Seleciona "Sim" se perguntar para substituir o arquivo
    pyautogui.press('enter', interval=0.5)

    # Fecha o Bloco de Notas
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    pyautogui.press('enter', interval=0.5)

# Define um breve atraso após cada ação do pyautogui para estabilidade
pyautogui.PAUSE = 0.5

# Alerta o usuário que a automação vai começar
pyautogui.alert('A automação vai começar. Por favor, não use o mouse ou o teclado. Pressione Ctrl+C no terminal para parar.')

# Loop infinito para repetir a automação
try:
    while True:
        abrir_e_escrever_no_bloco_de_notas()
except KeyboardInterrupt:
    # Alerta o usuário que a automação foi interrompida
    pyautogui.alert('A automação foi interrompida pelo usuário.')