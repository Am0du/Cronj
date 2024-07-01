import requests
import time

def hit_endpoint():
    url = 'https://hngg1-latest.onrender.com/api/hello?visitor_name=David'
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Response Status: {response.status_code}")
        print(f"Response Content: {response.content}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def main():
    interval = 1 * 60  # 10 minutes in seconds
    while True:
        hit_endpoint()
        print(f"Waiting for {interval} seconds before the next request...")
        time.sleep(interval)

if __name__ == '__main__':
    main()
