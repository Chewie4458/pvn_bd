"""excluir"""

import sqlite3
from banco import criacao_banco

criacao_banco()

con = sqlite3.connect('pvn_banco.bd')

c = con.cursor()

c.execute('''''')

'''
for linha in c.fetchall():
    print(linha)
'''

con.commit()


"""
saidas

controle medicamentos -> SELECT a.nome, m.nome, m.especificacoes, c.qtd_dose, c.frequencia, c.inicio_tratamento, 
    c.termino_tratamento, c.obs FROM acolhidos as a JOIN controle_medicamentos as c ON a.id_acolhido = c.id_acolhido
    JOIN medicamentos as m on c.id_medicamento = m.id_medicamento;

entrada -> SELECT m.nome, m.especificacoes, m.obs, e.qtd_entrada, e.data_entrada, e.obs FROM medicamentos as m
    JOIN entradas_medicamentos as e ON m.id_medicamento = e.id_medicamento;

"""