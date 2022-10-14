from flask import Flask, jsonify
from flask_restful import Api
from Recursos.tabela import Tabela


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def banco_cria():
    database.create_all()


api.add_resource(Tabela, '/valores/<int:id_id>')



if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
