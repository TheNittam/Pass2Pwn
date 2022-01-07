#/!python
#!/usr/bin/python

import time,pathlib,os

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
print("_"*65+"\n")

def main():
	file = pathlib.Path("pwd.lst")
	if file.exists():
		run()
	else:
		CreateConfig()
		run()
	pass

def CreateConfig():
	print (f"Dear {colors.OKGREEN+colors.BOLD+os.getlogin()+colors.ENDC},\n\n\tThe password pattern list {colors.OKGREEN+colors.BOLD}(Pwd.lst){colors.ENDC} is missing,\n\tbut don't worry, I'll make one specifically for you.\n\nRegards,\nYour {colors.OKBLUE+colors.BOLD}@TheNittam{colors.ENDC}")
	f = open("pwd.lst", "a")
	f.write("{}123\n{}@123\n{}1234\n{}654\n{}456\n{}789\n{}963")
	f.close()
	print("_"*65+"\n")

def run():
	with open('pwd.lst') as formatlst:
		word = input("Word/s : ").lower().split(" ")

		if len(word)==1:
			print(f"Input Type \"{colors.OKGREEN+colors.BOLD}Word{colors.ENDC}\"")
			word = word[0]
		else:
			print(f"Input Type \"{colors.OKGREEN+colors.BOLD}Sentence{colors.ENDC}\"")
			word = [w[0] for w in word]
			word = "".join(word)
		
		defaultlst = word.replace("\\", "_").replace("/", "_") 
		pwdlst = input(f"Save as [\"{colors.OKGREEN+colors.BOLD+defaultlst}.txt{colors.ENDC}\"] : ") or defaultlst

		print("_"*65)
		print(f"\nCreating a List of Common Passwords({colors.OKGREEN+colors.BOLD}"+pwdlst+f".txt{colors.ENDC})")
		print("_"*65+"\n")

		for x in formatlst:
			x = x.rstrip('\n').format(word)
			print(x+"\n"+x.upper()+"\n"+x.capitalize()+"\n")
			f = open(pwdlst+"_"+time.strftime("%Y%m%d_%H%M%S")+".txt", "a")
			f.write(x+"\n"+x.upper()+"\n"+x.capitalize()+"\n")
			f.close()
	print("_"*65+f"\n\n\tWorking with you has been a true blessing...{colors.OKGREEN+colors.BOLD+os.getlogin()+colors.ENDC}")
	print("_"*65+"\n")

if __name__ == "__main__":
	main()
