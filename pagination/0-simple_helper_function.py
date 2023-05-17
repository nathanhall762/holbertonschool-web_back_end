#!/usr/bin/env python3
"""
Calculate the start and end indexes for a given page and page size.
"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of size two containing the start index and end index.
            The start index is inclusive, while the end index is exclusive.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
