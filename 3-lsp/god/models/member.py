from .developer import Developer


class Member(Developer):
  def __init__(self, username, email):
    super().__init__(username, email)
    
