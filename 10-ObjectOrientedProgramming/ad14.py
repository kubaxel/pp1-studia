class Ebook():
    def __init__(self):
        self.title="hary poter"
        self.author='marek mostowiak'
        self.pages_no=500
        self.opened=False
        self.current_page=0

    def ebook_open(self):
        self.opened=True
    
    def ebook_close(self):
        self.opened=False
    
    def next_page(self):
        if self.opened:
            self.current_page=+1
        else:
            print('The book is closed you can not change pages')

    def previous_page(self):
        if self.opened:
            self.current_page-=1
        else:
            print('The book is closed you can not change pages')

    def ebook_info(self):
        print(f'The book title is: {self.title}\nThe book author is: {self.author}\nThe book number of pages is {self.pages_no}\nThe book current page is: ')

a=Ebook()