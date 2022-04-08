import glob
from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()


engine = create_engine(f"postgresql://{os.getenv('DB_STRING')}")

filenames = glob.glob('*.csv')
for filename in filenames:
    dataset = pd.read_csv(filename)
    dataset.to_sql(
        name=filename, con=engine, schema="public", if_exists="replace"
    )
    print(f'SUCCEED: {filename}')