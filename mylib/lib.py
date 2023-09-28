"""
Extract a dataset from a URL

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
    c.execute("DROP TABLE IF EXISTS indexs")
    c.execute('''CREATE TABLE IF NOT EXISTS indexs (
                name_cap_2 TEXT,
                num_rom_ca TEXT PRIMARY KEY,
                Shape_Leng INTEGER,
                Shape_Area INTEGER
            )''')
    #insert
    c.executemany("INSERT INTO indexs VALUES (?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "ktopomapseriesindexDB.db"

"""CRUD"""

def connect():
    conn = sqlite3.connect('ktopomapseriesindexDB.db')
    c = conn.cursor()
    return c, conn

def create(c):
    # Connect to my DB
    c.execute('''CREATE TABLE IF NOT EXISTS indexs (
                name_cap_2 TEXT,
                num_rom_ca TEXT PRIMARY KEY,
                Shape_Leng INTEGER,
                Shape_Area INTEGER
            )''')
    
def insert(c, conn, name_cap_2, num_rom_ca, Shape_Leng, Shape_Area):
    c.execute("INSERT INTO indexs (name_cap_2, num_rom_ca, Shape_Leng, Shape_Area) VALUES (?, ?, ?, ?)", (name_cap_2, num_rom_ca, Shape_Leng, Shape_Area))
    conn.commit()

def read(c):
    c.execute("SELECT * FROM indexs")
    indexs = c.fetchall()
    return indexs

def update_Shape_Leng(c, conn, Shape_Leng, num_rom_ca):
    c.execute("UPDATE indexs SET Shape_Leng = ? WHERE  num_rom_ca = ?", (Shape_Leng, num_rom_ca))
    conn.commit()

def delete(c, conn, num_rom_ca):
    c.execute("DELETE FROM indexs WHERE  num_rom_ca = ?", (num_rom_ca,))
    conn.commit()

"""Query the database"""

def query1(c):
    # 1. Query to count the number of indexs in the table
    c.execute("SELECT COUNT(*) FROM indexs")
    count = c.fetchone()[0]
    print(f"Total number of indexs: {count}")

def query2(c):
    # 2. Query to get Shape_Leng less than 56140
    c.execute("SELECT * FROM indexs WHERE Shape_Leng < ?", (56140,))
    q_indexs = c.fetchall()
    print("indexs have Shape_Leng less than 56140:")
    for i in q_indexs:
        print(f"name_cap_2: {i[0]}, num_rom_ca: {i[1]}, Shape_Leng: {i[2]}, Shape_Area: {i[3]}")
