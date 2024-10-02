from cryptography.fernet import Fernet

# Gerando uma chave secreta
chave = Fernet.generate_key()
fernet = Fernet(chave)

# Criptografando dados
mensagem = input("Digite mensagem para ser criptografada: ")
msg_criptografada = fernet.encrypt(mensagem.encode())
print("Mensagem criptografada com Fernet: " + msg_criptografada.decode())

# Para descriptografar a mensagem (opcional)
msg_descriptografada = fernet.decrypt(msg_criptografada).decode()
print("Mensagem descriptografada: " + msg_descriptografada)