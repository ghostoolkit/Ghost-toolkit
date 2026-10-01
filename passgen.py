import random
import string
import time

print("GHOST Password Generator\n")

name = input("Kitne letters ka password chahiye? (e.g 12): ")

length = int(name)

chars = string.ascii_letters + string.digits + "!@#$%&*"
password = ""

for i in range(length):
    password += random.choice(chars)

print("\nGenerating...")
time.sleep(1)
print(f"\n[✓] Your Strong Password: {password}")
