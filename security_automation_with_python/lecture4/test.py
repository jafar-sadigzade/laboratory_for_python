# The first install nmap to device
# The second install python-namp using pip
import nmap

# Initialize Nmap PortScanner
nm = nmap.PortScanner()

# Scan a specific IP and port range
target = '192.168.1.1'
nm.scan(target, '22-443')
print(f"Scan report for {target}")

# Print scan results
for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    for protocol in nm[host].all_protocols():
        ports = nm[host][protocol].keys()
        print(f"Protocol: {protocol}")
        for port in ports:
            print(f"Port: {port}, State: {nm[host][protocol][port]['state']}")
