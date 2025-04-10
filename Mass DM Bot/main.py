from InstagramAPI import InstagramAPI
import instaloader,stdiomask,getpass,sys,random,json,requests,threading,time, os.path
from configparser import ConfigParser

def send_all(username,password,message,timeout1,timeout2, amount ,sent):

    parser = instaloader.Instaloader()
    parser.login(username,password)
    api = InstagramAPI(username,password)
    api.login()
    file1 = open(f"{username}.txt", 'r')
    file2 = open("sent_file.txt",'a')
    Lines = file1.readlines()
    userid = []
    for line in Lines:
        userid.append(line.strip())
    for i in userid:

        if int(sent) == int(amount):
            break
        else:
            api.sendMessage(i,message)
            print(f"Sent message to username: {i}|","Sent Counter: ",sent+1)
            file2.write(i+"\n")
            time.sleep(random.randint(int(timeout1),int(timeout2)))
            #file1.truncate(0)
            sent += 1
    print("Task Completed")
    file1.close()
    file2.close()

# def send_some(username,password,message,timeout1,timeout2, amount ,sent, arr):
#     f = open(f"{username}.txt", "w+")
#     api = InstagramAPI(username,password)
#     api.login()
#     for i in arr:
#         print(i)
#         api.sendMessage(f"{i}",message)
#         print(f"Sent message to ID: {i}|Account: {username}")
#         time.sleep(random.randint(int(timeout1),int(timeout2)))
#         f.truncate(0)
#     f.close()
#username:password:max_dms_to_send:time_to_wait_after_done
#accounts = ["uauf_:Csk2015!:50:hi you"]

parser = ConfigParser()
parser.read('config.ini')

print(parser.sections())

timeout1 = int(input("Seconds to wait between message: (1): "))
timeout2 = int(input("Seconds to wait between message (2): "))
timeout_accountswitch = int(input("Seconds to wait after each account: "))
username = input("Username of last: ")

for i in parser.sections():
   # do = input("Do you want to  do left?: ")
    # if do == "yes":
    #     if os.path.isfile(f'{username}.txt'):

    #         print(f"Doing last of {username}")
    #         left = []
    #         with open(f'{username}.txt') as left_file:
    #             for line in left_file:
    #                 left.append(line)

    #         print(i)
    #         username = parser.get(i, 'username')
    #         #print(username)
    #         password = parser.get(i, 'password')
    #         #print(password)
    #         amount = parser.get(i, 'amount')
    #         print(amount)
    #         message = parser.get(i, 'message')
    #         #print(message)
    #         sent = 0
    #         for i in left:
    #             send_some(username,password,message,timeout1, timeout2,amount, sent, left)
    #         time.sleep(timeout_accountswitch)
    #         print(f"Starting using username {username}")
    #     else:
    #         pass
    # else:
        print(f"Starting using username {username}")
        print(i)
        username = parser.get(i, 'username')
        #print(username)
        password = parser.get(i, 'password')
        #print(password)
        amount = parser.get(i, 'amount')
        #print(amount)
        message = parser.get(i, 'message')
        #print(message)
        sent = 0
        for i in range(int(amount)):
            send_all(username,password,message,timeout1,timeout2, amount ,sent)
            break
        break
        time.sleep(timeout_accountswitch)