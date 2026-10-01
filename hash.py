
import hashlib


print ("\nGHOST Hash Cracker - Lab ")
hash_input = input("MD5 hash likho !").strip()


wordlist = ["123456", "password", "admin", "admin123", "letmein", "ghost123"]

print (f"\nCracking {hash_input} ...\n")

found = False
for word in wordlist:
    word_hash = hashlib.md5(word.encode()).hexdigest()
    print (f"trying {word} -> {word_hash}")
    if word_hash == hash_input:
        print (f"\n[FOUND] Password mil gaya: {word}")
        found = True
        break

if not found:
    print(f"\n[NOT FOUND] ") 
