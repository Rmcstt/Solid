class MarkdownGenerator():
  @classmethod
  def build(cls, repos):
    items = ' '.join(f'**ID: **{repo.id} **NAme: **{repo.name} **Size: **{repo.size}\n' for repo in repos )

    return f'## REPOS \n\n{items}'