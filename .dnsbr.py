import socket
#Extractor dns portugues
def obtener_dns(nombre_dominio):
    try:
        direcciones_ip = socket.getaddrinfo(nombre_dominio, None)
        direcciones_sin_duplicados = list(set(direccion[4][0] for direccion in direcciones_ip))
        return direcciones_sin_duplicados
    except socket.gaierror as e:
        print(f"Nao foi possivel obter DNS para o dominio {nombre_dominio}. Erro: {e}")
        return []

url = input("Digite um URL: ")

direcciones_ip = obtener_dns(url)

if direcciones_ip:
    print(f"DNS para {url}:")
    for ip in direcciones_ip:
        print("")
        print(ip)
else:
    print("Nenhum endereco IP encontrado para o URL.")
