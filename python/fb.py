import pyrebase
import json

config = {
  "apiKey": "AIzaSyATXHe94YBU8n1wbEsbGwFfVitO9XXQ79s",
  "authDomain": "https://notifier-a756e.firebaseapp.com",
  "databaseURL": "https://notifier-a756e.firebaseio.com",
  "storageBucket": "notifier-a756e.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#Retrieve Data
all_users = db.child("Users").get()
for user in all_users.each():
	#print(user.val())
	print

#Save Data
data = {"animal": "Dragon","numberPlate":"MKBHD69","time":"now"}
testKey=db.child("test").push(data)
j = json.dumps(testKey)
a = json.loads(j)
key = a["name"]
print(key)


#Store image
storage = firebase.storage()
storage.child("images").child(key+".jpeg").put("p.jpeg")

#Download image
storage.child("images").child(key+".jpeg").download("downloaded.jpg")
