import datetime
from books import Book, BookItem
from library import Library
from models import Address, BookFormat, BookStatus, Person
from users import Member

# STEP 1: Create Address and Person
address = Address("123 Elm St", "Tempe", "AZ", "85281", "USA")
person = Person("Alice Johnson", address, "alice@example.com", "555-1234")

# STEP 2: Create Book and Add Author (as string)
book = Book(
    isbn="9780451524935",
    title="1984",
    subject="Dystopian",
    publisher="Secker & Warburg",
    language="English",
    number_of_pages=328,
    book_format=BookFormat.PAPERBACK
)
book._authors.append("George Orwell")

# STEP 3: Create BookItem (physical copy of the book)
book_item = BookItem(
    id="BOOK1",
    book=book,
    is_reference_only=False,
    borrowed=False,
    due_date=None,
    price=10.99,
    status=BookStatus.AVAILABLE,
    date_of_purchase=datetime.date.today(),
    publication_date=datetime.date(1949, 6, 8),
    placed_at=None
)

# STEP 4: Get Library instance and add the BookItem
library = Library.get_instance()
library.add_book_item(book_item)

# STEP 5: Register Member
member = Member(id="M1", password="secure123", person=person)

# STEP 6: Member checks out the book
print("\n--- Checkout Book ---")
member.checkout_book_item(book_item)

# STEP 7: Force the lending to be overdue by 5 days
lending = library.get_lending("BOOK1")
lending._due_date = datetime.date.today() - datetime.timedelta(days=5)

# STEP 8: Check for fine
print("\n--- Check Fine ---")
member.check_for_fine("BOOK1")

# STEP 9: Member returns the book
print("\n--- Return Book ---")
member.return_book_item(book_item)

# STEP 10: Search via Catalog
print("\n--- Search by Author ---")
results = library.get_catalog().search_by_author("George Orwell")
for item in results:
    print(f"Found BookItem ID: {item.id}, Title: {item.get_book()._title}")
