import json
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def criptografia_simetrica(mensagem: str, chave: bytes) -> str:
    

    if len(chave) not in [16, 24, 32]:
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes de comprimento.")
    
    # Cria um objeto AES em modo EAX
    cipher = AES.new(chave, AES.MODE_EAX)
    
    # Criptografa a mensagem e gera a tag de autenticação
    ciphertext, tag = cipher.encrypt_and_digest(mensagem.encode('utf-8'))
    
    # Prepara o payload para ser serializado como JSON
    payload = {
        "nonce": base64.b64encode(cipher.nonce).decode('utf-8'),
        "ciphertext": base64.b64encode(ciphertext).decode('utf-8'),
        "tag": base64.b64encode(tag).decode('utf-8')
    }
    
    return json.dumps(payload)



def descriptografia_simetrica(cifra_criptografado: str, chave: bytes) -> str:
    
    if len(chave) not in [16, 24, 32]:
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes de comprimento.")

    try:
        # Decodifica a string JSON para um dicionário
        payload = json.loads(cifra_criptografado)
        
        # Converte os dados de Base64 para bytes
        nonce = base64.b64decode(payload["nonce"])
        ciphertext = base64.b64decode(payload["ciphertext"])
        tag = base64.b64decode(payload["tag"])

        # Cria um novo objeto AES com os dados
        cipher = AES.new(chave, AES.MODE_EAX, nonce=nonce)
        
        # Descriptografa a mensagem e verifica a autenticidade
        mensagem_original = cipher.decrypt_and_verify(ciphertext, tag)
        
        return mensagem_original.decode('utf-8')

    except (ValueError, KeyError) as e:
        raise ValueError("Erro ao descriptografar: dados inválidos ou chave incorreta.") from e



