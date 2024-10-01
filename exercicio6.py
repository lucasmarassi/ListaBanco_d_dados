from pymongo.mongo_client import MongoClient
import hashlib

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

# Texto a ser criptografado
texto = input("Digite uma senha: ")

# Gera os hashes
sha_signature_md5 = hashlib.md5(texto.encode()).hexdigest()
sha_signature = hashlib.sha256(texto.encode()).hexdigest()
sha_signature_1 = hashlib.sha1(texto.encode()).hexdigest()

# Exibe o texto original e os hashes gerados
print(f"Texto original: {texto}")
print(f"Hash MD5: {sha_signature_md5}")
print(f"Hash SHA-1: {sha_signature_1}")
print(f"Hash SHA-256: {sha_signature}")

# Comparar os hashes
print("\nComparação de hashes:")
if sha_signature_md5 == sha_signature:
    print("MD5 e SHA-256 são iguais.")
else:
    print("MD5 e SHA-256 são diferentes.")

if sha_signature_md5 == sha_signature_1:
    print("MD5 e SHA-1 são iguais.")
else:
    print("MD5 e SHA-1 são diferentes.")

if sha_signature == sha_signature_1:
    print("SHA-256 e SHA-1 são iguais.")
else:
    print("SHA-256 e SHA-1 são diferentes.")

# Insere o hash MD5 na coleção
c = colecao.insert_one({"string": sha_signature_md5})
print(f"Documento inserido com string: { sha_signature_md5}")








#print(colecao.insert_one({"string" : sha_signature}))