import requests

question_data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean").json()["results"]
