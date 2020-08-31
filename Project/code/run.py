from flask import Flask, jsonify, render_template, request,redirect, url_for
import csv
import pandas as pd
import numpy as np
from functions import *

app = Flask(__name__)

data = pd.read_csv('https://raw.githubusercontent.com/myc9799/CSE564-Visualization/master/Project/suicide.csv')
year = None
country = None

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/get_first_country')
def get_first_country():
    country_data = first_country_chart(data, year)
    return jsonify(country_data)

@app.route('/get_first_sex')
def get_first_sex():
    sex_data = first_sex_chart(data, year)
    return jsonify(sex_data)

@app.route('/get_first_age')
def get_first_age():
    age_data = first_age_chart(data, year)
    return jsonify(age_data)

@app.route('/get_second_sex')
def get_second_sex():
    sex_data = second_sex_chart(data, country)
    return jsonify(sex_data)

@app.route('/get_second_age')
def get_second_age():
    age_data = second_age_chart(data, country)
    return jsonify(age_data)

@app.route('/update',methods=['GET','POST'])
def test_post():
    global year

    recv_data = request.get_data()
    if recv_data:
        year = int(str(recv_data,'utf-8'))
    return render_template('home.html')

@app.route('/update_map',methods=['GET','POST'])
def test_post_map():
    global country

    recv_data = request.get_data()
    if recv_data:
        country = str(recv_data,'utf-8')
    print(country)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
