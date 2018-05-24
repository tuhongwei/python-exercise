from sqlalchemy import Column,String,create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
	"""docstring for User"""
	__tablename__ = 'user'
	id = Column(String(20),primary_key = True)
	name = Column(String(20))
	books = relationship('Book')

class Book(Base):
	"""docstring for Book"""
	__tablename__ = 'book'
	id = Column(String(20),primary_key = True)
	name = Column(String(20))
	user_id = Column(String(20),ForeignKey('user.id'))
		
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test') 
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id="4",name="Twittytop")
session.add(new_user)
session.commit()
session.close()		

# 查询
session = DBSession()
user = session.query(User).filter(User.id=="6").one()
print("type",type(user))
print("name:",user.name)
print("name:",user.books)
