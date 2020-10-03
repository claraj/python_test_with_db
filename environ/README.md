# Example program that modifies database for tests 


## Importing and changing a DB configuration

The DB path is stored in an environment variable called FLOWER_DB_PATH.
When the program runs, it reads this value and uses it to locate the database.

In the tests, the python dotenv library is used to temporarily replace the value of FLOWER_DB_PATH with the location of a test database.

The environment variable is stores in a file called .env. 

Install dotenv with 

pip install python-dotenv

Documetation: https://github.com/theskumar/python-dotenv

## To run tests

Add a file `__init__.py` in the tests directory 

Run a specific test file with one of these commands 

```python -m unittest discover tests
python -m unittest tests/test_db.py
python -m unittest tests.test_db
```

Or run all the tests in a directory with the discover option

```python -m unittest discover tests```