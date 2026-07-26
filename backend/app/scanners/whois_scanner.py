import whois

class WhoisScanner:

    @staticmethod
    def scan(target: str):
        data = whois.whois(target)

        return {
            "domain": data.domain_name,
            "registrar": data.registrar,
            "creation_date": str(data.creation_date),
            "expiration_date": str(data.expiration_date),
            "name_servers": data.name_servers,
        }