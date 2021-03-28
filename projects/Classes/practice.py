

class User:
    # init is a method to initiatize values in the class
    def __init__(self, user_id, username):
        # self is the general version of the object that will be created when you call the class
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # can also create methods which are the things that an object can do. Attributes are the things that it is
    def follow(self, user):
        user.followers += 1
        self.following += 1




user1 = User('69','jwong')
user2 = User('70','jwongg')
user1.follow(user2)