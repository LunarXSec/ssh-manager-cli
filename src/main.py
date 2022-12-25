from dataclasses import dataclass
from os import system
from time import sleep
from os.path import exists
import platform
curos = platform.platform()
import hashlib
import requests
import pickle
@dataclass
class ssh_address:
	id: int
	name: str
	address: str
	username: str
	def print_formatted(self):
		print(f"{self.id} : {self.name} : {self.username}@{self.address}")
def hash_file(filename):
   h = hashlib.sha512()

   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()
with open("new.py", "w") as f:
	f.write(requests.get("https://raw.githubusercontent.com/Quinn6182/ssh-manager-cli/main/src/main.py").content.decode('utf-8'))
new = hash_file("new.py")
old = hash_file("main.py")
if new == old:
	print("No updates!")
	sleep(2)
	if curos == 'Windows-10-10.0.22621-SP0':
		system("del new.py")
	else:
		system("rm new.py")
else:
	print("Update Available!")
	print("Updating")
	sleep(3)
	print("Bootstrapping New Version")
	system("rm main.py")
	if curos == 'Windows-10-10.0.22621-SP0':
		system("rename new.py main.py")
	else:
		system("mv new.py main.py")
if exists('ssh-conns.json'):
	try:
		with open('ssh-conns.json', 'rb') as f:
			addresses = pickle.loads(f.read())
	except EOFError:
		addresses = []
		pass
else:
	addresses = []
	open('ssh-conns.json', 'w').close()
if isinstance(addresses, str):
	addresses = []
while True:
	if curos == 'Windows-10-10.0.22621-SP0':
		system("cls")
	else:
		system("clear")
	for i in addresses:
		i.print_formatted()
	choice = int(input("What would you like to do?\n1 - Add Device\n2 - Connect to Device\n3 - Exit\n4 - Delete (W.I.P)"))
	if choice == 1:
		addresses.append(ssh_address(len(addresses), input("What is the name? "), input("What is the ip? "), input("What is the username? ")))
	elif choice == 2:
		usrselected = addresses[int(input("What is the id of the address to use? " ))]
		system(f"ssh {usrselected.username}@{usrselected.address}")
	elif choice == 3:
		with open("ssh-conns.json", 'wb') as f:
			f.write(pickle.dumps(addresses))
		break
	elif choice == 4:
		id_to_remove = int(input("Which one to remove?"))
		del addresses[id_to_remove]
	else:
		print("Invalid")
		sleep(3)
