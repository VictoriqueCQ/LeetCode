import random
class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.v = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.v.append(val)
        return val not in self.v[: -1]

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.v:
            return False
        self.v.remove(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.v)

