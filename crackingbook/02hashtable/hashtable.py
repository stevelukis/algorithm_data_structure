class HashTable:
    def __init__(self):
        table_size = 10
        self.table_size = table_size

        self.data_list = [[] for _ in range(table_size)]

    def _get_index(self, key):
        key_hash = hash(key)
        key_index = key_hash % self.table_size
        return key_index

    def _find_in_parent(self, parent_list, key):
        """
        :param parent_list: The parent list to search
        :param key: The key of the value to find
        :return: None if the data doesn't exist in the parent list,
                 [index, value] if exists where "index" is the index
                 of the item inside parent list, and "value"
                 is the value for the associated key
        """
        for index in range(len(parent_list)):
            node = parent_list[index]
            [i_key, i_value] = node
            if i_key == key:
                return [index, i_value]
        return None

    def remove(self, key):
        key_index = self._get_index(key)
        parent_list = self.data_list[key_index]
        find_result = self._find_in_parent(parent_list, key)

        if find_result is not None:
            [index, _] = find_result
            parent_list.pop(index)

    def put(self, key, value):
        key_index = self._get_index(key)
        parent_list = self.data_list[key_index]
        find_result = self._find_in_parent(parent_list, key)

        if find_result is None:
            parent_list.append([key, value])
        else:
            [index, _] = find_result
            parent_list[index] = [key, value]

    def get(self, key):
        key_index = self._get_index(key)
        parent_list = self.data_list[key_index]

        find_result = self._find_in_parent(parent_list, key)

        if find_result is None:
            return None

        [_, value] = find_result

        return value
