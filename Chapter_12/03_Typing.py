from typing import List, Tuple, Dict, Union

# Using type hints for various data structures
numbers: List[int] = [1, 2, 3, 4, 5]  # A list of integers

person: Tuple[str, int] = ("Alice", 30)  # A tuple containing a string and an integer

scores: Dict[str, int] = {"Alice": 90, "Bob": 85}  # A dictionary with string keys and integer values

identifier: Union[int, str] = "ID123"  # Variable can hold either an int or a str
identifier = 12345  # Reassigned to an integer, also valid
