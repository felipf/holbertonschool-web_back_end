#!/usr/bin/env python3
"""Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing
the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page,
None if no previous page
total_pages: the total number of pages
in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary."""
import csv
import math
from typing import List, Dict
import math
from typing import Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        "get_page() method of Server class"
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indexes = index_range(page, page_size)
        first = indexes[0]
        last = indexes[1]

        return self.dataset()[first:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        "get_hyper() method for Server class"
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page + 1 < total_pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Tuple with start index and end index for pagination """
    return ((page - 1) * page_size, page * page_size)
