import requests
import json

class NetworkReachabilityChecker:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def check_reachability(self):
        try:
            response = requests.get(f'http://{self.ip_address}:80')
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.ConnectionError:
            return False

    def check_ping(self):
        try:
            response = os.system(f'ping -c 1 {self.ip_address}')
            if response == 0:
                return True
            else:
                return False
        except Exception as e:
            return False

    def check_traceroute(self):
        try:
            response = os.system(f'tracepath {self.ip_address}')
            if response == 0:
                return True
            else:
                return False
        except Exception as e:
            return False

def main():
    ip_address = input("Ishlatiladigan IP manzilni kiriting: ")
    checker = NetworkReachabilityChecker(ip_address)
    print("Tarmoq ulanishini tekshirish:")
    print(f"HTTP ulanishi: {checker.check_reachability()}")
    print(f"Ping ulanishi: {checker.check_ping()}")
    print(f"Traceroute ulanishi: {checker.check_traceroute()}")

if __name__ == "__main__":
    import os
    main()
```

Kodda quyidagi funksiyalar mavjud:

- `check_reachability`: HTTP ulanishini tekshiradi.
- `check_ping`: Ping ulanishini tekshiradi.
- `check_traceroute`: Traceroute ulanishini tekshiradi.
- `main`: Asosiy funksiya, IP manzilni so'raydi va ulanishni tekshiradi.

Kodda `requests` kutubxonasidan foydalaniladi, shuningdek, `os` kutubxonasidan `system` funksiyasi foydalaniladi.
