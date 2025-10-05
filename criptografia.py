import json
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def criptografia_simetrica(mensagem, chave):
    """
    Criptografa uma mensagem usando AES
    """
    # Verifica se a chave tem tamanho válido
    if len(chave) not in [16, 24, 32]:
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes")
    
    # Cria o objeto para criptografia
    cifra = AES.new(chave, AES.MODE_EAX)
    
    # Criptografa a mensagem
    texto_criptografado, tag = cifra.encrypt_and_digest(mensagem.encode('utf-8'))
    
    # Converte para base64 para facilitar armazenamento
    nonce_b64 = base64.b64encode(cifra.nonce).decode('utf-8')
    texto_b64 = base64.b64encode(texto_criptografado).decode('utf-8')
    tag_b64 = base64.b64encode(tag).decode('utf-8')
    
    # Cria um dicionário com os dados
    dados_criptografados = {
        "nonce": nonce_b64,
        "texto_criptografado": texto_b64,
        "tag": tag_b64
    }
    
    # Converte para JSON string
    return json.dumps(dados_criptografados)



def descriptografia_simetrica(dados_json, chave):

    # Verifica se a chave tem tamanho válido
    if len(chave) not in [16, 24, 32]:
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes")
    
    try:
        # Converte JSON string para dicionário
        dados = json.loads(dados_json)
        
        # Converte de base64 para bytes
        nonce = base64.b64decode(dados["nonce"])
        texto_criptografado = base64.b64decode(dados["texto_criptografado"])
        tag = base64.b64decode(dados["tag"])
        
        # Cria o objeto para descriptografia
        cifra = AES.new(chave, AES.MODE_EAX, nonce=nonce)
        
        # Descriptografa e verifica a autenticidade
        texto_original = cifra.decrypt_and_verify(texto_criptografado, tag)
        
        return texto_original.decode('utf-8')
    
    except (ValueError, KeyError):
        raise ValueError("Erro: dados inválidos ou chave incorreta")

