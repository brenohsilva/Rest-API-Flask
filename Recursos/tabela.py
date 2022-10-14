from flask_restful import Resource, reqparse
from Modelos.tabela import TabelaModelo
import sqlite3

class Tabela(Resource):

    valores = reqparse.RequestParser()
    valores.add_argument('valor_atual', type=str, required=True)
    valores.add_argument('ultimo_ganho', type=float, required=True)
    valores.add_argument('ultimo_gasto', type=float, required=True)
    
    valores.add_argument('ganho_02', type=float, required=True)
    valores.add_argument('ganho_03', type=float, required=True)
    valores.add_argument('ganho_04', type=float, required=True)
    valores.add_argument('ganho_05', type=float, required=True)

    valores.add_argument('gasto_02', type=float, required=True)
    valores.add_argument('gasto_03', type=float, required=True)
    valores.add_argument('gasto_04', type=float, required=True)
    valores.add_argument('gasto_05', type=float, required=True)


    def get(self, id_id):
        resposta_valores = TabelaModelo.find_valores(id_id)
        return resposta_valores.json()

    def post(self, id_id):
        dados = Tabela.valores.parse_args()
        objeto_tabela = TabelaModelo(id_id, **dados)
        objeto_tabela.save_tabela()
        return objeto_tabela.json()


    def put(self, id_id):
        dados = Tabela.valores.parse_args()

        objeto_tabela = TabelaModelo.find_valores(id_id)
        objeto_tabela.update(**dados)
        objeto_tabela.save_tabela()
        return objeto_tabela.json()
        