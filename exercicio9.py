from pymongo.mongo_client import MongoClient


uri = "mongodb://projetoBruno:123@cluster0-shard-00-00.qcgmm.mongodb.net:27017,cluster0-shard-00-01.qcgmm.mongodb.net:27017,cluster0-shard-00-02.qcgmm.mongodb.net:27017/?ssl=true&replicaSet=atlas-d8dhbq-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

meu_banco = client['LISTA4BI']
colecao = meu_banco['TESTE']

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
# Insere a mensagem criptografada na coleção
c = colecao.insert_one({"mensagem": msg_criptografada.decode()})
print(f"Documento inserido com mensagem: {msg_criptografada.decode()}")









#print(colecao.insert_one({"string" : sha_signature}))