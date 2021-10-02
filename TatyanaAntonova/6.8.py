def main():
    class Pagination():
        pages = {}

        def __init__(self, string, length) -> None:
            self.string = string
            self.length = length
            self.page_count = self.pg_count()
            self.item_count = len(self.string)
            self.pages = self.dict_pages()

        def pg_count(self):
            if len(self.string) % self.length == 0:
                cnt = len(self.string) / self.length
            else:
                cnt = len(self.string) // self.length + 1
            return cnt

        def dict_pages(self):
            i = 0
            for j in range(self.page_count):
                if j != self.page_count - 1:
                    self.pages.update({j: self.string[i: i+self.length]})
                    i += self.length
                else:
                    self.pages.update({j: self.string[i:]})
            return self.pages

        def count_items_on_page(self, page_number):
            if page_number in self.pages.keys():
                return len(self.pages[page_number])
            else:
                raise Exception("Invalid index. Page is missing")

        def find_page(self, s):
            final_res = set()
            starts = [i for i in range(len(self.string)) if self.string.startswith(s, i)]           
            if len(starts) != 0:
                for i in starts:
                    start = (i // self.length)
                    end = ((i+len(s)) // self.length)
                for j in range(start, end+1):
                    final_res.add(j)
                return list(final_res)
            else:
                raise Exception(f"'{s}' is missing on the pages")

        def display_page(self, page):
            return self.pages[page]
        
    
    pages = Pagination('Your beautiful text', 5) # Testing
    print(pages.page_count)
    print(pages.item_count)
    print(pages.pages)
    print(pages.count_items_on_page(0))
    print(pages.count_items_on_page(3))
    #print(pages.count_items_on_page(4))
    print(pages.find_page('Y'))
    print(pages.find_page('r beautiful t'))
    print(pages.display_page(0))



if __name__ == "__main__":
    main()