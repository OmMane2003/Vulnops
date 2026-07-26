import requests


class HeadersScanner:

    @staticmethod
    def scan(target: str):

        if not target.startswith(("http://", "https://")):
            target = "https://" + target

        response = requests.get(target, timeout=10)

        headers = response.headers

        return {
            "Server": headers.get("Server"),
            "Strict-Transport-Security": headers.get("Strict-Transport-Security"),
            "Content-Security-Policy": headers.get("Content-Security-Policy"),
            "X-Frame-Options": headers.get("X-Frame-Options"),
            "X-Content-Type-Options": headers.get("X-Content-Type-Options"),
            "Referrer-Policy": headers.get("Referrer-Policy"),
            "Permissions-Policy": headers.get("Permissions-Policy"),
        }