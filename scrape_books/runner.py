from bookscraper import BookScraper

with BookScraper() as book_s:
    book_s.land_first_page()
    book_s.get_price_of_book("The Black Maria")
