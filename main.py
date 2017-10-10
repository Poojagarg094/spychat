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


from spy_details import spy_chat, chatmessage, defaultuser, friends

from steganography.steganography import Steganography #added by running pip install steganography in anaconda navigator
from datetime import datetime #added by running pip install datetime in anaconda navigator
from colored import fg, bg, attr
import sys   #python package  it helps in closing the prgrm because it provide sys.exit() function

import easygui #import easygui to view output on gui mode

easygui.msgbox("WELCOME TO SPY CHAT !!") #by aapplying this we create a box in our app

print "Let's get started"  # our project start

#response = raw_input("Do you want to continue as " + spy_chat['salutation'] + " " + spy_chat['name'] + "? ( yes / no )")  # here we ask ques thats why we use raw_input fn and stored these details in var ie response

#pre-defined STATUS MSG
STATUS_MESSAGES = ["Don't tell people your dreams, SHOW THEM", 'Shaken , not stirred', "typing...",  "I just want to die young as late as possible",]   #square braces bcoz we use list

#import save for saving chat msg
import csv



# #FRDS DETAILS
# friends_name = []
# friends_age = []
# friends_rating = []
# friends_status = []

def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.read(friends_data)

    for row in reader:
        spy_chat = spy_chat(row[0], row[1], row[2], row[3])
        friends.append(spy_chat)

def start_chat(defaultuser):   # def is a fn
    current_status_message = None
    show_menu = True

    #features of app
    while show_menu == True :
        print "you can perform following tasks using spy chat /n"
        menu_options = "what do you want to do ? \n 1) Add a status update \n 2) Add a friend \n 3) Select a friend \n 4) Send a secret message \n 5)Read a secret message \n 6)Read chat of any user \ns7) Close application"
        menu_choice = raw_input(menu_options)

#menu options
        if menu_choice > 0 :
            # to convert other data type into interger Data type
            menu_choice = int(menu_choice)
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

            elif menu_choice == 6:
                print "\nYour Have Selected Chat Read Feature. \n"
                # code for Read a Chat From the user Comes here

            elif menu_choice == 7:
                print "You have selected a close appn feature"
                close_application = "choose (Y/N)"
                close = raw_input("close_application. choose (y/n)")

                if close.upper() == "Y" :
                    show_menu = False
                    exit()
                    easygui.msgbox("THANX FOR USING SPY CHAT. I HOPE U ENJOYED A LOT")

                else:
                    show_menu == True

    else:
        print "select valid option"




    #FOR ADDING STATUS MSG FUNCTION DEFINE HERE
def add_status(current_status_message):
    updated_status_message = None
    if defaultuser.current_status_message != None:     #always remember : colon in if else and != indicates not equal to
        print "Your current status message is " + defaultuser.current_status_message + "\n"
    else:
        print "You don't have any status message curently \n"

    default = raw_input("Do you want to select from the older status (Y/N)")

    # updated_status_message=""
    # current_status_message=""

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set ? ")

        if len(new_status_message)>0:
            #update the STATUS MSGS
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
            print " Now your status msg is : ' " + updated_status_message +  " ' \n "
            defaultuser.current_status_message = updated_status_message

        else:
            print "Plzz enter a valid status update"

    elif default.upper() == 'Y':
        item_position = 1

        for message in STATUS_MESSAGES:
            print str(item_position) + " " + str(message)
            item_position = item_position + 1
        message_selection =int(raw_input(" \n Choose from the above messages "))
        if len(STATUS_MESSAGES) >= message_selection :   # here we check length of any status
            updated_status_message = STATUS_MESSAGES[message_selection - 1]   #-1 bcoz item_position will be started from 1
            #current_status_message = add_status(current_status_message)

    else:
        print "Press y or n only"

    if updated_status_message :
        print "\n Now your status is : ' " + updated_status_message +  " ' \n "
        defaultuser.current_status_message = updated_status_message
    else:
        print "You dont have any status update"

    # return updated_status_message  # this stmt here bcoz here work if or else in both case status return value

#FOR ADD A FRD FUNCTION DEFINES HERE
def add_friend():

    # new_friend = spy_chat{
    #     'name' :'',
    #     'salutation' :'',
    #     'age' : 0,
    #     'rating' : 0.0,
    #     'chats' : []
    #  }
    new_friend = spy_chat('', '', 0, 0.0)

    new_friend.name = raw_input("Plz add your friend's name ")   #concept of dict and always use square braces
    new_friend.salutation = raw_input(" Are they Mr. or Ms. ?")
    # new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    new_friend.name = new_friend.salutation + " " + new_friend.name

    # new_friend.age = raw_input("Age ")
    # new_friend.age = int(new_friend.Age )

    new_friend.age = raw_input(new_friend.name + "\'s Age:  \t")
    # coverting input data to integer format
    new_friend.age = int(new_friend.age)

    # new_friend.rating = raw_input("spy_rating")
    # new_friend.rating = float(new_friend.rating)
    new_friend.rating = raw_input(new_friend.name + "\'s Smart rating? \t")
    # converting input data into float
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and  new_friend.rating >= 1 :
        # print "Friend Added"   #add friend
        # friends_name.append(new_name)   #adding new data of frds lists  and list declare above already
        # friends_age.append(new_age)
        # friends_rating.append(new_rating)
        # friends_status.append(True)
        friends.append(new_friend)
        print "new friend name %s age  %d  of rating  %2f  Added into friend list."  %(new_friend.name, new_friend.age, new_friend.rating)

    else:
        print "Sorry ! Invalid entry. We can't add spy with the details you provided"  #if not a above single cndn matched then this cndn print
    return len(friends)    #return value of friends


    #SELECT A FRIEND FUNCTION HERE
def select_friend():
    def view_friend():
        item_number = 0
        for friend in friends:  #it will select all frds from frds list
            print '\t%d %s age %d ratinng %2f is online' %((item_number + 1), friend.name, friend.age, friend.rating)
            item_number = item_number + 1

    view_friend()
    friend_choice = raw_input("choose from your friends")
    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position #return selected frd number


#sending a secret msg
def send_message():
    friend_choice = select_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Secured_image = raw_input("Enter Name (without extension .jpg) For Newly Generated Secure Message File : \t")
    # set the name for the out secure image with text
    output_path = Secured_image + '.jpg'
    Steganography.encode(original_image, output_path, text)

    temp = text.split(' ')
    # If a Smart send a message with special words such as SOS, SAVE ME etc. you should display an appropriate message
    special = ['SOS', 'sos', 'HELP', 'Save', 'save']
    for any in special:
        if any in temp:
            temp[temp.index(any)] = ' Please Help Me. i am In Denger. Contact me as soon as Possible'
    # replece with new full length message
    text = str.join(' ', temp)

    new_chat = {
        "message" : text,
        "time" : datetime.now(),  #it represents current time
        "sent_by_me" : True
    }
   # print new_chat['message']
    friends[friend_choice].chats.append(new_chat)

    print 'Your secret message is ready? "%s"' %output_path

#read a secret msg fn
def read_message():

    owner = select_friend()
    output_path = raw_input("Enter image name without extension") + ".jpg"
    try:
        secret_text = Steganography.decode(output_path)
    except ValueError:
        print "\tNo Any Secret Message In This Image. Please Try Another Image File \n"
        read_message()
    #secret_text = Steganography.decode(output_path)
    # new_chat = {
    #     "message": text,
    #     "time": datetime.now(),  # it represents current time
    #     "sent_by_me": False
    # }

    #friends[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready?" + secret_text + ' " '


print "APP STARTED"
question = '\n Continue as' + defaultuser.salutation + "" +defaultuser.name + "(y/n)? "
existing = raw_input(question)

if existing.upper() == "Y":   #app start upper change letters
    defaultuser.name = defaultuser.salutation + "" +defaultuser.name
    print "Welcome " + defaultuser.salutation + defaultuser.name + " Glad to have you back with us"
    AskForPassword = defaultuser.name + " Please Enter your password: \t"
    password = raw_input(AskForPassword)
    #  check and verify password here
    if password == "":
        #  print "Authentication complete. Welcome " + vchat.name + " age: " + str(vchat.age) + " and rating of: " + str(vchat.rating) + " Proud to have you onboard"
        print "\nAuthentication Complete. Welcome %s Age: %d and Rating of: %.1f Proud to have you onboard." % (
        defaultuser.name, defaultuser.age, defaultuser.rating)
        print "Now You Can Start Chat with your Friends."
        #  after all varifaction chat will start from here as a old user
        start_chat(defaultuser)
    # if user Enter Wrong password
    else:
        print "\n\t Please Enter Correct password. and Try again"
        easygui.msgbox("Please Enter Correct password", 'password Issue', ("Close"))

# if a new user(not want to start as a old User) want to srart using Smart Vchat

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

elif existing.upper() == "N":
    new_user = spy_chat('', '', 0, 0.0)
    new_user.name = raw_input('Welcome to spy chat , U must tell your appy name first : ')
    # spy_chat.name= spy_name

    #loop
    # while True:

    if len(new_user.name)>0:

            #newuser.salutation = raw_input("Should I call you (Mr. or Ms.) ? \t")
        new_user.salutation = raw_input("What would we call you (Mr. or Ms.)?")
            #spy_name = spy_salutation + " " + spy_name  #it doesnt work bcoz we have to give keyword print
        new_user.name = new_user.salutation + ' ' + new_user.name
        print "Alright " + new_user.salutation + " " + new_user.name + " I'd like to know a little bit more about you before we proceed"

        new_user.age = input("What is your Spy age ? ")
        if new_user.age>12 and new_user.age<50:

            new_user.rating = input("What is your spy rating ? ")

            if new_user.rating > 4.7:
                print "you are great"

            elif new_user.rating>3.5 and new_user.rating<4.5:
                print "work harder"
            elif new_user.rating > 2.5 and new_user.rating <= 3.5:
                print 'You can always do better'
            new_user.is_online = True
                #  print "Authentication complete. Welcome " + vchat.name + " age: " + str(vchat.age) + " and rating of: " + str(vchat.rating) + " Proud to have you onboard"
            print "\nAuthentication Complete. Welcome %s Age: %d and Rating of: %.1f Proud to have you onboard." % (
            new_user.name, new_user.age, new_user.rating)
            print "\t Now You Can Start Chat with your Friends."
                #  after all varifaction chat will start from here as a old user
            start_chat(new_user)
        else:
            print "Sorry you are not of the correct age to be a spy"
                #sys.exit()
            # spy_chat_is_online = True  # T in caps
            # print "Authentication Complete. Welcome  %s age :  %d and rating of :  %1f  \n Proud to have you entered" #here we use str() fn bcoz int and str never concatanate together
            # break
    else:  # semicolon must and indentation too
        print "A Spy needs to have a valid name. Try Again please"
    # start_chat(spy_chat)