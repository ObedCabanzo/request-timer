#https://ventura-backend-jaj1.onrender.com/health-check/

import requests
import time

url = 'https://ventura-backend-jaj1.onrender.com/health-check/'  # Reemplaza esto con la URL de tu servidor y ruta específica
try:
    print("Enviando petición...")
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Petición enviada exitosamente")
    else:
        print(f"Error al enviar la petición. Código de estado: {respuesta.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")