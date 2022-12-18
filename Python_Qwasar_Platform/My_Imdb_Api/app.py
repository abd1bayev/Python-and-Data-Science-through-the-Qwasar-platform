import logging
from flask import Flask, request
import csv
import json

app = Flask(__name__)
data = []

with open('imdb-movie-data.csv', 'r', encoding="utf-8") as f:
    file = csv.reader(f, delimiter=',')
    for row in file:
        data.append(row)
        # print(data)


@app.route('/')
def info():
    genre = request.args.get('genre', default=None, type=str)
    result_rows = [[e or None for e in row] for row in data[1:] if genre.title() in row[2]]
    return json.dumps([dict(zip(data[0], row)) for row in result_rows], separators=(",", ":"))

@app.route('/<genre>')
def info2(genre):
    result_rows = [[e or None for e in row] for row in data[1:] if genre.title() in row[2]]
    a = json.dumps([dict(zip(data[0], row)) for row in result_rows], separators=(',', ':'))
    return a
# print(a)


if __name__ == '__main__':
    app.run(host='localhost', port=8080)