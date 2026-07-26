import nmap

scanner = nmap.PortScanner()


def run_scan(target):

    scanner.scan(target)

    return scanner.csv()