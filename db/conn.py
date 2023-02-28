from pymongo import MongoClient
from pymongo import errors
from contextlib import suppress
from os import getenv


def conn_db():
    conn_db = getenv('MONGO_DB')
    with suppress(errors.ConnectionFailure()):
        adm = MongoClient(conn_db)
        database = adm['adm']
        return database


tabela_publicacoes = conn_db()['publicacoes']

tabela_publicacoes.insert_one({"nome": "Ohhh ze", "data": "02/10/2022"})
