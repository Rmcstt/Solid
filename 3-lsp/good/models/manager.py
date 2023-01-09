from .user import User

class Manager(User):
  def __init__(self, username, email):
    super().__init__(username, email)

  @staticmethod
  def members():
    print("Member is'nt authorized to do this action")