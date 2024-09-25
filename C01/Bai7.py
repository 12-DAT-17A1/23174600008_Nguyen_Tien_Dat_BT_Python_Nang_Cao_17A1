from datetime import datetime, timedelta

class Date:
    def __init__(self,day,month,year):
        self.day = day 
        self.month = month 
        self.year = year
    def display(self):
        print(f"Ngày: {self.day}/{self.month}/{self.year}")
    def next_day(self):
        today = datetime.strptime(f'{self.day}/{self.month}/{self.year}','%d/%m/%Y')
        date = today  + timedelta(days=1)
        print(f'Ngày tiếp theo: {date.day}/{date.month}/{date.year}')
    
    
date = Date(day=23,month=9,year=2024)
date.display()
date.next_day()