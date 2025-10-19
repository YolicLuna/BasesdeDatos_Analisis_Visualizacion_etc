from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine("postgresql://postgres:aqui_tu_contraseña@localhost/orm")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key = True)
    username = Column(String(50), nullable = False, unique = True)
    email = Column(String(50), nullable = False, unique = True)
    created_at = Column(DateTime(), default = datetime.now())

    def __str__(self):
        return self.username

Session = sessionmaker(engine)
session = Session()

if __name__ == "__main__":

    session.query(User).filter(
        User.id == 1
    ).delete()

    session.commit()