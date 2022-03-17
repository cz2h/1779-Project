import requests

TIMEOUT_IN_SECONDS = 1


def post(url, data=None):
    try:
        res = requests.post(url, data=data, time=TIMEOUT_IN_SECONDS)
        return res
    except TimeoutError as e:
        print(f'{url}: Timeout')
        print(e)
        return False
    except Exception as e:
        print(e)
        return False
