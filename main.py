import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()[7:-1]


@app.route('/')
def home():
    fact = get_fact()
    form = {'input_text': fact}
    req = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/', form, allow_redirects=False)
    link = req.headers['Location']

    #gets the text at the pig latin link
    req2 = requests.get(link)
    #gets the quote from the long string of text
    page = req2.text.split('\n')[8].strip()

    return link


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

