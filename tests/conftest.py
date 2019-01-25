# import os
# import tempfile
# import pytest

# from app import create_app
# from app.db import get_db, init_db

# # Abrindo o arquivo SQL para popular o banco
# with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
#     _data_sql = f.read().decode('utf-8')


# @pytest.fixture
# def app():
#     """
#         Cria uma instancia do app,
#         Com o intuito de reutilizar
#     """
#     # Isolando o db para realizar os testes
#     db_fd, db_path = tempfile.mkstemp()
#     # Criando o app
#     app = create_app({
#         'TESTING': True,
#         'DATABASE': db_path
#     })

#     # Criando o db e carregando os dados do SQL
#     with app.app_context():
#         init_db()
#         get_db().executescript(_data_sql)

#     # Generator do app
#     yield app

#     # Fechando e removendo o banco temporário
#     os.close(db_fd)
#     os.unlink(db_path)
