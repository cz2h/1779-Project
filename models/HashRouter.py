import hashlib


class HashRouter:

    def __init__(self, caches_url=None):
        if caches_url is None:
            caches_url = []
        self.caches_url = caches_url

    def get_cache_node_url(self, key):
        md5_hex = hashlib.md5(key.encode('utf-8')).hexdigest()
        cache_index = int(md5_hex, 16) % len(self.caches_url)
        return self.caches_url[cache_index]

    def set_caches(self, new_caches):
        self.caches_url = new_caches
