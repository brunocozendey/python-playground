#!/usr/bin/python #coding: utf-8

#Instalar libs
#!sudo apt-get install python3-dev default-libmysqlclient-dev
#!pip install pymysql
#!pip install pandas

#importar as libs
import pymysql
import pandas as pd

#Variáveis DB

HOST = 'sat-hdr.copwenuiq12i.us-east-1.rds.amazonaws.com'
PORT = 3306
USER = 'powerbi'
PASSWORD = '375354004'
DB = 'sathdr'

# Preparando SQL com db SHDR
conn = pymysql.connect(
    host= HOST,
    port=PORT,
    user=USER,
    passwd= PASSWORD,
    db=DB)

# Dados de entrada
DATA_INICIAL = '2020-05-01' #AAAA-MM-DD
DATA_FINAL = '2020-05-31' #AAAA-MM-DD

# Query SQL
query = ("SELECT Data.id, Data.froms, Data.city, Data.state, Ezones.city_id, Data.distributor, Data.createdAt, Data.updatedAt, Data.provider FROM Data INNER JOIN Ezones ON Data.city=Ezones.city WHERE Data.createdAt BETWEEN '2020-05-01' AND '2020-05-31' ORDER BY createdAt ASC;").format(DATA_INICIAL, DATA_FINAL)

# Transforma em DataFrame do pandas
ezone_df = pd.read_sql(query, conn)

# Imprime os 50 primeiros resultados
#ezone_df.head(50)


# Transforma em csv
ezone_df.to_csv("submission.csv", index=False)
