import json
from collections import defaultdict

from flask import Flask, request

import settings
from utils import (get_random_word, get_word_content, get_joke, get_words_stats)


app = Flask(__name__)


def make_response(status_code, data):
    return app.response_class(
        response=json.dumps(data),
        status=status_code,
        mimetype='application/json'
    )

@app.route("/")
def index():
    return make_response(200, {'msg': 'Strings API'})


@app.route("/random")
def random():
    '''API to get random word'''
    error, word = get_random_word()
    if not error:
        resp = make_response(200, {'word': word})
    else:
        resp = make_response(502, {'status': 'error', 'error': error})

    return resp


@app.route("/wikipedia/<string:word>")
def wikipedia_content(word):
    '''API to get random word'''
    error, content = get_word_content(word)
    if not error:
        resp = make_response(200, {'content': content})
    else:
        resp = make_response(502, {'status': 'error', 'error': error})

    return resp


@app.route("/joke/")
def joke():
    '''API to get random word'''
    error, content = get_joke(
        request.args.get('firstName', settings.DEFAULT_FIRST_NAME),
        request.args.get('lastName', settings.DEFAULT_LAST_NAME),
    )
    if not error:
        resp = make_response(200, {'content': content})
    else:
        resp = make_response(502, {'status': 'error', 'error': error})

    return resp
    

@app.route("/stats/<int:limit>")
def stats(limit):
    """Returns a stats of most common words"""
    error, stats = get_words_stats(limit)
    return make_response(502, {'status': 'success', 'stats': stats})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
