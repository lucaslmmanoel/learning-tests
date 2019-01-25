import os

from flask import Flask, render_template


def create_app(test_config=None):
    """
        Criando e Configurando o app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )
    if test_config is None:
        # Declarando a instancia de configuração
        # Caso não esteja em teste
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Caso esteja em teste
        app.config.from_mapping(test_config)

    # Lançando uma exceção caso o arquivo não exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Uma simples tela
    @app.route('/')
    def index():
        return render_template('index.html')

    # Uma simples tela
    @app.route('/hello')
    def hello():
        return hello

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
