# backend/load_data.py
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app.models import property
import pandas as pd


def load_data(file_path):
    """
    Load data from an Excel file into the database.
    :param file_path:
    :return:
    """
    Base.metadata.create_all(bind=engine)

    df = pd.read_excel(file_path)

    session = Session(bind=engine)

    if session.query(property.Property).count() == 0:
        for index, row in df.iterrows():
            property_table = property.Property(
                full_address=row["Full Address"],
                class_description=row["CLASS_DESCRIPTION"],
                estimated_market_value=row["ESTIMATED_MARKET_VALUE"],
                building_use=row["BLDG_USE"],
                building_square_feet=row["BUILDING_SQ_FT"],
                latitude=row["Latitude"],
                longitude=row["Longitude"],
            )
            session.add(property_table)
        session.commit()
    else:
        print("Data already loaded.")


if __name__ == "__main__":
    load_data("Enodo_Skills_Assessment_Data_File.xlsx")
