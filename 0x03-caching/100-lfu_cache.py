#!/usr/bin/python3
""" LFUCache module """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - overwrite functions of BaseCaching
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.keys = []
        self.count = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.keys:
                self.keys.remove(key)
                self.count[key] += 1
            elif len(self.keys) >= self.MAX_ITEMS:
                min_count = min(self.count.values())
                min_keys = [k for k, v in self.count.items() if v == min_count]
                for k in min_keys:
                    if k in self.keys:
                        print("DISCARD: {}".format(k))
                        del self.cache_data[k]
                        self.keys.remove(k)
                        del self.count[k]
                        break
            self.keys.append(key)
            self.cache_data[key] = item
            if key not in self.count:
                self.count[key] = 0

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.count[key] += 1
            self.keys.append(key)
            return self.cache_data[key]
        return None
