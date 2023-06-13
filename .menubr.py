#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import subprocess
import os
import time
from urllib.parse import urlparse        

def mostrar_menu():
    
    color_reset = "\033[0m"  # Restablecer el color
    # Colores básicos
    color_azul = "\033[94m"
    color_verde = "\033[92m"
    color_amarillo = "\033[33m"
    color_magenta = "\033[35m"
    color_cyan = "\033[36m"
    color_rojo = "\033[91m"
    color_reset = "\033[0m"
    
    print(color_amarillo + "Dev: @RealStrategy" + color_reset)
    print(color_verde + "               _   _              _                         ")
    print("              | | | |            | |                        ")
    print("              | |_| |  ___   ___ | |_                       ")
    print("              |  _  | / _ \ / __|| __|                      ")
    print("              | | | || (_) |\__ \| |_                       ")
    print("              \_| |_/ \___/ |___/ \__|                      ")
    print("_____        _                       _                      ")
    print("|  ___|      | |                     | |                    ")
    print("| |__  __  __| |_  _ __   __ _   ___ | |_   ___   _ __      ")
    print("|  __| \ \/ /| __|| '__| / _` | / __|| __| / _ \ | '__|     ")
    print("| |___  >  < | |_ | |   | (_| || (__ | |_ | (_) || |        ")
    print("\____/ /_/\_\ \__||_|    \__,_| \___| \__| \___/ |_|        ")
    print("                                                            ")
    print(color_verde + "V= 3.0                        I R P A R P A Y A Ñ A      " + color_reset)
    print("")
    print(color_cyan + "1. Extrator de host ")
    print("2. Extrator de Subdominio ")
    print("3. Extrator de Domínio DNS ")
    print("4. Verifique o status do host ")
    print("5. Gerador de carga util Pro ")
    print("6. Veja as portas abertas ")
    print("7. Geolocalizacao por IP")
    print("8. Mais informacoes e creditos")
    print("9. Mude o idioma do script ")
    print("0. Salir" + color_reset)
    print("")


def extraer_links():
    url = input("\033[1;32mInsira o host: ")
    if not url.startswith("http"):
        url = "http://" + url

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        href_regex = re.compile(r'href=[\'|"](.*?)[\'"]')
        href_matches = re.findall(href_regex, response.text)
        unique_urls = set()

        for href in href_matches:
            if href.startswith("http"):
                unique_urls.add(href)
            elif href.startswith("/"):
                unique_urls.add(url + href)
            else:
                unique_urls.add(url + "/" + href)

        sorted_urls = sorted(unique_urls)
        for url in sorted_urls:
            print(url)

        guardar_archivo(sorted_urls)
    else:
        print("Erro ao acessar a URL.")


def guardar_archivo(urls):
    archivo = "hosts.txt"
    with open(archivo, 'w') as file:
        for url in urls:
            file.write(url + '\n')
            
    print("")
    print("Os resultados foram salvos no arquivo:", archivo)
    print("Voce pode editar o arquivo de texto para adicionar outros URLs e exibir status.")
    print("")


def extract_urls(text):
    url_regex = r"https?://[^\s/$.?#].[^\s]*"
    return re.findall(url_regex, text)

def extract_internal_subdomains(url, urls):
    base_domain = urlparse(url).netloc
    internal_subdomains = set()

    for u in urls:
        netloc = urlparse(u).netloc
        if netloc.endswith(base_domain) and not netloc == base_domain:
            internal_subdomains.add(netloc)

    return internal_subdomains

def extract_external_subdomains(url, urls):
    base_domain = urlparse(url).netloc
    external_subdomains = set()

    for u in urls:
        netloc = urlparse(u).netloc
        if not netloc.endswith(base_domain):
            external_subdomains.add(netloc)

    return external_subdomains

def extraer_subdominios():
    url = input("\033[32mDigite o URL completo: ")
    print("")
    response = requests.get(url)
    html_content = response.text

    urls = extract_urls(html_content)

    internal_subdomains = extract_internal_subdomains(url, urls)
    external_subdomains = extract_external_subdomains(url, urls)
    
    print("\033[31mURLs encontrados:")
    print("")
    for u in urls:
        print("\033[32m", u)

    print("\033[31mSUBDOMINIOS INTERNOS:")
    print("")
    for subdomain in internal_subdomains:
        print("\033[32m", subdomain)
        
    print("\033[31mSUBDOMINIOS EXTERNOS:")
    print("")
    for subdomain in external_subdomains:
        print("\033[32m", subdomain)

    else:
        print("Erro ao acessar a URL.")


def generar_payload():   
    time.sleep(1)
    os.system("python3 .payloadbr.py")      

def verificar_estado_hosts():
    archivo = "hosts.txt"
    try:
        with open(archivo, 'r') as file:
            urls = file.readlines()
            urls = [url.strip() for url in urls]

        for url in urls:
            response = requests.head(url, verify=False)
            print(response.status_code, url)

    except FileNotFoundError:
        print("O arquivo", archivo, "nao existe.")

    except Exception as e:
        print("Falha ao verificar o status dos hosts:", str(e))
        print("")


def ver_puertos_abiertos():
    host = input("\033[32mDigite a URL ou IP: ")
    print("")
    print("Verificando portas abertas... Isso pode levar tempo!")
    print("")
    try:
        resultado = subprocess.check_output(["nmap", "-p-", host])
        print("")
        print(resultado.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o comando nmap:", str(e))


def trace_ip_address(ip):
    response = requests.get(f"http://ipinfo.io/{ip}")
    data = response.json()
    return data

def change_language():
    print("\033[32m")
    print("1. English")
    print("2. Portuguese")
    print("3. Russian")
    print("4. Hindi")
    print("5. Spanish")
    print("0. Go back to main menu")
    print("")
    try:
        option = int(input("\033[31mSelect an option: "))
        if option == 1:
            # Set language to English
            print("\033[32mLanguage changed to English.")
            time.sleep(1)
            os.system("python3 .menuen.py")
        elif option == 2:
            # Set language to Portuguese
            print("\033[32mIdioma alterado para Português.")
            time.sleep(1)
            os.system("python3 .menubr.py")
        elif option == 3:
            # Set language to Russian
            print("\033[32mЯзык изменен на Русский.")
            time.sleep(1)
            print("\033[1;32mNot available")
        elif option == 4:
            # Set language to Hindi
            print("\033[32mभाषा हिंदी में बदल गई।")
            time.sleep(1)
            print("\033[1;32mNot available")
        elif option == 5:
            # Set language to Spanish
            print("\033[32mIdioma cambiado a Español.")
            time.sleep(1)
            os.system("python3 menu.py")
        elif option == 0:
            # Go back to main menu
            return
        else:
            print("Invalid option.")
    except ValueError:
        print("Invalid option.")

    input("\nPress Enter to continue...")
    change_language()

def ejecutar_opcion(opcion):
    if opcion == 1:
        print("\033[1;32m")
        extraer_links()
    elif opcion == 2:
        print("")
        extraer_subdominios()
    elif opcion == 3:
        print("")
        os.system("python3 .dnsbr.py")
    elif opcion == 4:
        print("\033[32m")
        verificar_estado_hosts()
    elif opcion == 5:
        print("")
        generar_payload()
    elif opcion == 6:
        print("")
        ver_puertos_abiertos()
    elif opcion == 7:
        ip = input("\033[1;32mDigite o endereco IP: ")
        print("")
        ip_data = trace_ip_address(ip)
        print(f"nome de anfitriao: {ip_data.get('hostname', '')}")
        print(f"Organizacao: {ip_data.get('org', '')}")
        print(f"Localizacao: {ip_data.get('city', '')}, {ip_data.get('region', '')}, {ip_data.get('country', '')}")
        print(f"Direcao IP: {ip_data['ip']}")
        print(f"Codigo Postal: {ip_data.get('postal', '')}")
        print(f"Coordenadas: {ip_data.get('loc', '')}")
        print(f"Provedor de internet: {ip_data.get('isp', '')}")
        print(f"Fuso horario: {ip_data.get('timezone', '')}")
        print("")
        print(f"\033[1;36mLink de geolocalizacao: https://www.google.com/maps/place/{ip_data.get('loc', '')}")
    elif opcion == 8:
        time.sleep(1)
        #Cambiar cat por type para windows
        print("\033[1;32m")
        os.system("cat READMEBR.MD") 
        
    elif opcion == 9:
        print("\033[31m")
        change_language()
        print("")
        
    elif opcion == 0:
        print("\033[32m")
        print("Obrigado por usar o Host-Extractor! Volta em breve.")
        print("")
        return False
    else:
        print("Opcao invalida.")

    input("\nPressione Enter para continuar...")
    return True


continuar = True
while continuar:
    os.system("clear")
    mostrar_menu()
    try:
        opcion = int(input("\033[31mDigite uma opcao em numero: "))
        continuar = ejecutar_opcion(opcion)
    except ValueError:
        print("Opcao invalida. Tente novamente de outra maneira.")
        input("\nPressione Enter para continuar...")
