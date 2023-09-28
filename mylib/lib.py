"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests

def extract(url="https://catalogue.data.wa.gov.au/dataset/f39087e2-2885-473e-bc62-ca610cd94340/resource/96c892f3-b387-410c-80d0-e4dcec68e6f2/download/25ktopomapseriesindex.csv", 
            file_path="/Users/xiahaochong/Desktop/IDS 706 DES/Haochong-Week-5/25ktopomapseriesindex.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path

"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="/Users/xiahaochong/Desktop/IDS 706 DES/Haochong-Week-5/25ktopomapseriesindex.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('ktopomapseriesindexDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS ktopomapseriesindexDB")
    c.execute("CREATE TABLE ktopomapseriesindexDB (name_cap_2,num_rom_ca,Shape_Leng,Shape_Area)")
    #insert
    c.executemany("INSERT INTO ktopomapseriesindexDB VALUES (?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "ktopomapseriesindexDB.db"

"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("ktopomapseriesindexDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ktopomapseriesindexDB")
    print("Top 5 rows of the ktopomapseriesindexDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
