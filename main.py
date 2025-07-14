from flask import Flask
import requests
import os
from dotenv import load_dotenv

# Carregando as variáveis de ambiente do arquivo .env

app = Flask(__name__)
load_dotenv()
url = os.getenv("URL")
token = os.getenv("TOKEN")

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'This is your web app! Let\'s get going!'

@app.route('/pipefy')
def teste_pipefy() -> str:

    query = """
     {
          allCards(pipeId: "306514398") {
            edges {
              node {
                labels {
                  name
                }
                title
                id
              }
            }
          }
    }
    """

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json={"query": query}, headers=headers)
    data = response.json()

    print(data)
    return "okok"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
