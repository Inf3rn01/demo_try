from src.database.database_manager import DBManager

def check_login(db_manager: DBManager, login: str, password: str):
    query = "SELECT UserID, TypeID FROM Users WHERE login = ? AND password = ?" # UserID = id, TypeID = post_id
    params = (login, password)
    result = db_manager.execute(query, params)
    if result['code'] == 200 and result['data']:
        UserID, TypeID = result['data'][0]
        return {"id": UserID, "post_id": TypeID}
    else:
        return None

def register(db_manager: DBManager, name: str, login: str, password: str):
    query = "INSERT INTO users (fio, login, password) VALUES (?, ?, ?)"
    params = (name, login, password)
    result = db_manager.execute(query, params, many=False)
    if result['code'] == 200:
        print("Registration successful")
        return True
    else:
        print("Registration failed")
        return False