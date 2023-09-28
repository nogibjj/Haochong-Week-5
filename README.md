# Haochong-week5-mini-repo [![CI](https://github.com/nogibjj/Haochong-Week-5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Haochong-Week-5/actions/workflows/cicd.yml)
This is a repo template for course 706_Data_Engineering Week 5 Mini Project. First of all, I use the same dataset in week 2 since it doesn't have too many columns. Secondly, I define functions called `extract` to get data from url. Then, use `load` to create database. After that, I use `connect` to connect database.  Next, I create the table "indexs" and perform CRUD by `create` `read`, `update_Shape_Leng` and `delete`. I also define a function called `insert` to help me with CRUD. Consequently, I use `main.py` to use my function in `lib.py`, and use the output of `main.py` and `test_main.py` to test my `main.py`. Finally, I use Action to run `Makefile` and got a 100% pass. 

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

3. Test code by using `make test`

In this project, I failed lots of times before I passed all of them. At the beginning, I tried to add a file with `.ipynb` directly in my repo. Nevertheless, it shown as "invalid notebook". After consulting TA, I understanded that we can't use jupyter notebook in this way. Since setting up the environment on github would be redundant, I created a jupyter notebook locally, git clone my repo to local and drag the notebook into my repo then update my repo. Finally, I got vaild notebook.

<img width="169" alt="截屏2023-09-16 上午1 43 18" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/c67ffd16-68ff-450f-9468-464f5b6bccdd">


When I tried to plot the distribution of `TotalConfirmed` by `Date`, after I groupby the dataset by `Date`, I met the second problem: dates were not shown under x-axis. After print the type of Date column, I found out that the type is str. Hence, I use package `datetime` to convert the type into date, then I fixed the problem.

<img width="552" alt="截屏2023-09-16 上午1 52 53" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/563d977d-2618-4620-95b3-2074bfb6e286">


When I tried to do the liner regression, I met the third problem: both date type data and row index are not able to do liner regression. Therefore, I first reset the Date index and then I added a new column into the dataframe as Date index, use that column and `TotalConfirmed` to do liner regression. Finally, I got what I want.

<img width="281" alt="截屏2023-09-16 上午1 54 59" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/bfbcedd3-05f3-4ec3-a928-e9b009abe436">


After fixing all of these, I got all pass.

`test_lib.py` and `test_script.py`:

<img width="653" alt="截屏2023-09-16 上午1 58 01" src="https://github.com/nogibjj/Individual-Project-1/assets/89813704/65e3467c-c17a-48f4-8256-f2edfebe8e91">



