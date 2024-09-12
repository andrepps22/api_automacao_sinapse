from passlib.context import CryptContext


CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
        Função para verificar se a senha esta correta, comparando
        a senha em texto puro, informado pelo usuario
    """

    return CRIPTO.verify(senha, hash_senha)



def gerar_hash(senha: str) -> str:
    """
        Função que retorna o hash da senha
    """
    return CRIPTO.hash(senha)