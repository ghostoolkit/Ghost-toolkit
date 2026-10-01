import requests
print ("\nGHOST Admin Finder\n")

site = input("website likho (e.g example.com):")

if not site.startswith("https"):
    site = "https://" + site

paths = ["admin", "admin/login", "administrator", "login", "wp-admin", "admin.php", "cpa>"]
print (f"\nScanning {site} ...\n")

for path in paths:
    url = site + "/" + path
    try:
        r = requests.get(url, timeout=2)
        if r.status_code == 200:
            print (f"[FOUND] {url}")
        else:
            print (f"[NOT] {url}")
    except:
        print ("[OK]")
