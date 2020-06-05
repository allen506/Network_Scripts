import requests

url = "https://www.google.com"
#url = "http://144.77.43.85:8000/services/cusip/GetActiveAttributes?ssm_id=01F030660&deletecache=1"
limit = int(input("Enter number of connections: "))


def check_conn_pimco(url):
    try:
        r = requests.head(url)
        print(r.status_code)
    except requests.ConnectionError:
        print("failed to connect")


for i in range(limit):
    check_conn_pimco(url)