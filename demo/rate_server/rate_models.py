from sqlalchemy import Column, Integer, String, REAL

from rate_server.rate_database import Base

# ,,BGN,CYP,CZK,DKK,EEK,GBP,HUF,LTL,LVL,MTL,PLN,ROL,RON,SEK,SIT,SKK,CHF,ISK,NOK,HRK,RUB,TRL,TRY,AUD,BRL,CAD,CNY,HKD,IDR,ILS,INR,KRW,MXN,MYR,NZD,PHP,SGD,THB,ZAR,

class Rate(Base):
    __tablename__ = "rates"

    Date = Column(String, primary_key=True)
    EUR = Column(REAL, nullable=True)
    USD = Column(REAL, nullable=True)
    JPY = Column(REAL, nullable=True)
    BGN = Column(REAL, nullable=True)
    CYP = Column(REAL, nullable=True)
    CZK = Column(REAL, nullable=True)
    DKK = Column(REAL, nullable=True)
    EEK = Column(REAL, nullable=True)
    GBP = Column(REAL, nullable=True)
    HUF = Column(REAL, nullable=True)
    LTL = Column(REAL, nullable=True)
    LVL = Column(REAL, nullable=True)
    MTL = Column(REAL, nullable=True)
    PLN = Column(REAL, nullable=True)
    ROL = Column(REAL, nullable=True)
    RON = Column(REAL, nullable=True)
    SEK = Column(REAL, nullable=True)
    SIT = Column(REAL, nullable=True)
    SKK = Column(REAL, nullable=True)
    CHF = Column(REAL, nullable=True)
    ISK = Column(REAL, nullable=True)
    NOK = Column(REAL, nullable=True)
    HRK = Column(REAL, nullable=True)
    RUB = Column(REAL, nullable=True)
    TRL = Column(REAL, nullable=True)
    TRY = Column(REAL, nullable=True)
    AUD = Column(REAL, nullable=True)
    BRL = Column(REAL, nullable=True)
    CAD = Column(REAL, nullable=True)
    CNY = Column(REAL, nullable=True)
    HKD = Column(REAL, nullable=True)
    IDR = Column(REAL, nullable=True)
    ILS = Column(REAL, nullable=True)
    INR = Column(REAL, nullable=True)
    KRW = Column(REAL, nullable=True)
    MXN = Column(REAL, nullable=True)
    MYR = Column(REAL, nullable=True)
    NZD = Column(REAL, nullable=True)
    PHP = Column(REAL, nullable=True)
    SGD = Column(REAL, nullable=True)
    THB = Column(REAL, nullable=True)
    ZAR = Column(REAL, nullable=True)

    def __str__(self) -> str:
        return (
            f"<Date={self.Date}, "
            f"USD={self.USD}, "
            f"JPY={self.JPY}, "
            f"BGN={self.BGN}>"
        )