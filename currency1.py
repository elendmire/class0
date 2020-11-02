import requests


def main():
    base = input("First Currency: ")
    other = input("Second currency: ")
    res = requests.get("http://data.fixer.io/api/latest", 
    params= {"access_key": "652ce75dde647a300747a031338d8216", format: 1, "symbols": other})

    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")

    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")


if __name__ == "__main__":
    main()
