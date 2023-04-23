# Importando a biblioteca de criptografia AES da Crypto
from Crypto.Cipher import AES

# Definindo a chave para criptografar e descriptografar dados
key = b'mysecretkey'

# Criando um objeto de criptografia com a chave definida no passo anterior e o modo de operação EAX
cipher = AES.new(key, AES.MODE_EAX)

# Definindo o texto simples que será criptografado
plaintext = b'my secret message'

# Criptografando o texto simples definido anteriormente com a chave e o modo de operação EAX
# A função 'encrypt_and_digest' retorna o texto cifrado e uma tag de autenticação
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# Comentário para fins didáticos: aqui é o lugar onde o texto cifrado e a tag devem ser enviados pela internet

# Criando um novo objeto de criptografia com a mesma chave e o mesmo modo de operação EAX, mas definindo um nonce (número usado apenas uma vez) para decifrar os dados
cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)

# Decifrando o texto cifrado usando a mesma chave, modo de operação EAX e nonce definido anteriormente
# A função 'decrypt' retorna o texto simples original
plaintext = cipher.decrypt(ciphertext)

# Exibindo o texto simples original decifrado
print(plaintext.decode('utf-8'))
