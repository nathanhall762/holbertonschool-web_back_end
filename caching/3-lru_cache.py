#!/usr/bin/env python3
"""
LRU caching system that inherits from BaseCaching.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize an instance of the LRUCache class.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value for the key
        key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS,
        the least recently used item is discarded (LRU algorithm).
        DISCARD: with the key discarded is printed and followed by a new line.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                lru_key = self.queue.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
        self.queue = [key] + [q for q in self.queue if q != key]
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return
        None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.queue = [key] + [q for q in self.queue if q != key]
        return self.cache_data[key]
