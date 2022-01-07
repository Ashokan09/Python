from cryptography import fernet
from cryptography.fernet import Fernet
message = "Ashokan"
key = Fernet.generate_key()
print(key)
fernet = Fernet(key)
encmessage = fernet.encrypt(message.encode())
decmessage = fernet.decrypt(encmessage).decode()
print(encmessage, decmessage)


