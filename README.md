# POC to process big data in a pipeline of transformations

## run
    To run open install all dependencies and
    type "python 1_cleanup_trans\main.py <year:int>" in a command prompt.

    The first script calls the second, the second calls the third asynchronous for each month, and the third calls the forth.

## steps (tasks):
- 1_cleanup_trans: deletes all transactions and reports over its data from big data database;

- 2_get_trans: get transactions from transactions read only database (entity db);

- 3_calculate_monthly_amount: calculates the monthly amount for each month and save into "trans_monthly_amount" report collection;

- 4_calculate_monthly_taxes_amount: calculate the monthly taxes, calling "taxes_api", for the month and save into "trans_monthly_taxes_amount" collection.


## taxes_api
    A simple API that expose a GET route to return the claculated taxes over amount for the month. Is called on step 4 to calculate monthly taxes.

## docs
    Diagram source and another documentions and notes

## data
    A database filled with transactions is mandatory to run this project. For confidentiality reasons, this data was not sent to GitHub.
