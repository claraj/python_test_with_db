from peewee import * 

from config import db_path

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