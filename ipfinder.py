import socket

print("\nGHOST IP finder\n")

site = input("Website likho (e.g. google.com): ")

try:
    ip = socket.gethostbyname(site)
    print(f"\n[OK] {site} ka IP hai {ip}")
except:
    print("\n[X] Galat website name hai")
