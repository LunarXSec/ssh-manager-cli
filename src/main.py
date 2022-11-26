from dataclasses import dataclass
from os import system
from time import sleep
from os.path import exists
import pickle
@dataclass
class ssh_address:
	id: int
	name: str
	address: str
	username: str
	def print_formatted(self):
		print(f"{self.id} : {self.name} : {self.username}@{self.address}")
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
	system("clear")
	for i in addresses:
		i.print_formatted()
	choice = int(input("What would you like to do?\n1 - Add Device\n2 - Connect to Device\n3 - Exit\n"))
	if choice == 1:
		addresses.append(ssh_address(len(addresses), input("What is the name? "), input("What is the ip? "), input("What is the username? ")))
	elif choice == 2:
		usrselected = addresses[int(input("What is the id of the address to use? " ))]
		system(f"ssh {usrselected.username}@{usrselected.address}")
	elif choice == 3:
		with open("ssh-conns.json", 'wb') as f:
			f.write(pickle.dumps(addresses))
		break
	else:
		print("Invalid")
		sleep(3)