import socket
# Dns en ingles
def obtener_dns(nombre_dominio):
    try:
        direcciones_ip = socket.getaddrinfo(nombre_dominio, None)
        direcciones_sin_duplicados = list(set(direccion[4][0] for direccion in direcciones_ip))
        return direcciones_sin_duplicados
    except socket.gaierror as e:
        print(f"Could not get DNS for domain {nombre_dominio}. Mistake: {e}")
        return []

url = input("Enter a URL:")

direcciones_ip = obtener_dns(url)

if direcciones_ip:
    print(f"DNS for {url}:")
    for ip in direcciones_ip:
        print("")
        print(ip)
else:
    print("No IP addresses found for the URL.")
