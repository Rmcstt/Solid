from .user import User

class Member(User):
  def __init__(self, name, email):
    super().__init__(name, email)
    
  @staticmethod
  def members():
    return ['username1','username2','username3','team1']

  def pay(self):
    pass

  def code(self):
    return 'coding...'