import Credential

from instabot import Bot

import os

import time 

from random import * 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if os.path.isfile(Credential.path+"config/"+Credential.my_username+"_uuid_and_cookie.json"):
    os.remove(Credential.path+"config/"+Credential.my_username+"_uuid_and_cookie.json")


bot = Bot(
    filter_users=True,
    filter_private_users=True,
    filter_previously_followed=True,
    filter_business_accounts=True,
    filter_verified_accounts=True,
    max_likes_per_day=200000,
    max_follows_per_day = 10000,
    max_comments_per_day = 20000,
    min_likes_to_like=0,
    max_likes_to_like=400,
    like_delay=3,
    min_followers_to_follow = 10000 ,
    min_following_to_follow =10000,
    follow_delay=35,
    comment_delay=20,
    )


# Login The Bot 
bot.login(username=Credential.my_username, password=Credential.my_password,force=True)



#Asking User To Input Username Of The Instagram User To Get His Followers 
insta_username = "faizu2407" #input("\n \n Enter Instagram Username : ")

# Getting Follower Using Isnta Bot 
followers=bot.get_user_followers(insta_username)

msg = "Hello Your Profile Is Amazing !! You Are Looking Very Cool !! support me to reach 100k my dream  i makes a reels video hope you guys like it please share like comment follow me and support me Here Is The Link  :-- \n  https://instagram.com/attitudeloverr_143"

for user_id in followers:  
    user_info = bot.get_user_info(user_id)
    if user_info["is_private"] == True:
        bot.follow(user_id)
        print("Followed The User")
        print("\n \n \t \t Waiting For Some Seconds")
        time.sleep(randint(2,6))
        bot.send_messages(msg, [user_id])
    else:
        bot.follow(user_id)
        print("Followed The User")
        print("\n \n \t \t Waiting For Some Seconds")
        time.sleep(randint(2,6))
        bot.send_messages(msg, [user_id])
        print("This Is A Public Account ")
        medias=bot.get_user_medias(user_id)
        if len(medias) > 3 :
            time.sleep(randint(2,6))
            for i in range(2):
                bot.like(medias[i])
                print("\n \t Liked The Post")
                print("\n \n \t \t Waiting For Some Seconds")
                time.sleep(randint(2,6))
                cmt = ["Jabardast ","The Perfect Click !! Awesome ","Amazing Post  ","Jabardast","Supper ","Jhakas "]
                bot.comment(medias[i],cmt[randint(0,5)])
                print("\n \t Commented On  The Post")
                time.sleep(randint(2,6))
        else:
            print("\t \t This User Have No Media Skiiping This !!")
        
        time.sleep(randint(2,6))

print("Task Completed")