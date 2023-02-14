#!/usr/bin/python3
""" FIFO caching module """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - overwrite functions of BaseCaching
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.keys:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                print("DISCARD: {}".format(self.keys[0]))
                del self.cache_data[self.keys[0]]
                self.keys.pop(0)
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
