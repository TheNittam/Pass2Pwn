#/!python
#!/usr/bin/python
#import time,pathlib,os
import os
import itertools

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f'''{colors.BOLD+colors.OKGREEN}
         ____               ____  ____
        |  _ \\ __ _ ___ ___|___ \\|  _ \\__      ___ __
        | |_) / _` / __/ __| __) | |_) \\ \\ /\\ / / '_ \\
        |  __/ (_| \\__ \\__ \\/ __/|  __/ \\ V  V /| | | |
        |_|   \\__,_|___/___/_____|_|     \\_/\\_/ |_| |_| v1.1

\t\tCoded By #Nittam | @TheNittam
\t\t   https://nirmaldahal.com.np
{colors.ENDC}''')
def generate_passwords(word):
    """
    Generate common passwords based on a given word.
    """
    variations = set(itertools.product(*zip(word.upper(), word.lower())))
    passwords = [''.join(variation) for variation in variations]
    passwords.append(word)
    passwords.append(word.capitalize())
    passwords.append(word.upper())
    passwords.append(word.lower())
    passwords.append(word[::-1])
    return passwords

def save_passwords(passwords, filename):
    """
    Save a list of passwords to a file.
    """
    with open(filename+".txt", 'w') as file:
        for password in passwords:
            file.write(password + '\n')
    print(f"\n\n\tPassword list saved to {filename}.txt\n")

def main():
    """
    Main function.
    """
    word = input("Enter a word to generate common passwords: ")
    filename = input(f"Save as [\"{colors.OKGREEN+colors.BOLD+word}.txt{colors.ENDC}\"] : ")  or word
    passwords = generate_passwords(word)
    print("_"*65)
    print(f"\nCreating a List of Common Passwords({colors.OKGREEN+colors.BOLD}"+filename+".txt{colors.ENDC})")
    print("_"*65+"\n")
    save_passwords(passwords, filename)
    print("_"*65+f"\n\n\tWorking with you has been a true blessing...{os.environ['USER']}")
if __name__ == '__main__':
    main()
