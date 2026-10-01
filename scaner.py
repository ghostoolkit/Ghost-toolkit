import socket


print ("\nGHOST Port Scannet-LAB")

target = input("\nIP likho (default 127.0.0.1): ") or "127.0.0.1"
print (f"\nScanning {target}...\n")

ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)   #1 second wait
    result = s.connect_ex((target, port))
    if result == 0:
        print (f"OPEN port {port} is open")
    else:
        print (f"CLOSED port {port} close hi")
    s.close()
print ("OK scan khatam ")
