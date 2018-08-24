#do :
# pip install InstagramApi
# then change the image path
# image can be downloaded with wget
# change the username and pass

# and finally change the caption variable to tag all the fadders




from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("username", "password")
InstagramAPI.login()

while 1:
	try :
		photo_path = 'path to picture'
		caption = "@alajaiem"
		InstagramAPI.uploadPhoto(photo_path, caption=caption)
	except KeyboardInterrupt :
		break