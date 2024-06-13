from database_manager import DBManager

def check_login(db_manager: DBManager, login: str, password: str):
    query = "SELECT id, name, post_id FROM users WHERE login = ? AND password = ?"
    params = (login, password)
    result = db_manager.execute(query, params)
    if result['code'] == 200 and result['data']:
        user_id, name, post_id = result['data'][0]
        return {"id": user_id, "name": name, "post_id": post_id}
    else:
        return None

def register(db_manager: DBManager, name: str, login: str, password: str):
    query = "INSERT INTO users (name, login, password) VALUES (?, ?, ?)"
    params = (name, login, password)
    result = db_manager.execute(query, params, many=False)
    if result['code'] == 200:
        print("Registration successful")
        return True
    else:
        print("Registration failed")
        return False