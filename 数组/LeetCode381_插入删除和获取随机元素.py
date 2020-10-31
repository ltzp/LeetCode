import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.store:
            self.store.append(val)
            return True
        else:
            self.store.append(val)
            return False


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.store:
            self.store.remove(val)
            return True
        else:
            return False



    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        length = len(self.store)
        return self.store[random.randint(0, length - 1)]
