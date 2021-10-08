import unittest
from hashtable import HashTable


class HashTableTest(unittest.TestCase):

    def setUp(self):
        hashtable = HashTable()
        self.hashtable = hashtable

    def put1(self):
        key = "key1"
        value = "value1"
        self.key1 = key
        self.value1 = value
        hashtable = self.hashtable
        hashtable.put(key, value)

    def put2(self):
        key = "key2"
        value = "value2"
        self.key2 = key
        self.value2 = value
        hashtable = self.hashtable
        hashtable.put(key, value)

    def put3(self):
        key = "key3"
        value = "value3"
        self.key3 = key
        self.value3 = value
        hashtable = self.hashtable
        hashtable.put(key, value)

    def test_put(self):
        self.put1()
        self.put2()
        self.put3()

        hashtable = self.hashtable
        self.assertEqual(hashtable.get(self.key1), self.value1)
        self.assertEqual(hashtable.get(self.key2), self.value2)
        self.assertEqual(hashtable.get(self.key3), self.value3)

    def test_replace(self):
        self.put1()

        hashtable = self.hashtable
        key1 = self.key1

        new_value = self.value1 + "111"
        hashtable.put(key1, new_value)

        self.assertEqual(hashtable.get(key1), new_value)

    def test_remove(self):
        self.put1()

        hashtable = self.hashtable
        key1 = self.key1

        self.assertEqual(hashtable.get(self.key1), self.value1)

        hashtable.remove(key1)
        self.assertIsNone(hashtable.get(self.key1))