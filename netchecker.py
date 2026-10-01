import os
import time

print("GHOST Net Checker Starting...\n")
time.sleep(1)

# Google ko ping kar rahe hain
result = os.system("ping -c 1 google.com > /dev/null")

if result == 0:
    print("[✓] Internet Connected - Sab Ok Hai!")
    print("[✓] Google is Working!")
else:
    print("[X] Internet Down Hai!")
    print("[X] Connection Check Karo!")
