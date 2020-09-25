# Example program that modifies database for tests 


## Importing and changing a DB configuration

DB is set in config.py
See notes in tests/test_db.py on importing the database config and changing it for the tests 
The way it is imported, and the order of imports in your tests, matter.

## To run tests

Add a file `__init__.py` in the tests directory 

Run tests with one of these commands 

```python -m unittest discover tests
python -m unittest tests/test_db.py
python -m unittest tests.test_db
```