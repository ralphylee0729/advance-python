from sqlalchemy import Column, Integer, String

from databases.database import Base


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer)

    def __str__(self) -> str:
        return (
            f"<Person Id={self.id}, "
            f"FirstName={self.first_name}, "
            f"LastName={self.last_name}, "
            f"Age={self.age}>"
        )