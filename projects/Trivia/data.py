import requests
import json

question_data = []

parameters = {
    'amount':10,
    'type':'boolean'
}

response = requests.get('https://opentdb.com/api.php?',params=parameters)
data = response.json()
question_data = data['results']

print(question_data)

