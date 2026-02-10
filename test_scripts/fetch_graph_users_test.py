from graph import fetch_users

def main():
    res_json = fetch_users()
    print("fetching users from graph")
    print("users->")
    print(res_json)


if __name__ == "__main__":
    main()