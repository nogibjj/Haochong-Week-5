# Haochong-week5-mini-repo [![CI](https://github.com/nogibjj/Haochong-Week-5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Haochong-Week-5/actions/workflows/cicd.yml)
This is a repo template for course 706_Data_Engineering Week 5 Mini Project. First of all, I use the same dataset in week 2 since it doesn't have too many columns. Secondly, I define functions called `extract` to get data from url. Then, use `load` to create database. After that, I use `connect` to connect database.  Next, I create the table "indexs" and perform CRUD by `create`, `read`, `update_Shape_Leng` and `delete`. I also define a function called `insert` to help me with CRUD. Consequently, I use `main.py` to use my function in `lib.py`, and use the output of `main.py` and `test_main.py` to test my `main.py`. Finally, I use Action to run `Makefile` and got a 100% pass. 

Important file:
* `Makefile`
* `lib.py`
* `main.py`
* `25ktopomapseriesindex.csv`
* `ktopomapseriesindexDB.db`
* `test_main.py`

# Purpose
- Connect to a SQL database
- Perform CRUD operations
- Write at least two different SQL queries

## Preparation 
1. open codespaces and vscode
2. wait for container to be built with requiremnts.txt installed

## Check format and test errors
1. Format code with Python black by using `make format`

2. Lint code with Ruff by using `make lint`. 

Got single line too long for some files, which is easy to fix.

![Alt text](<截屏2023-09-28 下午1.14.01.png>)

3. Test code by using `make test`

In this project, I got the first failure while creating database. I use the name of my csv file directly and got this:

![Alt text](<截屏2023-09-27 下午11.54.39.png>)

I was confused at first, and you can see I create several ways but all failed. After google this I noticed that it was because I use the number as the fisrt letter of my database, which is not allowed. I fixed this by delete "25".


I didn't meet too many trouble for other parts.

I first use `connect` to connect to my database:

### connect
```python
def connect():
    conn = sqlite3.connect('ktopomapseriesindexDB.db')
    c = conn.cursor()
    return c, conn
```

For the "CRUD" part:

### create
```python
def create():
    c.execute('''CREATE TABLE IF NOT EXISTS indexs (
            name_cap_2 TEXT,
            num_rom_ca TEXT PRIMARY KEY,
            Shape_Leng INTEGER,
            Shape_Area INTEGER
        )''')
```

### read
```python
def read(c):
    c.execute("SELECT * FROM indexs")
    indexs = c.fetchall()
    return indexs
```

### update (for Shape_Leng, same for other columns)
```python
def update_Shape_Leng(c, conn, Shape_Leng, num_rom_ca):
    c.execute("UPDATE indexs SET Shape_Leng = ? WHERE  num_rom_ca = ?", 
              (Shape_Leng, num_rom_ca))
    conn.commit()
```

### delete
```python
def delete(c, conn, num_rom_ca):
    c.execute("DELETE FROM indexs WHERE  num_rom_ca = ?", (num_rom_ca,))
    conn.commit()
```

For the two queries:
### query1
```python
def query1(c):
    # 1. Query to count the number of indexs in the table
    c.execute("SELECT COUNT(*) FROM indexs")
    count = c.fetchone()[0]
    print(f"Total number of indexs: {count}")
```

### query2
```python
def query2(c):
    # 2. Query to get Shape_Leng less than 56140
    c.execute("SELECT * FROM indexs WHERE Shape_Leng < ?", (56140,))
    q_indexs = c.fetchall()
    print("indexs have Shape_Leng less than 56140:")
    for i in q_indexs:
        print(f"""name_cap_2: {i[0]}, 
              num_rom_ca: {i[1]}, 
              Shape_Leng: {i[2]}, 
              Shape_Area: {i[3]}""")
```


For the test, I didn't test for function like `connect`, since they are just for the connection. If they can't work, all other part won't be able to run, which means they are definitely fine.

I write test in `test_main.py` for CRUD functions. I use function`fetchone()` to fetch the row I want, and then compare the result with `None` to see whether the operation happened. I got them all pass:



![Alt text](<截屏2023-09-28 下午1.15.28.png>)


