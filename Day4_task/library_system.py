class LibraryItem:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def describe(self) -> str:
        return (
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Year: {self.year}"
        )


class Book(LibraryItem):
    def __init__(self, title: str, author: str, year: int, pages: int):
        super().__init__(title, author, year)
        self.pages = pages

    def describe(self) -> str:
        return (
            f"Book - Title: {self.title}, "
            f"Author: {self.author}, "
            f"Year: {self.year}, "
            f"Pages: {self.pages}"
        )


class EBook(LibraryItem):
    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        file_size_mb: float
    ):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def describe(self) -> str:
        return (
            f"EBook - Title: {self.title}, "
            f"Author: {self.author}, "
            f"Year: {self.year}, "
            f"File Size: {self.file_size_mb} MB"
        )


# Create Book objects
book1 = Book(
    "Python Crash Course",
    "Eric Matthes",
    2019,
    544
)

book2 = Book(
    "Clean Code",
    "Robert C. Martin",
    2008,
    464
)

# Create EBook objects
ebook1 = EBook(
    "Data Science Handbook",
    "Jake VanderPlas",
    2020,
    12.5
)

ebook2 = EBook(
    "Machine Learning Guide",
    "Andrew Ng",
    2023,
    8.7
)

# Store all items in one list
library_items = [book1, book2, ebook1, ebook2]

# Polymorphism: same method call, different behavior
for item in library_items:
    print(item.describe())


# EXPLORE
# isinstance() checks whether an object belongs to a class
# or inherits from that class.

print(isinstance(book1, LibraryItem))
# Output: True

# Explanation:
# Book inherits from LibraryItem.
# Therefore every Book object is also considered
# a LibraryItem object.