# main.py
from dataverse import list_accounts,list_test_1,find_test_table
from auth import whoami
import asyncio

def main():
    rows = list_test_1()
    print(len(rows))
    print(rows[0])
    print(rows[::20])
 
if __name__ == "__main__":
    main()
