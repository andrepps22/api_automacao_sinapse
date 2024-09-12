from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()




def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
        Função para verificar se a senha esta correta, comparando
        a senha em texto puro, informado pelo usuario
    """

    return pwd_context.verify(senha, hash_senha)



def gerar_hash(senha: str) -> str:
    """
        Função que retorna o hash da senha
    """
    return pwd_context.hash(senha)

