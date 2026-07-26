import nmap


class NmapScanner:

    @staticmethod
    def scan(target: str):
        scanner = nmap.PortScanner()

        scanner.scan(hosts=target, arguments="-F")

        result = {}

        host = scanner.all_hosts()[0]

        result["host"] = host
        result["hostname"] = target
        result["state"] = scanner[host].state()

        result["protocols"] = {}

        for proto in scanner[host].all_protocols():
            result["protocols"][proto] = []

            for port in scanner[host][proto]:
                result["protocols"][proto].append({
                    "port": port,
                    "state": scanner[host][proto][port]["state"]
                })

        return result