from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/words/<string:given_word>')
def anagrams(given_word):
    l = []
    f = open('words.txt')
    word_list = f.read().splitlines()
    for word in word_list:
        if sorted(given_word.upper()) == sorted(word):
            l.append(word)
        else:
            continue
    return render_template('anagrams.html', given_word=given_word, l=l)