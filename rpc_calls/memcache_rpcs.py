from config.Config import DevConfig
import requests


def call_put(key, value):
    url = DevConfig.MEMCACHE_SERVER + DevConfig.END_POINTS['put']
    data = {
        "key": key,
        "value": value
    }
    res = requests.post(url, data=data)
    return res.json()


def call_get(key):
    url = DevConfig.MEMCACHE_SERVER + DevConfig.END_POINTS['get']
    data = {
        "key": key,
    }
    res = requests.post(url, data=data)
    return res.json()


def call_clear():
    url = DevConfig.MEMCACHE_SERVER + DevConfig.END_POINTS['clear']
    res = requests.post(url)
    return res.json()


def call_invalidate_key(key):
    url = DevConfig.MEMCACHE_SERVER + DevConfig.END_POINTS['invalidatekey']
    data = {
        "key": key,
    }
    res = requests.post(url, data=data)
    return res.json()


def call_refresh_configuartion():
    url = DevConfig.MEMCACHE_SERVER + DevConfig.END_POINTS['refreshconfiguration']
    res = requests.post(url)
    return res.json()
