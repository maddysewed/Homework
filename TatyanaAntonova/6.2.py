def main():
    class HistoryDict():
        def __init__(self, d) -> None:
            self.d = d
            self.buffer = []

        def set_value(self, key, value) -> None:
            self.d.update({key: value})
            if len(self.buffer) < 10:
                self.buffer.append(key)
            else:
                del self.buffer[0]
                self.buffer.append(key)

        def get_history(self):
            return print(self.buffer)

    d = HistoryDict({"foo": 42}) # Testing
    d.set_value("bar", 43)
    d.get_history()
    d.set_value("a", 43)
    d.get_history()
    d.set_value("b", 43)
    d.get_history()

if __name__ == "__main__":
    main()