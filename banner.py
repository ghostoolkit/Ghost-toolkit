import socket
print ("\nGHOST Banner Grabber\n")

target = input ("website likho (e.g google.com):")
port = 80

try:
    s = socket.socket()
    s.settimeout(2)
    s.connect((target, port))
    s.send(b"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n")
    banner = s.recv(1024)
    print ("\n--- server info ---\n")
    print(banner.decode())
    s.close()
except:
    print ("\n[X] Connect nhi hosakta ! ")
