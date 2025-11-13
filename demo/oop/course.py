class Course:
    # Static attribute or class attribute
    taxrate = 12

    def __init__(self, title: str, duration: int, fee: int):
        # Object attributes
        self.title = title
        self.duration = duration
        self.fee = fee

    def show(self):
        print('Title    :', self.title)
        print('Duration :', self.duration)
        print('Fee      :', self.fee)

    def net_fee(self):
        tax = (Course.taxrate / 100) * self.fee
        return self.fee + tax

    @staticmethod
    def gettaxrate():
        return Course.taxrate




c1 = Course("Python Programming", 10, 10000)
c1.show()
print(c1.net_fee())
print(Course.gettaxrate())
