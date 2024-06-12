import sqlite3
import os
from settings import DB_PATH

class DBManager():
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

    def check_base(self):
        return os.path.exists(self.db_path)

    def connect_to_db(self):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        return con, cur

    def execute(self, query: str, args=(), many: bool = True):
        con, cur = self.connect_to_db()
        try:
            res = cur.execute(query, args)
            result = res.fetchall() if many else res.fetchone()
            con.commit()
            return {"code": 200, "data": result}
        except sqlite3.Error as er:
            print(str(er))
            return {'code': 500}
        finally:
            con.close()

base_manager = DBManager(DB_PATH)