# Source

This folder created to set up database with the data downloaded from Kaggle:

[https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

`script.py` file reads all CSV files downloaded from the link above and then writes to the database which is its credentials given in `.env` file. An example `.env` file is given below.

```bash
DB=BrazilianEcommerce
DB_USER=postgres
DB_PASSWORD=1234
DB_HOST=127.0.0.1
DB_PORT=5432
DB_STRING=${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB}
```

So, if you want to execute `script.py`, you have to be downloaded the data from the source given above.
