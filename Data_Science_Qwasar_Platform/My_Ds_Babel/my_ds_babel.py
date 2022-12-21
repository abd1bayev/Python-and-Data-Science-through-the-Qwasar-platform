import csv
import sqlite3
import pandas as pd

class exchange:
    def sql_convert(self):
        ulanish = sqlite3.connect('all_fault_line.db')
        cr = ulanish.cursor()
        cr.execute("SELECT name FROM sqlite_master WHERE type='table'")
        jadval_nomi = cr.fetchone()[0]
#######################################################################################################
        sorov='select * from ' + jadval_nomi
        data = pd.read_sql(sorov, ulanish)
        data.to_csv('all.csv', index=False)
        ulanish.close()
#******************************************************************************************************
    def csv_convert(self, csv_table):
        cn = sqlite3.connect('list.db')
        cr = cn.cursor()
        cr.execute('CREATE TABLE list_volcanos (Volcano_Name,Country,Type,Latitude,Longitude,Elevation)')
#######################################################################################################
        with open(csv_table,'r') as n:
            df = csv.DictReader(n)
            db = [(i['Volcano Name'], i['Country'], i['Type'], i['Latitude (dd)'], i['Longitude (dd)'], i['Elevation (m)']) for i in df]
        cr.executemany("INSERT INTO list_volcanos (Volcano_Name,Country,Type,Latitude,Longitude,Elevation) VALUES (?, ?, ?, ?, ?, ?);", db)
        cn.commit()
        cn.close()
#******************************************************************************************************
jadval = exchange()
jadval.sql_convert()
jadval.csv_convert("list_volcano.csv")
