class User: # use Pascal case for class names: every word capital (camel has first word lowercase)
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # set initial value for followers
        self.following = 0
        # print("new user being created...")

    # self refers to the object that will be created from this class inside the class blueprint
    def follow(self, user):
        user.followers += 1 # user is the user that self will follow
        self.following += 1


user_1 = User("001", "angela") # this is a constructor
# user_1.id = "001" # can add attributes to the object
# user_1.username = "angela"

user_2 = User("002", "jack")
# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"
# ^ this is repetitive, can use a constructor instead

user_1.follow(user_2) # in follow, user_1 is self, user_2 is user
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# def function():
#     pass # gets rid of "expected indent" error on print line below
#
# print("hello")