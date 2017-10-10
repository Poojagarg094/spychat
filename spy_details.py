# spy_name = "Pooja"
# spy_salutation = "Ms."
# spy_age = 20
# spy_rating = 3.4

#all details in the form of dictionary
#spy_chat = {
    #'name' : 'Pooja',
  #  'salutation' : 'Ms.',
   # 'age' : 21,
    #'rating' : 4.2,
    #'is_online' : True,
    #'chats' : [1]
#}

class spy_chat :
#constructor for initializing class
    def __init__(self, name, salutation, age, rating) :
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
        self.chats_avg = [0.0]
    #default user for spy chat uses

defaultuser = spy_chat('Rahul', 'Mr.', 21,4.7)

friend_one = spy_chat('Sawan', 'Mr.', 23, 2.2)
friend_two = spy_chat('Rohit', 'Mr.', 22, 3.2)
friend_three = spy_chat('Anu', 'Ms.', 21, 2.7)
friend_four = spy_chat('Sapna', 'Ms.', 25, 3.7)
friend_five = spy_chat('Pawan', 'Mr.', 22, 2.9)

friends = [friend_one, friend_two, friend_three, friend_four, friend_five]

class chatmessage:
    def __init__(self, message, sent_by_me):
        self_message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
