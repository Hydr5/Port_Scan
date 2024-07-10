# port_scanner.py

import socket
from concurrent.futures import ThreadPoolExecutor
from common_ports import get_service_name

def check_port(target, port):
    """
    Função auxiliar para verificar se uma porta está aberta.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    s.close()
    return port if result == 0 else None

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    # Resolver o alvo para obter o endereço IP
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        if not target.replace(".", "").isnumeric():
            return "Error: Invalid hostname"
        else:
            return "Error: Invalid IP address"

    # Verificar portas no intervalo fornecido
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: check_port(ip, p), range(port_range[0], port_range[1] + 1))
    
    open_ports = [port for port in results if port is not None]

    if verbose:
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = None

        if hostname:
            output = f"Open ports for {hostname} ({ip})\nPORT     SERVICE\n"
        else:
            output = f"Open ports for {ip}\nPORT     SERVICE\n"

        for port in open_ports:
            service = get_service_name(port)
            output += f"{port:<8} {service}\n"
        return output.strip()
    
    return open_ports

# Testando a função
if __name__ == "__main__":
    print(get_open_ports("209.216.230.240", [440, 445]))
    print(get_open_ports("www.stackoverflow.com", [79, 82], verbose=True))
