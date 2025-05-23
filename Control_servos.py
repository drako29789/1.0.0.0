#Control_servos.py
# Este script controla dos servos conectados a un Arduino mediante una interfaz gráfica
# Usando Tkinter para la GUI y pySerial para la comunicación serie
# Requiere instalacion de las librerías Tkinter y pySerial
# Para instalar pySerial: pip install pyserial
# Para instalar Tkinter: sudo apt-get install python3-tk (en sistemas basados en Debian/Ubuntu)
# Importar las librerías necesarias

import tkinter as tk
import serial
import time

# Cambia este puerto al que corresponda con tu Arduino (ej: 'COM3' en Windows o '/dev/ttyUSB0' en Linux)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Espera a que Arduino reinicie

def enviar_comando(comando):
    arduino.write(comando.encode())

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Control de Servos")
ventana.geometry("300x250")

# Botones para Servo 1
tk.Label(ventana, text="Servo 1", font=("Arial", 14)).pack(pady=10)
tk.Button(ventana, text="↶ Izquierda", command=lambda: enviar_comando('A')).pack(pady=5)
tk.Button(ventana, text="↷ Derecha", command=lambda: enviar_comando('B')).pack(pady=5)

# Botones para Servo 2
tk.Label(ventana, text="Servo 2", font=("Arial", 14)).pack(pady=10)
tk.Button(ventana, text="↶ Izquierda", command=lambda: enviar_comando('C')).pack(pady=5)
tk.Button(ventana, text="↷ Derecha", command=lambda: enviar_comando('D')).pack(pady=5)

ventana.mainloop()
