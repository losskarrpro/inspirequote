import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inspirequote.core import Quote, QuoteManager

class TestQuote(unittest.TestCase):
    def test_quote_creation(self):
        """Test creation of a Quote object."""
        quote = Quote("Test text", "Test author")
        self.assertEqual(quote.text, "Test text")
        self.assertEqual(quote.author, "Test author")

    def test_quote_representation(self):
        """Test the string representation of a Quote."""
        quote = Quote("Life is great", "John Doe")
        expected_repr = "Life is great — John Doe"
        self.assertEqual(str(quote), expected_repr)

    def test_quote_to_dict(self):
        """Test conversion of Quote to dictionary."""
        quote = Quote("Hello World", "Jane Doe")
        expected_dict = {"text": "Hello World", "author": "Jane Doe"}
        self.assertEqual(quote.to_dict(), expected_dict)

    def test_quote_from_dict(self):
        """Test creation of Quote from dictionary."""
        data = {"text": "Python is fun", "author": "Guido"}
        quote = Quote.from_dict(data)
        self.assertIsInstance(quote, Quote)
        self.assertEqual(quote.text, "Python is fun")
        self.assertEqual(quote.author, "Guido")

class TestQuoteManager(unittest.TestCase):
    def setUp(self):
        """Set up a QuoteManager with sample quotes for testing."""
        self.manager = QuoteManager()
        self.sample_quotes = [
            Quote("The only way to do great work is to love what you do.", "Steve Jobs"),
            Quote("Innovation distinguishes between a leader and a follower.", "Steve Jobs"),
            Quote("Life is what happens to you while you're busy making other plans.", "John Lennon")
        ]
        for q in self.sample_quotes:
            self.manager.add_quote(q)

    def test_add_quote(self):
        """Test adding a new quote."""
        initial_count = len(self.manager.quotes)
        new_quote = Quote("Test quote", "Test Author")
        self.manager.add_quote(new_quote)
        self.assertEqual(len(self.manager.quotes), initial_count + 1)
        self.assertIn(new_quote, self.manager.quotes)

    def test_remove_quote_by_index(self):
        """Test removing a quote by index."""
        initial_count = len(self.manager.quotes)
        quote_to_remove = self.manager.quotes[1]
        self.manager.remove_quote_by_index(1)
        self.assertEqual(len(self.manager.quotes), initial_count - 1)
        self.assertNotIn(quote_to_remove, self.manager.quotes)

    def test_remove_quote_by_index_invalid(self):
        """Test removing a quote with an invalid index."""
        initial_count = len(self.manager.quotes)
        with self.assertRaises(IndexError):
            self.manager.remove_quote_by_index(10)
        self.assertEqual(len(self.manager.quotes), initial_count)

    def test_get_random_quote(self):
        """Test retrieving a random quote."""
        random_quote = self.manager.get_random_quote()
        self.assertIsInstance(random_quote, Quote)
        self.assertIn(random_quote, self.manager.quotes)

    def test_get_random_quote_empty(self):
        """Test retrieving a random quote from an empty manager."""
        empty_manager = QuoteManager()
        random_quote = empty_manager.get_random_quote()
        self.assertIsNone(random_quote)

    def test_get_all_quotes(self):
        """Test retrieving all quotes."""
        all_quotes = self.manager.get_all_quotes()
        self.assertEqual(len(all_quotes), len(self.sample_quotes))
        for q in self.sample_quotes:
            self.assertIn(q, all_quotes)

    def test_clear_quotes(self):
        """Test clearing all quotes."""
        self.manager.clear_quotes()
        self.assertEqual(len(self.manager.quotes), 0)

    def test_quote_count(self):
        """Test getting the count of quotes."""
        self.assertEqual(self.manager.quote_count(), len(self.sample_quotes))

if __name__ == '__main__':
    unittest.main()