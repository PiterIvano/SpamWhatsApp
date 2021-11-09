import pyautogui
import time 
import os


message = input("Ingrese el mensaje->>> ")
cant = int(input("Ingrese la cantidad de veces->>> "))
num = str(input("Ingrese el numero->>> "))
n = 500

print("Iniciando...")
count = 5 
while count != 0:
    time.sleep(1)
    count -= 1

print("Iniciando Navegador...")

for i in range(0, int(n)):
    ##############################################################################################
    os.system(f'start chrome "https://web.whatsapp.com/send?phone=%2B{num}&text=h&app_absent=0"')
    time.sleep(20)
    print("Navegador abierto")
    time.sleep(1)
    print("Escribiendo...")
    pyautogui.typewrite('\n')
    
    
    x = 1
    while x <= int(cant):
        pyautogui.typewrite(message + '\n')
        time.sleep(0.5)
        x += 1
        print(f"Mensaje numero: {x}")
        if x == int(cant):
            print("Fin de la escritura")
            exit()
