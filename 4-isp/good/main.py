from github.client import GithubClient
from repo.parse import RepoParser
from repo.reports_generator import ReportsGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator

from models.member import Member
from models.manager import Manager

if __name__ == "__main__":
  username = 'Rmcstt'
  response = GithubClient.get_repos_by_user(username)

  if response["status_code"] == 200:
    repos = RepoParser.parse(response["body"])
    markdown_report = ReportsGenerator.build(MarkdownGenerator, repos)
    html_report = ReportsGenerator.build(HTMLGenerator, repos)

    print(markdown_report)
    print(html_report)
  else:
    print(response["body"])

  member = Member('renato','renato@gmail.com')
  manager = Manager('50cent','50cent@gmail.com')

  print(member.members())
  
  print(member.work())
  print(manager.work())