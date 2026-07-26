import dns.resolver


class DNSScanner:

    @staticmethod
    def scan(target: str):
        result = {}

        records = ["A", "AAAA", "MX", "NS", "TXT"]

        for record in records:
            try:
                answers = dns.resolver.resolve(target, record)

                if record == "MX":
                    result[record] = [
                        str(r.exchange) for r in answers
                    ]
                else:
                    result[record] = [
                        str(r) for r in answers
                    ]

            except Exception:
                result[record] = []

        return result