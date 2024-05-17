class Date:

  
    def __init__(self, month, day):
        self.month = month
        self.day = day

  
    def __sub__(self, other):
        days_in_month = [31, 28, 30]
        days = 0
      
        if self.month == other.month:
            days = abs(self.day - other.day)
          
        else:
            start_month = min(self.month, other.month)
            end_month = max(self.month, other.month)
            days = days_in_month[start_month - 1] - self.day

            for i in range(start_month, end_month - 1):
                days += days_in_month[i]
            days += other.day

        if self.month > other.month:
            return days
        else:
            return -days
