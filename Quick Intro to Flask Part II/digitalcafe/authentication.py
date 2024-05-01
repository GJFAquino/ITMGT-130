import database as db

def login(username, password):
    is_valid_login = False
    user = None
    error_message = None

    if not (username and password):
        error_message = "Please enter both username and password."
    else:
        temp_user = db.get_user(username)
        if temp_user is not None:
            if temp_user["password"] == password:
                is_valid_login = True
                user = {"username": username,
                        "first_name": temp_user["first_name"],
                        "last_name": temp_user["last_name"]}
            else:
                error_message = "Invalid username or password. Please try again."
        else:
            error_message = "Invalid username or password. Please try again."

    return is_valid_login, user, error_message