from trello import TrelloApi

trello = TrelloApi('84586947fe8d81f7d6faa30b8e9e2056')

print(trello.boards.get("t6QwKQ74"))
print(trello.boards.get_list("t6QwKQ74"))
print(trello.boards.get_card("t6QwKQ74"))
print(trello.get_token_url('My App', expires='30days', write_access=True))

