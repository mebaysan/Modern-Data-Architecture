# Introduction

I created this repo to simulate modern data architecture by using the tools below.

# [Airbyte](https://airbyte.com/)

# [DBT](https://www.getdbt.com/)

- [Source](./Source/) folder is created to provide data for dbt.
- [modern_data_architecture](./modern_data_architecture/) folder is the dbt project for the data provided in [Source](./Source/) folder. The data is from Kaggle by [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

# [Apache Superset](https://superset.apache.org/)

- I have created a sub module in [Superset-Production-Environment](./Superset-Production-Environment/) folder. Also you can visit its original repo by using [here](https://github.com/mebaysan/Superset-Production-Environment). I have created that repo to make easy the set up progress of Superset.
- You have to override the [superset_config.py](./Superset-Production-Environment/superset_config.py) file to run Superset on your local with the [dbt](modern_data_architecture/) project.
- Also, you should add more `RUN pip install <package>` in [Dockerfile](./Superset-Production-Environment/Dockerfile) to install database connectors if you want to use other databases.
- Your Superset database credentials *should be* different than [dbt project](./modern_data_architecture/)'s output database.
