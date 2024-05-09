from databases.database import SessionLocal, engine, Base

from databases.models import Person


def main() -> None:
    try:
        Base.metadata.create_all(bind=engine)

        db_session = SessionLocal()
        print(f"try session active: {db_session.is_active}")

        for person in db_session.query(Person).all():
            print(person)

        natalie_fav_person = (
            db_session.query(Person).filter_by(first_name="Charlie").first()
        )

        print(natalie_fav_person)

    finally:
        db_session.close()
        print(f"finally session active: {db_session.is_active}")


if __name__ == "__main__":
    main()