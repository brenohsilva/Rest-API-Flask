from sql_alchemy import database

class TabelaModelo(database.Model):
    __tablename__ = 'valores'

    id_id = database.Column(database.Integer, primary_key=True)
    valor_atual = database.Column(database.Float(precision=2))
    ultimo_ganho = database.Column(database.Float(precision=2))
    ultimo_gasto = database.Column(database.Float(precision=2))
    
    ganho_02 = database.Column(database.Float(precision=2))
    ganho_03 = database.Column(database.Float(precision=2))
    ganho_04 = database.Column(database.Float(precision=2))
    ganho_05 = database.Column(database.Float(precision=2))

    gasto_02 = database.Column(database.Float(precision=2))
    gasto_03 = database.Column(database.Float(precision=2))
    gasto_04 = database.Column(database.Float(precision=2))
    gasto_05 = database.Column(database.Float(precision=2))


    def __init__(self, id_id, valor_atual, ultimo_ganho, ultimo_gasto, ganho_02, ganho_03, ganho_04, ganho_05, gasto_02, gasto_03, gasto_04, gasto_05 ):
        self.id_id = id_id
        self.valor_atual = valor_atual
        self.ultimo_ganho = ultimo_ganho
        self.ultimo_gasto = ultimo_gasto
        self.ganho_02 = ganho_02
        self.ganho_03 = ganho_03
        self.ganho_04 = ganho_04
        self.ganho_05 = ganho_05
        self.gasto_02 = gasto_02
        self.gasto_03 = gasto_03
        self.gasto_04 = gasto_04
        self.gasto_05 = gasto_05


    def json(self):
        return {
            'id_id': self.id_id,
            'valor_atual': self.valor_atual,
            'ultimo_ganho': self.ultimo_ganho,
            'ultimo_gasto': self.ultimo_gasto,
            'ganho_02': self.ganho_02,
            'ganho_03': self.ganho_03,
            'ganho_04': self.ganho_04,
            'ganho_05': self.ganho_05,
            'gasto_02': self.gasto_02,
            'gasto_03': self.gasto_03,
            'gasto_04': self.gasto_04,
            'gasto_05': self.gasto_05
        }
    
    def save_tabela(self):
        database.session.add(self)
        database.session.commit()

    def update(self,valor_atual, ultimo_ganho, ultimo_gasto, ganho_02, ganho_03, ganho_04, ganho_05, gasto_02, gasto_03, gasto_04, gasto_05):
        self.valor_atual = valor_atual
        self.ultimo_ganho = ultimo_ganho
        self.ultimo_gasto = ultimo_gasto
        self.ganho_02 = ganho_02
        self.ganho_03 = ganho_03
        self.ganho_04 = ganho_04
        self.ganho_05 = ganho_05
        self.gasto_02 = gasto_02
        self.gasto_03 = gasto_03
        self.gasto_04 = gasto_04
        self.gasto_05 = gasto_05

    @classmethod
    def find_valores(cls, id_id):
        valores = cls.query.filter_by(id_id=id_id).first() # é igual o select do SQL 
        print(valores)
        if valores:
            return valores
        return None