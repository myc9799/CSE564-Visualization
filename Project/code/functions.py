import pandas as pd
import numpy as np
import json
from flask import Flask, jsonify,render_template

# first country bar chart
def first_country_chart(data, year=None):
    data_useful = _1_get_year_df(data, year)
    return _1_get_country(data_useful)

def _1_get_country(data):
    return_data = []
    country_series = pd.DataFrame(data.groupby(by=['country'])['suicides_no'].sum()).sort_values(by='suicides_no', ascending=False).head(10)
    for i in range(country_series.shape[0]):
        eachData = {}
        eachData['class'] = country_series.iloc[i].name
        eachData['num'] =  int(country_series.iloc[i].values[0])
        return_data.append(eachData)
    return return_data

def _1_get_year_df(data, num_=None):
    if(num_==None):
        return data
    else:
        return data.loc[data['year'] == num_]

def _1_get_age(data):
    age_series = pd.DataFrame(data.groupby(by=['age'])['suicides_no'].sum())
    return_data = []
    for i in range(age_series.shape[0]):
        eachData = {}
        eachData['class'] = age_series.iloc[i].name
        eachData['num'] =  round(age_series.iloc[i].values[0]/age_series['suicides_no'].sum()*100, 2)
        return_data.append(eachData)
    return return_data

def _1_from_age_get_sex(data, str_=None):

    return_data = []

    if(str_==None):
        sex_series = pd.DataFrame(data.groupby(by=['sex'])['suicides_no'].sum())
    else:
        age_data = data.loc[data['age'] == str_]
        sex_series = pd.DataFrame(age_data.groupby(by=['sex'])['suicides_no'].sum())

    for i in range(sex_series.shape[0]):
        eachData = {}
        eachData['class'] = sex_series.iloc[i].name
        eachData['num'] =  round(sex_series.iloc[i].values[0]/sex_series['suicides_no'].sum()*100, 2)
        return_data.append(eachData)

    return return_data

def _2_get_country_df(data,str_=None):
    if(str_==None):
        return data
    else:
        return data.loc[data['country']==str_]

# first age pie chart
def first_age_chart(data, year=None):
    data_useful = _1_get_year_df(data, year)
    return _1_get_age(data_useful)

# first sex pie chart
def first_sex_chart(data, year=None, age=None):
    data_useful = _1_get_year_df(data, year)
    return _1_from_age_get_sex(data_useful,age)

# second age pie chart
def second_age_chart(data, country=None):
    data_useful = _2_get_country_df(data, country)
    return _1_get_age(data_useful)

# second sex pie chart
def second_sex_chart(data, country=None, age=None):
    data_useful = _2_get_country_df(data, country)
    return _1_from_age_get_sex(data_useful,age)


# import json
#
# def get_trend(data,country_name=None):
#     year_list = pd.unique(data['year']).tolist()
#     year_list.sort()
#     return_data = []
#     for item in year_list:
#         eachData = {}
#         if(country_name==None):
#             data=data
#         else:
#             data=data.loc[data['country'] == country_name]
#         data_ = data.loc[data['year'] == item]
#         num_ = data_['suicides_no'].sum()
#         eachData['num'] = int(num_)
#         eachData['year'] = item
#         return_data.append(eachData)
#     return return_data
#
# def download_data(data, country_list):
#     for i in range(len(country_list)):
#         data_ = get_trend(data, country_list[i])
#         with open(country_list[i].replace(' ', '')+'.json', 'w') as outfile:
#             json.dump(data_, outfile)
#
#     data_ = get_trend(data)
#     with open('world.json', 'w') as outfile:
#         json.dump(data_, outfile)
#
# top_ten = list(pd.DataFrame(data.groupby(by=['country'])['suicides_no'].sum()).sort_values(by=['suicides_no'],ascending=False).head(10).index.values)
# download_data(data, top_ten)