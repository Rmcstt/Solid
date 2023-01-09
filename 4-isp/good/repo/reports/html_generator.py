class HTMLGenerator():
  @classmethod
  def build(cls, repos):
    items = ' '.join(f'<strong>ID: </strong>{repo.id} <strong>NAme: </strong>{repo.name} <strong>Size: </strong>{repo.size} kb\n' for repo in repos )

    return f'<p>{items}</p>'