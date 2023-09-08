from firebase import firebase
firebase = firebase.FirebaseApplication('https://students11-default-rtdb.firebaseio.com/',None)
data = {
     #'name': 'hafi',
      # 'place':'malappuram',
       # 'age': 25,
        #'mobile':1234

 }
Result = firebase.delete('https://students11-default-rtdb.firebaseio.com',data)
print(Result)



