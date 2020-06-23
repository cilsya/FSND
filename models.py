import os
from sqlalchemy import Column, Integer, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

# https://knowledge.udacity.com/questions/88219
# In windows console, set the environment
# set DATABASE_URL='postgres://...'
#database_path = os.environ['DATABASE_URL']
#database_path = "postgresql://postgres:abcd1234@localhost:5432/herokusample"

# AN ALTERNATIVE
# https://knowledge.udacity.com/questions/217605
#default_path=postgres://postgres:postgres@localhost:5432/default_database_path
#database_path=os.getenv('DATABASE_URL', default_path)
default_path='postgresql://postgres:abcd1234@localhost:5432/herokusample'
database_path=os.getenv('DATABASE_URL', default_path)


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}