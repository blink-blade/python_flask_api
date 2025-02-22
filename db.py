import requests
from sqlalchemy import *
from sqlalchemy.orm import *


engine = create_engine('sqlite:///OHYEAH.db')

Session = sessionmaker(bind=engine)
db_session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Base.metadata.create_all(engine)


# user1 = User(name='Jimmy', email='Jimmy@gmail.com', password='12345')
# user2 = User(name='John', email='John@gmail.com', password='123')
# user3 = User(name='Jeorge', email='Jeorge@gmail.com', password='1234567890')
# db_session.add(user1)
# db_session.add(user2)
# db_session.add(user3)
# db_session.commit()


# for user in db_session.query(User).all():
#     db_session.delete(user)
#     print(user)
# db_session.commit()

