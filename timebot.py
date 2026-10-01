import time
from datetime import datetime

print("GHOST Time Bot Started...\n")

for i in range(5):
    t = datetime.now().strftime("%H:%M:%S")
    print(f"[{i+1}] Time: {t}")
    time.sleep(2)

print("\nBot Khatam!")

