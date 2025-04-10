from InstagramAPI import InstagramAPI
import instaloader,stdiomask,getpass,sys,random,json,requests,threading,time, os.path
from configparser import ConfigParser

def scrape_data(username, password):
    parser = instaloader.Instaloader()
    
    
    parser.login(username,password)
    s = requests.Session()
    # s.save_session_to_file(filename='session.txt')
    # parser.load_session_from_file(s)
    
    api = InstagramAPI(username,password)
    api.login()
   # count = int(input("Enter count to scrap: "))
    try:
        f = open(f"{username}.txt", "w+")
        profile = instaloader.Profile.from_username(parser.context, username)
        list = []
        list = api.getTotalFollowers(profile.userid)
        userids = []
        for i in list:
            #userids.append(str(i.get('pk')))
            f.write(str(i.get('pk'))+"\n")
            # print(i.get('pk'))
    except:
        with open(f'{username}.txt', "w") as f:
           profile = instaloader.Profile.from_username(parser.context, username)
           list = []
           list = api.getTotalFollowers(profile.userid)
           userids = []
           for i in list:
               #userids.append(str(i.get('pk')))
               f.write(str(i.get('pk'))+"\n")
               # print(i.get('pk'))

parser = ConfigParser()
parser.read('config.ini')

print(parser.sections())



for i in parser.sections():
        username = parser.get(i, 'username')
        password = parser.get(i, 'password')
        scrape_data(username, password)
        print("Scraping Done!!!")
        # sent = 0
        # for i in range(int(amount)):
        #     send_all(username,password,message,timeout1,timeout2, amount ,sent)
        #     break
        # break
        # time.sleep(timeout_accountswitch)