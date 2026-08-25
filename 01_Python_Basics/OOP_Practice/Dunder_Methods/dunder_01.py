class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):
        return self.pages

    #def __str__(self):
       # return f"this is a book title -> {self.title} //str"

    def __repr__(self):
        return f"this is a book title -> {self.title} //repr"