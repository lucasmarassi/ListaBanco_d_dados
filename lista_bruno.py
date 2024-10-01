import hashlib
# Texto a ser criptografado
texto = input("Digite uma senha: ")
# Cria um objeto sha256 e gera o hash
sha_signature = hashlib.sha256(texto.encode()).hexdigest()
# Exibe o texto original e o hash gerado
print(f"Texto original: {texto}")
print(f"Hash SHA-256: {sha_signature}")