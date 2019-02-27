class User:

    def __init__(self, name):
        self.name = name
        self.chat_room = None

    def join_chat_room(self, chat_room):
        chat_room.add_user(self)
        self.chat_room = chat_room

    def send_message(self, msg):
        if self.chat_room:
            self.chat_room.send_message(self, msg)

    def receive_message(self, msg):
        print('{} received message: {}'.format(self.name, msg))

class ChatRoom:

    def __init__(self):
        self.user_set = set()
    
    def add_user(self, user):
        self.user_set.add(user)

    def send_message(self, user, msg):
        for usr in self.user_set:
            if user != usr:
                usr.receive_message(msg)
if __name__ == '__main__':
    david = User('David')
    alice = User('Alice')
    emily = User('Emily')
    bob = User('Bob')
    bill = User('Bill')

    chat_room = ChatRoom()
    david.join_chat_room(chat_room)
    alice.join_chat_room(chat_room)
    david.send_message('Hello, Alice.')
    emily.join_chat_room(chat_room)
    bob.join_chat_room(chat_room)
    bill.join_chat_room(chat_room)
    bill.send_message('Hello, everyone.')
