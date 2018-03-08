from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    title = Column(String(100))
    href = Column(String(100))


engine = create_engine('mysql+mysqlconnector://root:root@localhost/py')
DBSession = sessionmaker(bind=engine)
