class ReversedList:

    def __init__(self, first_lst):
        self.first_lst = first_lst

  
    def __len__(self):
        return len(self.first_lst)

  
    def __getitem__(self, index):
        return self.first_lst[-1 - index]
