import instaloader
test=instaloader.Instaloader()
acc=input("enter the user name")
test.download_profile(acc,profile_pic_only=True)