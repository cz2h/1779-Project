class MemcacheStat:
    def __init__(self, data):
        mappings = [
            'num_items',
            'total_size',
            'num_requests',
            'mis_rate',
            'hit_rate']
        self.data = {}
        for i in range(len(mappings)):
            self.data[mappings[i]] = data[i]

    def to_json(self):
        return self.data