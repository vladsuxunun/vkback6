import time
import random
import requests
import vk_api 
import os


def ssphoto(tokens):
   succs = "-"
   print("dd")
   randstr = random.randint(36,51)

   if True:
       vk_session = vk_api.VkApi(token = tokens)
       time.sleep(1)
       vk = vk_session.get_api()
       vk.account.getProfileInfo()
       if randstr >= 44 and randstr <= 51:
          pathrand = str(44)
       else:
          pathrand = str(randstr)
       basedir = os.path.abspath(os.path.dirname(__file__))
       cnt1 = 1
       time.sleep(4)
       upload = vk_api.VkUpload(vk_session)
       photo = upload.photo_profile(photo = os.path.join(basedir, ('/app/ssm'+ pathrand +'/' + str(random.randint(1,50))+ '.jpg')))
       time.sleep(3)
       album = vk.photos.createAlbum(title = 'фото')
       ss = album['id']
       album = 1
       path ='ss'
       succs = "+"
   else :
      pass
   if succs == "+":
      for i in range(1,201):
       time.sleep(1)
       try:
          upload = vk_api.VkUpload(vk_session)
          upload.photo(photos=os.path.join(basedir, ('/app/ssm' + pathrand +'/' + str(i) + '.jpg')),album_id =ss)
          upload = 1
       except:
          pass
   else:
      pass


def friend_cnt(tokens):
    try:
        vk_session = vk_api.VkApi(token = tokens)
        vk = vk_session.get_api()
    except:
        pass
    friend = vk.friends.getRequests(count = 50)
    fr1 = friend['items']
    print(fr1)
    for i in fr1:
       try:
        print(vk.friends.add(user_id = i))
       except:
        pass



   