class User:
    #Constructor
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.following=0

    #Method
    def follow(self):
      
        self.following+=1


user1=User("6541","invishwn")
user2=User("3213","faizmani")


user1.follow()
print(user1.following)