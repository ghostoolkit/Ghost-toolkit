import socket, hashlib 

def port_scanner():
    target = input("target IP (127.0.0.1): ") or "127.0.0.1"
    for port in [21, 22, 80, 443, 8080]:
        s=socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((target, port))==0:
            print (f"[OPEN] {port}")
        else:
            print (f"[CLOSED] {port}")
        s.close()

def hash_tool():
    text=input("text lilho !\n")
    h=hashlib.md5(text.encode()).hexdigest()
    print (f"MD5: {h}")

while True:
    print ("\n===GHOST TOOLKIT v1 (Loop Mood)===")
    print ("1. Port Scanner")
    print ("2. Hash Generator")
    print ("3. Enter exit for out")
    c=input("Choice (1/2 exit): ").lower()
    if c=="exit" or c=="3":
        print ("\nToolkit band ho rha hi")
        break
    elif c=="1":
        port_scanner()
    elif c=="2":
        hash_tool()
    else:
        print ("Wrong Choice !")
