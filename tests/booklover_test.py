import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        book_lover = BookLover("Test Use1r", "asdf@example.com", "Thriller")
        book_lover.add_book("The Hobbit", 5)
        self.assertTrue(book_lover.has_read("The Hobbit"))
    
    def test_2_add_book(self):
        book_lover = BookLover("Test User2", "test3@example.com", "Fantasy")
        book_lover.add_book("The Hobbit", 5)
        book_lover.add_book("The Hobbit", 5)
        self.assertEqual(book_lover.book_list[book_lover.book_list['book_name'] == "The Hobbit"].shape[0], 1)
    
    def test_3_has_read(self):
        book_lover = BookLover("Test User3", "testuser@example.com", "Thriller")
        book_lover.add_book("The Hobbit", 5)
        self.assertTrue(book_lover.has_read("The Hobbit"))
        
    def test_4_has_read(self):
        book_lover = BookLover("Test User4", "xyz@example.com", "Thriller")
        self.assertFalse(book_lover.has_read("1984")) 
        
    def test_5_num_books_read(self):
        book_lover = BookLover("Test User5", "abc@example.com", "Thriller")
        book_lover.add_book("The Hobbit", 5)
        book_lover.add_book("1984", 4)
        self.assertEqual(book_lover.num_books_read(), 2)
    
    def test_6_fav_books(self):
        book_lover = BookLover("Test User6", "test1@example.com", "Fantasy")
        book_lover.add_book("The Hobbit", 5)
        book_lover.add_book("1984", 2) 
        book_lover.add_book("Brave New World", 4)
        fav_books = book_lover.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
        self.assertEqual(fav_books.shape[0], 2)

if __name__ == '__main__':
    unittest.main(verbosity=3)
