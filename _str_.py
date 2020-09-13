from datetime import datetime
import os


class main():
    def __init__(self):
        # self.name = input('Name:')
        # self.age = int(input('Age:'))
        self.week, self.month, self.date, self.time, self.year = datetime.now().strftime('%c').split()
        self.time = self.time.join('n')

    def __str__(self):
        return f'{self.week} the {self.date}th, {self.year}'


print(main())
