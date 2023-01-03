from .user import User

class Manager(User):
  def __init__(self, name, email):
    super().__init__(name, email)

  @staticmethod
  def members():
    raise Exception("Member is'nt authorized to do this action"
    )