# common_ports.py

common_ports = {
    20: 'ftp',
    21: 'ftp',
    22: 'ssh',
    23: 'telnet',
    25: 'smtp',
    53: 'dns',
    80: 'http',
    110: 'pop3',
    115: 'sftp',
    143: 'imap',
    194: 'irc',
    443: 'https',
    465: 'smtps',
    993: 'imaps',
    995: 'pop3s',
    3306: 'mysql',
    3389: 'ms-wbt-server',
    5900: 'vnc',
    8080: 'http-proxy',
    # adicione mais portas conforme necessário
}

def get_service_name(port):
    """
    Função auxiliar para obter o nome do serviço de uma porta.
    """
    return common_ports.get(port, "Unknown")
