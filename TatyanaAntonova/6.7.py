from functools import total_ordering

def main():
    @total_ordering
    class Money():
        curr = "USD"
        to_curr = "EUR"

        def get_curr(self):
            import requests
            import json

            url = "https://v6.exchangerate-api.com/v6/38f05964d177a10b07eabfbe/latest/" + self.curr
            r = requests.get(url)
            currs = json.loads(r.text)
            currs = currs["conversion_rates"]
            return currs        

        def __init__(self, summ, curr="USD") -> None:
            self.summ = summ
            self.curr = curr
            self.exchange_rate = self.get_curr()
            self.exchanged = self.convert()

        def convert(self): 
            self.exchanged = self.summ * self.exchange_rate[self.to_curr]
            return self.exchanged

        def __add__(*args):
            s = 0
            for i in args:
                s += i.exchanged
            return Money(s)

        def __sub__(one, other):
            return str(one.exchanged - other.exchanged) + f" {one.to_curr}"

        def __mul__(self, other):
            return str(self.exchanged * other) + f" {self.to_curr}"

        def __div__(self, other):
            if other != 0:
                return str(self.exchanged / other) + f" {self.to_curr}"
            else:
                raise ZeroDivisionError

        def __eq__(self, other):
            return self.exchanged == other.exchanged

        def __lt__(self, other):
            return self.exchanged < other.exchanged

        def __le__(self, other):
            return self.exchanged <= other.exchanged


    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")
    print(z >= y) # result in “EUR”
    print((z + y + x).exchanged) # result in “EUR”
    print(x*2)
    lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
    print(Money.__add__(*lst).exchanged)


if __name__ == "__main__":
    main()