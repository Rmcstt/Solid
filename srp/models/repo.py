class Repo():
  def __init__(self, id, name, size):
    self._id = id
    self._name = name
    self._size = size

  @property
  def id(self):
    return self._id

  @property
  def name(self):
    return self._name

  @property
  def size(self):
    return self._size

  def __str__(self):
    return f'id: {self._id} name: {self._name} size: {self._size} bytes'