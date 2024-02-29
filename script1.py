import nmap

def perform_ping_scan(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sn')

    # Extracting the results
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    return hosts_list

if __name__ == "__main__":
    target_ip = input("Enter the target IP address or range: ")
    results = perform_ping_scan(target_ip)

    print("\nScan results:")
    for host, status in results:
        print(f"Host: {host} is {status}")