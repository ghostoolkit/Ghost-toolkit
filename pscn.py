import socket
print ("\nGHOST port scanner\n ")

target = input ("target IP / website (e.g scame.nmap.org):")
print (f"\nscanning {target} ...\n")


for port in range(20, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print (f"[OPEN] port {port} is open ")
    s.close()
print ("\nScanning khatam !")
