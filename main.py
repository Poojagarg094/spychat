# Notes:
# 1) PRINT: it is keyword.after print anything is wriiten it always shown on terminal and we can use single as well as double quotes.
# 2) we use \ as ignoring character
#3) raw_input is the function in which user give output acc to his\her wish we just ask question here
#4) for cancatenation we store input in VARIABLE AND for  concatenation we use + sign
#5) if we want to see ZEN OF PYTHON mean Why we use so just write in console IMPORT THIS in small letters
#6) AND / OR keyword is used to combine two if statements
#7)ducktyping : ability to declare int boolean by just providing a no. like o for int and true for boolean and 0.0 for float
#8) else if replaced by elif
#9) pattern
    # if
    #     if
    #     elif
    #     else
    # elif
    # else
#10) %s show blank space and place is holding by any value by using this we ignore the concat method
#11) str() function used for concatenation string and int together. we make int no. as a string
#12) IMPORT : import allows us to use pre-defined variables and functions from other files . for using this we write case-1 entire file import       import file-name and print file-name variable-name      case-2) some content of another file       from file-name import diff var  and print  var
#13) DRY programming : it states that never repeat urself
#14) list : datatype in python and no specific data types mean we can stored int str float together in memory and start with 0 i.e similar to array 1) for creating SYNTAX : list_name = [values1 , ----] mean always use square braces and values seprated by commas  2) for reading  SYNTAX:  print(list [index called number])

# print 'hello world!' # if we simply type this hello world and then type in terminal python file-name.extension i.e python main.py then it will show output i.e hello world
# print "hello world"  # both way of writing are correct mean we use'' & " " both
# print "hello world's" # thats why we use double quotes sometime
# print 'hello world\'s'# here\ back slash work as ignoring character
#len() is a function which  tell length of a string
#if() it is a keyword or condition and every condtn has an action that is true and false
#: show work of braces or if loop starts


from spy_details import spy_chat

print "Let's get started"  # our project start

response = raw_input("Do you want to continue as " + spy_chat['salutation'] + " " + spy_chat['name'] + "? ( yes / no )")  # here we ask ques thats why we use raw_input fn and stored these details in var ie response

#pre-defined STATUS MSG
STATUS_MESSAGES = ['My name is Pooja, Pooja Garg' , 'Shaken , not stirred']   #square braces bcoz we use list

#FRDS DETAILS
friends_name = []
friends_age = []
friends_rating = []
friends_status = []

def start_chat(spy_chat):   # def is a fn
    current_status_message = None
    show_menu = True

    #features of app
    while show_menu == True :
        print "you can perform following tasks using spy chat"
        menu_options = "what do you want to do ? \n 1) Add a status update \n 2) Add a friend \n 3) Select a friend \n 4) Send a secret message \n 5)Read a secret message \n 6)Read chat of any user \ns7) Close application"
        menu_choice = int(raw_input(menu_options))

#menu options
        if menu_choice == 1:  # here 1 is not in commas bcoz above we write int so not convertedc in string
            #print 'Status update function called'
            print "You have select a status feature"
            current_status_message = add_status(current_status_message)
        elif menu_choice == 2:
            print "You selected Add a friend feature"
            number_of_friends = add_friend()
            print "You have %d friends" %(number_of_friends)

        elif menu_choice == 3:
            print "You have selected a Select friend feature"
            select_friend()

        elif menu_choice == 4:
            print "You have selected a Send secret msg feature"
            send_message()

        elif menu_choice == 5:
            print "You have selected to read a secret msg feature"
            read_message()

        elif menu_choice == 7:
            print "You have selected a chat read feature"

        else:
            show_menu = False

    print "Thank you for using spy chat"

    #FOR ADDING STATUS MSG FUNCTION DEFINE HERE
def add_status(current_status_message):
    if current_status_message != None:     #always remember : colon in if else and != indicates not equal to
        print "Your current status message is " + current_status_message + "\n"
    else:
        print "You don't have any status message curently \n"
    default = raw_input("Do you want to select from the older status (Y/N)")

    if default.upper == "N":
        new_status_message = raw_input("What status message do you want to set ? ")

        if len(new_status_message)>0:
            #update the STATUS MSGS
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)

    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print str(item_position) + " " + message
            item_position = item_position + 1
        message_selection = input(" \n Choose from the above messages ")
        if len(STATUS_MESSAGES) >= message_selection :   # here we check length of any status
            updated_status_message = STATUS_MESSAGES[message_selection - 1]   #-1 bcoz item_position will be started from 1
            current_status_message = add_status(current_status_message
                                                )
    return updated_status_message  # this stmt here bcoz here work if or else in both case status return value


    #FOR ADD A FRD FUNCTION DEFINES HERE
def add_friend():
    new_friend ={
        'name' :"",
        'salutation' :"",
        'age' : 0,
        'rating' : 0.0
                }

    new_friend['name'] = input("Plz add your friend's name ")   #concept of dict and always use square braces
    new_friend['salutation'] = input(" Are they Mr. or Ms. ?")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    new_friend['age'] = input("Age ")
    new_friend['rating'] = input("spy_rating")
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and  new_friend['rating'] >= spy_chat['rating'] :
        # print "Friend Added"   #add friend
        # friends_name.append(new_name)   #adding new data of frds lists  and list declare above already
        # friends_age.append(new_age)
        # friends_rating.append(new_rating)
        # friends_status.append(True)
        friends.append(new_friend)
        print "friends added"

    else:
        print "Sorry ! Invalid entry. We can't add spy with the details you provided"  #if not a above single cndn matched then this cndn print
    return len(friends)    #return value of friends

    #SELECT A FRIEND FUNCTION HERE
def select_friend():
    item_number = 0
    for friend in friends:
        print '%d %s' %(item_number + 1), friends['name']
        item_number = item_number + 1

    friend_choice = raw_input("choose from your friends")
    friend_choice_position = friend_choice - 1

    return friend_choice_position



if response == "yes":   #app start
    print "APP STARTED"
    print "Welcome " + spy_chat['salutation'] +" " + spy_chat['name']
    #start_chat(spy_chat['name'], spy_chat['age'], spy_chat['rating'])

# #raw_input('What\'s your name?')   #after running o terminal we always seen that cursor blink in case if input means user first give inpu and after that it will proceed
#           # now we save name in one variable so just modify this code
# spy_name =raw_input("What's ur name?")#spy_name is variable in which name is stored
# #print "Welcome " + spy_name + " Glad to have you back with us"  # here we done concatenation
# spy_salutation = raw_input("What would we call you (Mr. or Ms.)?")
# print "Welcome " + spy_salutation + spy_name + " Glad to have you back with us"
# # name= "Mr. Bond"    it is an example of showing length and how indentation work
# # if len(name)>0:
# #     new_message = 'yay! name is not empty'   # indentation
# #     print new_message    again we modify all above code
else:
    spy_name = raw_input('Welcome to spy chat , U must tell your appy name first : ')

    if len(spy_chat['name'])>0:

        print "Welcome " + spy_chat['name'] + " Glad to have you back with us"
        spy_chat['salutation'] = raw_input("What would we call you (Mr. or Ms.)?")
        #spy_name = spy_salutation + " " + spy_name  #it doesnt work bcoz we have to give keyword print
        print "Alright " + spy_chat['salutation'] + " " + spy_chat['name'] + " I'd like to know a little bit more about you before we proceed"

        spy_chat['age'] = input("What is your Spy age ? ")
        if spy_chat['age']>12 and spy_chat['age']<50:

            spy_chat['rating'] = input("What is your spy rating ? ")

            if spy_chat['rating'] > 4.7:
                print "you are great"

            elif spy_chat['rating']>3.5 and spy_chat['rating']<4.5:
                print "work harder"

        else:
            print "Sorry you are not of the correct age to be a spy"

        spy_chat_is_online = True  # T in caps
        print "Authentication Complete. Welcome " + spy_name + " \n age : " + str(spy_chat['age']) + " and rating of " + str( spy_chat['rating']) + " \n Proud to have you entered" #here we use str() fn bcoz int and str never concatanate together

    else:  # semicolon must and indentation too
        print "A Spy needs to have a valid name. Try Again please"
        start_chat(spy_chat['name', 'age', 'rating'])