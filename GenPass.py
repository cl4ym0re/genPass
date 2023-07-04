import argparse

banner ='''


  ________                __________                         
 /  _____/   ____    ____ \______   \_____     ______  ______
/   \  ___ _/ __ \  /    \ |     ___/\__  \   /  ___/ /  ___/
\    \_\  \\  ___/ |   |  \|    |     / __ \_ \___ \  \___ \ 
 \______  / \___  >|___|  /|____|    (____  //____  >/____  >
        \/      \/      \/                \/      \/      \/ 

'''
print(banner)
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="target name")
args = parser.parse_args()

if not args.name:
    print("Please provide target name with -n or --name option.")
    exit()

special_chars = ['!', '@', '#']
years = [str(year) for year in range(2018, 2024)]

passwords = []
name = args.name.lower()

for char in special_chars:
    for year in years:
        passwords.append(name + char + year)
        passwords.append(name.upper() + char + year)
        passwords.append(name.capitalize() + char + year)
    
    for year in years:
        passwords.append(name + year)
        passwords.append(name.upper() + year)
        passwords.append(name.capitalize() + year)
    
    all_special_chars = ''.join(special_chars)
    for year in years:
        passwords.append(name + all_special_chars + year)
        passwords.append(name.upper() + all_special_chars + year)
        passwords.append(name.capitalize() + all_special_chars + year)

with open("top100.txt") as f:
    top_100 = f.readlines()
    top_100 = [x.strip() for x in top_100]

all_passwords = set(passwords + top_100)

with open("pass.txt", "w") as f:
    for password in all_passwords:
        f.write(password + "\n")
print("[+]saved as pass.txt.")