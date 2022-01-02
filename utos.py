import time
import random
import requests
import vk_api 
import os


def ssphoto(tokens):
   succs = "-"
   print("dd")
   if True:
       vk_session = vk_api.VkApi(token = tokens)
       time.sleep(1)
       vk = vk_session.get_api()
       vk.account.getProfileInfo()
       basedir = os.path.abspath(os.path.dirname(__file__))
       cnt1 = 1
       pathrand = str(1)
       time.sleep(4)
       upload = vk_api.VkUpload(vk_session)
       photo = upload.photo_profile(photo = os.path.join(basedir, ('/app/ss'+ pathrand +'/' + str(random.randint(1,50))+ '.jpg')))
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
          upload.photo(photos=os.path.join(basedir, ('/app/ss' + pathrand +'/' + str(random.randint(1,50)) + '.jpg')),album_id =ss)
          upload = 1
       except:
          pass
   else:
      pass

   