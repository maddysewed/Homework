def main():
    class Counter():
        def __init__(self, *, start=0, stop=None) -> None:
            self.start = start
            self.stop = stop
            self.value = start

        def increment(self) -> None:
            if self.value != self.stop:
                self.value += 1
            else:
                raise "Maximal value is reached."

        def get(self):
            return print(self.value)

    c = Counter() # Testing
    c.get()
    c.increment()
    c.get()
    c.increment()
    c.get()

if __name__ == "__main__":
    main()