#!/usr/bin/env python3
"""
This module defines the BasicCache class, which is a caching system that
inherits from BaseCaching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching.
    It provides a basic implementation of a cache with no size limit.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The value of the item.

        Returns:
            None.

        Notes:
            If either the key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return
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
