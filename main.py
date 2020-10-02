import requests


def main():
    response = requests.get("https://reqres.in/api/users?page=2")
    print(response.json())


main()
