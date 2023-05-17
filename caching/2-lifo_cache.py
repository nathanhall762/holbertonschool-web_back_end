#!/usr/bin/env python3
"""
LIFOCache is a caching system that inherits from BaseCaching.
It implements a caching algorithm based on the Last-In-First-Out (LIFO)
principle.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that inherits from BaseCaching.
    It implements a caching algorithm based on the Last-In-First-Out (LIFO)
    principle.
    """

    def __init__(self):
        """
        Initialize the LIFOCache.

        Args:
            None.

        Returns:
            None.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using the LIFO algorithm.

        Args:
            key: The key of the item.
            item: The value of the item.

        Returns:
            None.

        Notes:
            - If either the key or item is None, this method does nothing.
            - If the number of items in self.cache_data exceeds
            BaseCaching.MAX_ITEMS,
            the last item put in the cache is discarded (LIFO).
            A "DISCARD: <key>" message is printed indicating the discarded
            key.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the last item put in cache (LIFO)
            last_key = next(reversed(self.cache_data))
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

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

        return self.cache_data[key]
