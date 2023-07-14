from infra.configs.connection import DBConnectionHandler
from infra.entities.aposta import Aposta

class ApostaRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Aposta).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Aposta).filter(Aposta.id == id).first()
            return data

    def insert(self, aposta:Aposta):
        with DBConnectionHandler() as db:
            try:
                db.session.add(aposta)
                db.session.commit()

                return "OK"
            except Exception as e:
                db.session.rollback()
                return e

    def delete_all(self):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Aposta).delete()
                db.session.commit()

            except Exception as e:
                db.session.rollback()
                return e

