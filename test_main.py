"""
Test goes here

"""

from mylib.lib import extract
from mylib.lib import load
from mylib.lib import connect
from mylib.lib import create
from mylib.lib import read
from mylib.lib import query1
from mylib.lib import query2
from mylib.lib import insert
from mylib.lib import update_Shape_Leng
from mylib.lib import delete

def test_extract():
    extract()

def test_load():
    load()

def test_connect():
    c, conn = connect()
    return c, conn

def test_create():
    create(c)

def test_insert():
    insert(c, conn, "A", "key", 1, 1)
    query = """
        SELECT * 
        FROM indexs 
        WHERE 
            name_cap_2 = ? AND
            num_rom_ca = ? AND
            Shape_Leng = ? AND
            Shape_Area = ?
    """

    # Execute the query with the provided data
    c.execute(query, ('A', 'key', 1, 1))

    # Fetch the result
    result = c.fetchone()
    assert result is not None

def test_read():
    read(c)

def test_update_Shape_Leng():
    insert(c, conn, "c", "keyc", 3, 3)
    update_Shape_Leng(c, conn, 4, "keyc")
    query = """
        SELECT * 
        FROM indexs 
        WHERE 
            name_cap_2 = ? AND
            num_rom_ca = ? AND
            Shape_Leng = ? AND
            Shape_Area = ?
    """

    # Execute the query with the provided data
    c.execute(query, ('c', 'keyc', 4, 3))

    # Fetch the result
    result = c.fetchone()
    print("update:")
    print(result)
    assert result is not None

def test_delete():
    insert(c, conn, "B", "keyb", 2, 2)
    delete(c, conn, "keyb")
    data_to_check = {
        'name_cap_2': 'B',
        'num_rom_ca': 'keyb',
        'Shape_Leng': 2,
        'Shape_Area': 2
    }
    query = """
        SELECT * 
        FROM indexs 
        WHERE 
            name_cap_2 = ? AND
            num_rom_ca = ? AND
            Shape_Leng = ? AND
            Shape_Area = ?
    """

    # Execute the query with the provided data
    c.execute(query, ('B', 'keyb', 2, 2))

    # Fetch the result
    result = c.fetchone()
    assert result is None

def test_query1():
    query1(c)

def test_query2():
    query2(c)

if __name__ == "__main__":
    test_extract()
    test_load()
    c, conn = test_connect()
    test_create()
    test_insert()
    test_read()
    test_update_Shape_Leng()
    test_delete()
    test_query1()
    test_query2()
    conn.close()
    print("All passed!")
