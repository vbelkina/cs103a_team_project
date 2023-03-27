# TRACKER PA03

## App Description 

This app will create two SQL tables - tracker and categories and run a variety of functions:

            type quit (description: to end the program)
            type showall_categories (description: show all categories)
            type add_category (description: to add a new category)
            type modify_category (description: to modify a category)
            type showall_transactions (description: for all transactions)
            type add_transaction amount category date description (description: to add a new transaction)
            type delete_transaction item# (description: to delete a new transaction)
            type sum_transactions_date date (description: summarizes transactions on the given date in the format yyyy-mm-dd)
            type sum_transactions_month month (description: summarizes transactions in the given month in the format yyyy-mm)
            type sum_transactions_year year (description: summarizes transactions in the given year in the format yyyy)
            type sum_transactions_category category (description: summarizes transactions of the given category)
            type print_usage (description: to print this message)

## Pylint

## Pytest
```
=========================================== test session starts ================================================
platform linux -- Python 3.8.10, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/nika/Documents/Brandeis/S4/FundamentalsOfSE/cs103a_team_project/pa03
plugins: anyio-3.6.2
collected 7 items                                                                                                                                                                         

test_transcation.py .......                                                                                                                                                         [100%]

============================================= 7 passed in 0.09s =================================================
```
## Tracker.py
************* Module tracker
tracker.py:97:0: C0301: Line too long (104/100) (line-too-long)
tracker.py:68:0: R0912: Too many branches (15/12) (too-many-branches)
tracker.py:133:12: R1723: Unnecessary "elif" after "break" (no-else-break)

------------------------------------------------------------------
Your code has been rated at 9.72/10 (previous run: 9.63/10, +0.09)