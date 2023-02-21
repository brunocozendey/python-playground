#!/usr/bin/python #coding: utf-8
from flask import Flask, render_template, send_file, redirect, request
##!sudo apt-get install python3-dev default-libmysqlclient-dev
##!pip install pymysql
##!pip install Flask
##!pip install pandas

import pymysql
import pandas as pd

'''
conn = pymysql.connect(
    host='sat-hdr.copwenuiq12i.us-east-1.rds.amazonaws.com',
    port=3306,
    user="powerbi",
    passwd='375354004',
    db="sathdr")
'''


app = Flask(__name__, template_folder='template_folder')

@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        #req = request.form
        data_ini = request.form.get("data_ini")
        data_fim = request.form.get("data_fim")
        return redirect(request.url)
    
    return render_template('index.html')
    #return "Hello, World!"

@app.route("/download")
def download():
    query = "SELECT DISTINCT Data.id, Data.date, Data.city, Data.state, Ezones.city_id, Data.scua, Data.caid,  Data.distributor, Data.createdAt, Data.updatedAt, Data.provider FROM Data INNER JOIN Ezones ON Data.city=Ezones.city WHERE Data.date BETWEEN '2020-06-01' AND '2020-06-30' GROUP BY Data.scua ORDER BY date ASC;"
    ezone_df = pd.read_sql(query, conn)
    
    ## Para DEBUG
    #d = {'col1': [1, 2], 'col2': [3, 4]}
    #ezone_df = pd.DataFrame(data=d)
    
    # Transforma o DF para CSV e encoda no formato pra abrir no Excel.
    ezone_df.to_csv('df.csv', index=False, encoding = "ISO-8859-1", sep=";")
    
    return send_file('df.csv',
                     mimetype='text/csv',
                     attachment_filename='SHDR-Ativacoes.csv',
                     as_attachment=True)    

if __name__ == '__main__':
    app.run()