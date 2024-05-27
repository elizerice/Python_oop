class SparseArray:
    def __init__(self):
        self.sparse_dict = {}

  
    def __setitem__(self, key, value):
        self.sparse_dict[key] = value

  
    def __getitem__(self, key):
        return self.sparse_dict.get(key, 0)

