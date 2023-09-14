#!/usr/bin/env python3
"""Write a function named index_range that
takes two integer arguments page and page_size.

The function should return a tuple of size
two containing a start index and an end index
corresponding to the range of indexes to return
in a list for those particular pagination parameters.

Page numbers are 1-indexed,
i.e. the firstpage is page 1."""
import csv
import math
from typing import List
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


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Tuple with start index and end index for pagination """
    return ((page - 1) * page_size, page * page_size)
