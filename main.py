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
    URL = "https://app.pipefy.com/graphql"
    TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3NTIyNzEwODYsImp0aSI6IjhkNDE5Y2I3LWE2YzUtNGIxYS1iZjQzLWRmNGMyNGU0Njg3ZSIsInN1YiI6MzA2ODE1Mzc2LCJ1c2VyIjp7ImlkIjozMDY4MTUzNzYsImVtYWlsIjoib2xpdmVpcmFicnVub2FAZ21haWwuY29tIn19.CIQTs-cNeZG512sbCWhcr6FHMN_FbbMGzi8lyO7KNrw3Oz8Rcue_hpAIp2Q6Ta_bjED52MBuUMzKDcbJdWrQ1A"
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
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(URL, json={"query": query}, headers=headers)
    data = response.json()

    print(data)
    return "okok"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
