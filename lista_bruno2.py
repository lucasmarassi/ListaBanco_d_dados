import hashlib

# Texto a ser criptografado
texto1 = input("Digite uma senha: ")
texto2 = input("Digite uma senha: ")

# Cria um objeto sha256 e gera o hash
sha_signature1 = hashlib.sha256(texto1.encode()).hexdigest()

# Cria um objeto sha256 e gera o hash
sha_signature2 = hashlib.sha256(texto2.encode()).hexdigest()

if (sha_signature2 == sha_signature1):
    print("Assinaturas iguais")
else:
    print("Assinatura diferentes")  