import os
from github import Github
from trello import TrelloClient

github_token = os.environ['GITHUB_TOKEN']
trello_api_key = os.environ['TRELLO_API_KEY']
trello_token = os.environ['TRELLO_TOKEN']
trello_board_id = os.environ['TRELLO_BOARD_ID']

g = Github(github_token)
trello = TrelloClient(api_key=trello_api_key, token=trello_token)

repo = g.get_repo("user/repo")
board = trello.get_board(trello_board_id)

for issue in repo.get_issues(state='open'):
    card_title = f"GitHub Issue #{issue.number}: {issue.title}"
    card_desc = issue.body
    board.add_list(card_title).add_card(name=card_title, desc=card_desc)