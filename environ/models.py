from peewee import * 

import os 

# Read database location from an environment variable.
try:
    db_path = os.environ['FLOWER_DB_PATH']
except KeyError:
    print("""
An environment variable called FLOWER_DB_PATH must be set containing the location
of the flower database. This file need not exist already, the program will create it.
To set the environment variable, you could use with one of the following,
export FLOWER_DB_PATH="flower.db"    <-- mac or linux
set FLOWER_DB_PATH="flower.db"      <-- PC
Or set the environment variable however you usually do. 
"""
)

# this line is not needed - but used here to help see what's happening when 
# running the code vs testing 
print('Just checking - the database used will be ' + db_path)

db = SqliteDatabase(db_path)

class Flower(Model):
    name = CharField(unique=True)

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name}'

db.connect()
db.create_tables([Flower])

