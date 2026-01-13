from Message import Message

test = Message(1, 3, "salut! ceci est un petit message de log pas trop complique")
print(f"Message id : {test.get_id()}\nMessage importance level : {test.get_importance()}\nMessage string : {test.get_string()}\nMessage timestamp : {test.get_timestamp()}")