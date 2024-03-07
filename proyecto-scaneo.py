import os
import sys
import paramiko
import requests

def discover_targets(network_range):
    """Discover targets based on the given network range."""
    # Lista para almacenar las direcciones IP vulnerables
    vulnerable_targets = []
    # Recorremos las direcciones IP en el rango de red dado
    for ip in range(int(network_range.split(".")[0]), int(network_range.split(".")[0]) + 1):
        # Construimos la dirección IP completa
        ip_address = f"{ip}.{network_range.split('.')[1]}.{network_range.split('.')[2]}.{network_range.split('.')[3]}"
        try:
            # Intentamos establecer una conexión SSH con la dirección IP
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip_address, timeout=5, look_for_keys=False)
            ssh.close()
            # Imprimimos que la dirección IP no es un servidor FTP abierto
            print(f"{ip_address} is not an open FTP server.")
        except (paramiko.ssh_exception.SSHException, requests.exceptions.ConnectionError):
            # Si no se puede conectar, la dirección IP se considera vulnerable
            vulnerable_targets.append(ip_address)
            # Imprimimos que la dirección IP es un servidor FTP abierto
            print(f"{ip_address} is an open FTP server.")

    return vulnerable_targets

def find_files_with_extension(directory, extension):
    """Find all files with a specific extension in a given directory."""
    results = []
    # Recorremos todos los archivos en el directorio dado
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Si el archivo tiene la extensión especificada, lo agregamos a los resultados
            if file.endswith(extension):
                results.append(os.path.join(root, file))
    return results

def check_http_response(url):
    """Check the HTTP response code for a given URL."""
    try:
        # Realizamos una solicitud HTTP GET a la URL dada
        response = requests.get(url, timeout=5)
        # Devolvemos el código de respuesta HTTP
        return response.status_code
    except requests.exceptions.RequestException:
        # Si hay un error en la solicitud, devolvemos None
        return None

def report_data(vulnerable_targets):
    """Generate a report with the findings."""
    # Nombre del archivo de informe
    report_file = "open_ftp_servers_report.txt"
    # Escribimos las direcciones IP vulnerables en el archivo de informe
    with open(report_file, "w") as f:
        for target in vulnerable_targets:
            f.write(f"{target}\n")
    # Imprimimos la ubicación del archivo de informe
    print(f"Open FTP servers report saved to {report_file}")

if __name__ == "__main__":
    # Verificamos si se proporcionan los argumentos necesarios
    if len(sys.argv) != 3:
        print("Usage: python ftp_scanner.py <network_range> <extension> (e.g., 192.168.1.0/24 .txt)")
        sys.exit(1)

    network_range = sys.argv[1]
    extension = sys.argv[2]
    # Descubrimos las direcciones IP vulnerables en el rango de red dado
    vulnerable_targets = discover_targets(network_range)
    # Buscamos archivos con la extensión especificada en el directorio actual
    file_results = find_files_with_extension(".", extension)
    # Generamos un informe con las direcciones IP vulnerables encontradas
    report_data(vulnerable_targets)
    # Imprimimos los archivos encontrados con la extensión especificada
    print(f"Files with extension '{extension}' in the current directory: {file_results}")
    # Verificamos la respuesta HTTP para una URL específica
    url = "http://example.com"
    http_response_code = check_http_response(url)
    # Imprimimos el código de respuesta HTTP
    print(f"HTTP response code for {url}: {http_response_code}")
