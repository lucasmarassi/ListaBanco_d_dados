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



import hashlib
meu_banco = client['LISTA4BI']
colecao = meu_banco['TESTE']
# Texto a ser criptografado
texto = input("Digite uma senha: ")
# Cria um objeto sha256 e gera o hash
sha_signature = hashlib.md5(texto.encode()).hexdigest()
# Exibe o texto original e o hash gerado
print(f"Texto original: {texto}")
print(f"Hash SHA-256: {sha_signature}")
c = colecao.insert_one({"string" : sha_signature})
print(c)

for itens in colecao.find():
    print(itens)
    if itens["string"] == sha_signature:  # Correção aqui
        print("Os hashes são iguais!")
        break






#print(colecao.insert_one({"string" : sha_signature}))