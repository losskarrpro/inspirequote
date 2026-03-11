import json
import os
import tempfile
import unittest
from unittest.mock import patch, mock_open
from inspirequote.storage import StorageManager


class TestStorageManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_quotes.json")
        self.storage = StorageManager(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        os.rmdir(self.temp_dir)

    def test_init_creates_file_if_not_exists(self):
        new_file = os.path.join(self.temp_dir, "new_quotes.json")
        storage = StorageManager(new_file)
        self.assertTrue(os.path.exists(new_file))
        with open(new_file, 'r') as f:
            content = json.load(f)
        self.assertEqual(content, [])
        os.remove(new_file)

    def test_load_quotes_empty_file(self):
        quotes = self.storage.load_quotes()
        self.assertEqual(quotes, [])

    def test_load_quotes_with_data(self):
        test_data = [
            {"text": "Test quote 1", "author": "Author 1"},
            {"text": "Test quote 2", "author": "Author 2"}
        ]
        with open(self.test_file, 'w') as f:
            json.dump(test_data, f)
        quotes = self.storage.load_quotes()
        self.assertEqual(quotes, test_data)

    def test_load_quotes_file_not_found(self):
        os.remove(self.test_file)
        quotes = self.storage.load_quotes()
        self.assertEqual(quotes, [])

    def test_load_quotes_invalid_json(self):
        with open(self.test_file, 'w') as f:
            f.write("invalid json")
        quotes = self.storage.load_quotes()
        self.assertEqual(quotes, [])

    def test_save_quotes(self):
        test_data = [
            {"text": "Save test 1", "author": "Author A"},
            {"text": "Save test 2", "author": "Author B"}
        ]
        self.storage.save_quotes(test_data)
        with open(self.test_file, 'r') as f:
            saved_data = json.load(f)
        self.assertEqual(saved_data, test_data)

    def test_save_quotes_io_error(self):
        with patch('builtins.open', side_effect=IOError("Permission denied")):
            with self.assertRaises(IOError):
                self.storage.save_quotes([{"text": "test", "author": "test"}])

    def test_add_quote(self):
        initial_quotes = [
            {"text": "Existing quote", "author": "Existing Author"}
        ]
        with open(self.test_file, 'w') as f:
            json.dump(initial_quotes, f)
        new_quote = {"text": "New quote", "author": "New Author"}
        self.storage.add_quote(new_quote)
        with open(self.test_file, 'r') as f:
            saved_quotes = json.load(f)
        expected_quotes = initial_quotes + [new_quote]
        self.assertEqual(saved_quotes, expected_quotes)

    def test_remove_quote_by_index_valid(self):
        initial_quotes = [
            {"text": "Quote 1", "author": "Author 1"},
            {"text": "Quote 2", "author": "Author 2"},
            {"text": "Quote 3", "author": "Author 3"}
        ]
        with open(self.test_file, 'w') as f:
            json.dump(initial_quotes, f)
        removed = self.storage.remove_quote_by_index(1)
        self.assertTrue(removed)
        with open(self.test_file, 'r') as f:
            saved_quotes = json.load(f)
        expected_quotes = [
            {"text": "Quote 1", "author": "Author 1"},
            {"text": "Quote 3", "author": "Author 3"}
        ]
        self.assertEqual(saved_quotes, expected_quotes)

    def test_remove_quote_by_index_invalid(self):
        initial_quotes = [
            {"text": "Quote 1", "author": "Author 1"}
        ]
        with open(self.test_file, 'w') as f:
            json.dump(initial_quotes, f)
        removed = self.storage.remove_quote_by_index(5)
        self.assertFalse(removed)
        with open(self.test_file, 'r') as f:
            saved_quotes = json.load(f)
        self.assertEqual(saved_quotes, initial_quotes)

    def test_remove_quote_by_index_negative(self):
        initial_quotes = [
            {"text": "Quote 1", "author": "Author 1"}
        ]
        with open(self.test_file, 'w') as f:
            json.dump(initial_quotes, f)
        removed = self.storage.remove_quote_by_index(-1)
        self.assertFalse(removed)
        with open(self.test_file, 'r') as f:
            saved_quotes = json.load(f)
        self.assertEqual(saved_quotes, initial_quotes)

    def test_get_quote_count(self):
        initial_quotes = [
            {"text": "Quote 1", "author": "Author 1"},
            {"text": "Quote 2", "author": "Author 2"}
        ]
        with open(self.test_file, 'w') as f:
            json.dump(initial_quotes, f)
        count = self.storage.get_quote_count()
        self.assertEqual(count, 2)

    def test_get_quote_count_empty(self):
        count = self.storage.get_quote_count()
        self.assertEqual(count, 0)

    def test_clear_all_quotes(self):
        initial_quotes = [
            {"text": "Quote 1", "author": "Author 1"},
            {"text": "Quote 2", "author": "Author 2"}
        ]
        with open(self.test_file, 'w') as f:
            json.dump(initial_quotes, f)
        self.storage.clear_all_quotes()
        with open(self.test_file, 'r') as f:
            saved_quotes = json.load(f)
        self.assertEqual(saved_quotes, [])


if __name__ == '__main__':
    unittest.main()