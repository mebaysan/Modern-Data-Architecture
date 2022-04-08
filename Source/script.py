import glob
from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()


engine = create_engine(f"postgresql://{os.getenv('DB_STRING')}")

engine.execute("""
                CREATE SCHEMA IF NOT EXISTS ecommerce
                """)

filenames = glob.glob('*.csv')
for filename in filenames:
    dataset_name = filename.split('_dataset')[0]
    dataset = pd.read_csv(filename)
    dataset.to_sql(
        name=dataset_name, con=engine, schema="ecommerce", if_exists="replace"
    )
    print(f'SUCCEED: {filename} -> {dataset_name}')