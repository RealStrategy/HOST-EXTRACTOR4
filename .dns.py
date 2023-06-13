import socket

def obtener_dns(nombre_dominio):
    try:
        direcciones_ip = socket.getaddrinfo(nombre_dominio, None)
        direcciones_sin_duplicados = list(set(direccion[4][0] for direccion in direcciones_ip))
        return direcciones_sin_duplicados
    except socket.gaierror as e:
        print(f"No se pudo obtener la DNS para el dominio {nombre_dominio}. Error: {e}")
        return []

url = input("Ingrese una URL: ")

direcciones_ip = obtener_dns(url)

if direcciones_ip:
    print(f"DNS para {url}:")
    for ip in direcciones_ip:
        print("")
        print(ip)
else:
    print("No se encontraron direcciones IP para la URL.")
