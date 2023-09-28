"""
ETL-Query script
"""

from mylib.lib import extract
from mylib.lib import load
from mylib.lib import connect
from mylib.lib import create
from mylib.lib import insert
from mylib.lib import read
from mylib.lib import update_Shape_Leng
from mylib.lib import delete
from mylib.lib import query1
from mylib.lib import query2

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

if __name__ == "__main__":
    c, conn = connect()
    create(c)


       # CRUD operations
    insert(c, conn, "B", "keyb", 2, 2)
    insert(c, conn, "A", "key", 1, 1)
    
    print("Data after insertions:")
    indexs = read(c)
    for i in indexs:
        print(f"name_cap_2: {i[0]}, num_rom_ca: {i[1]}, Shape_Leng: {i[2]}, Shape_Area: {i[3]}")
    
    update_Shape_Leng(c, conn, 1, "I-NE")
    
    print("Data after updating I-NE's Shape_Leng:")
    indexs = read(c)
    for i in indexs:
        print(f"name_cap_2: {i[0]}, num_rom_ca: {i[1]}, Shape_Leng: {i[2]}, Shape_Area: {i[3]}")
    
    delete(c, conn, "I-SE")
    
    print("Data after deleting I-SE:")
    indexs = read(c)
    for i in indexs:
        print(f"name_cap_2: {i[0]}, num_rom_ca: {i[1]}, Shape_Leng: {i[2]}, Shape_Area: {i[3]}")

    # Query
    print("Querying data...")
    query1(c)
    query2(c)
    conn.close()

