#!/usr/bin/env python3
"""
LRU caching system that inherits from BaseCaching.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from BaseCaching.
    It implements a caching algorithm based on the Most Recently Used (MRU)
    principle.
    """

    def __init__(self):
        """
        Initialize the MRUCache.

        Args:
            None.

        Returns:
            None.
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Add an item to the cache using the MRU algorithm.

        Args:
            key: The key of the item.
            item: The value of the item.

        Returns:
            None.

        Notes:
            - If either the key or item is None, this method does nothing.
            - If the number of items in self.cache_data exceeds
            BaseCaching.MAX_ITEMS,
              the most recently used item in the cache is discarded (MRU).
              A "DISCARD: <key>" message is printed indicating the discarded
              key.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the most recently used item (MRU)
            most_recent_key = self.key_order.pop()
            del self.cache_data[most_recent_key]
            print(f"DISCARD: {most_recent_key}")

        self.cache_data[key] = item
        self.key_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key in the cache, or None if the key
            is None or
            if the key does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the key order to reflect the most recent usage
        self.key_order.remove(key)
        self.key_order.append(key)

        return self.cache_data[key]
