from sqlalchemy import create_engine
from core.config import Setting

engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/orcamento', echo=True)

# Função síncrona para criar as tabelas
def criar_tabelas():
    import models.__all_models
    # Cria as tabelas no banco de dados
    # Setting.DBModelReg.metadata.drop_all(engine)
    Setting.DBModelReg.metadata.create_all(engine)

# Executa a função de criação de tabelas
if __name__ == "__main__":
    criar_tabelas()