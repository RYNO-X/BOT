from ... import db

def str_list(text):
    return text.split(" ")

def list_str(list):
    str = ""
    for x in list:
        str += f"{x} "
    return str

def is_added(chat_id):
    if str(chat_id) in db.get("CHATS").split(" "):
        return True
    else:
        return False

def all_chats():
    chats = db.get("CHATS")
    return str_list(chats)
    

def is_sudo(id):
    if str(id) in db.get("SUDO_USERS"):
        return True
    else:
        return False

def all_sudo():
    sudos = db.get("SUDO_USERS")
    return str_list(sudos)

def add_sudo(id):
    sudos = all_sudo()
    sudos.append(id)
    db.set("SUDO_USERS", list_str(sudos))
    print(sudos)
    return True

def del_sudo(id):
    sudos = all_sudo()
    sudos.remove(id)
    db.set("SUDO_USERS", list_str(sudos))
    return True
    