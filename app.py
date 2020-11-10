import flask 
from flask import request, jsonify, render_template
import sqlite3
import json

app = flask.Flask(__name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/period', methods=['GET'])
def get_years():
    conn = sqlite3.connect('brics.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_years = cur.execute('SELECT * FROM years;').fetchall()
    return jsonify(all_years)

@app.route('/countries', methods=['GET'])
def get_countries():
    conn = sqlite3.connect('brics.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_countries = cur.execute('SELECT * FROM countries;').fetchall()
    return jsonify(all_countries)

@app.route('/names', methods=['GET'])
def get_names():
    conn = sqlite3.connect('brics.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_name = cur.execute('SELECT * FROM names;').fetchall()
    return jsonify(all_name)

@app.route('/brics', methods=['GET'])
def get_brics():
    conn = sqlite3.connect('brics.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_brics = cur.execute('SELECT * FROM brics;').fetchall()
    return jsonify(all_brics)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')