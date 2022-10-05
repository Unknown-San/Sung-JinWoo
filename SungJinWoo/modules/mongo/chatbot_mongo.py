"""@Kaizuryu"""

from SungJinWoo import mongodb as db_x

SungJinWoo = db_x["CHATBOT"]


def add_chat(chat_id):
    SungJin = SungJinWoo.find_one({"chat_id": chat_id})
    if SungJin:
        return False
    SungJinWoo.insert_one({"chat_id": chat_id})
    return True


def remove_chat(chat_id):
    SungJin = SungJinWoo.find_one({"chat_id": chat_id})
    if not SungJin:
        return False
    SungJinWoo.delete_one({"chat_id": chat_id})
    return True


def get_all_chats():
    r = list(SungJinWoo.find())
    if r:
        return r
    return False


def get_session(chat_id):
    SungJin = SungJinWoo.find_one({"chat_id": chat_id})
    if not SungJin:
        return False
    return SungJin
