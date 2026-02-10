from utils.csv_utils import json_to_csv
from graph import fetch_users

def main():  
    data = fetch_users()
    json_to_csv(data["value"])
    

if __name__ == "__main__":
    main()