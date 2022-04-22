import sqlite3


def criacao_banco():
    # conecta com o banco de dados ou cria ele se não existe
    con = sqlite3.connect('pvn_banco.bd')

    c = con.cursor()

    # cria tabela acolhidos se já não foi criada
    c.execute("""CREATE TABLE IF NOT EXISTS acolhidos(
                    id_acolhido INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(60) NOT NULL,
                    rg CHAR(9) NOT NULL UNIQUE,
                    cpf CHAR(11) NOT NULL UNIQUE,
                    nascimento DATE NOT NULL,
                    estado_civil TEXT CHECK(estado_civil IN ('solteiro', 'casado', 'separado', 'viuvo', 'divorciado'))
                                            NOT NULL DEFAULT 'solteiro',
                    qtd_filhos INTEGER DEFAULT ('0'),
                    trabalho VARCHAR(20) DEFAULT ('desempregado'),
                    posto_saude VARCHAR(50),
                    lazer VARCHAR(20),
                    substancia_favorita VARCHAR(20),
                    uso_desde_ano INTEGER,
                    religiao VARCHAR(15),
                    responsavel VARCHAR(60),
                    rg_responsavel CHAR(9),
                    cpf_responsavel CHAR(11),
                    vinculo_responsavel VARCHAR(15),
                    entrada DATE DEFAULT (CURRENT_TIMESTAMP),
                    saida DATE,
                    obs TEXT
                    );""")

    # cria tabela medicamentos se já não foi criada
    c.execute("""CREATE TABLE IF NOT EXISTS medicamentos(
                    id_medicamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(30) NOT NULL,
                    especificacoes VARCHAR(100),
                    obs VARCHAR(100)
                    );""")

    # cria tabela entradas_medicamentos se já não foi criada
    c.execute("""CREATE TABLE IF NOT EXISTS entradas_medicamentos(
                    id_entrada INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    id_medicamento INTEGER NOT NULL,
                    qtd_entrada VARCHAR(20) NOT NULL,
                    data_entrada DATE DEFAULT(CURRENT_TIMESTAMP),
                    obs VARCHAR(100),
                    FOREIGN KEY (id_medicamento) REFERENCES medicamentos(id_medicamento)
                    );""")

    # cria tabela controle_medicamentos se já não foi criada
    c.execute("""CREATE TABLE IF NOT EXISTS controle_medicamentos(
                    id_tratamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    id_acolhido INTEGER NOT NULL,
                    id_medicamento INTEGER NOT NULL,
                    qtd_dose VARCHAR(15) NOT NULL,
                    frequencia VARCHAR(15) NOT NULL,
                    inicio_tratamento DATE,
                    termino_tratamento DATE DEFAULT('indefinido'),
                    obs VARCHAR(100),
                    FOREIGN KEY (id_acolhido) REFERENCES acolhidos(id_acolhido),
                    FOREIGN KEY (id_medicamento) REFERENCES medicamentos (id_medicamento)                
                    );""")

    # salva as mudanças
    con.commit()

    # fecha a conexão
    con.close()
