import random
import json
from typing import List, Dict, Optional

class Quote:
    """Represents a single inspirational quote."""
    
    def __init__(self, text: str, author: str, tags: Optional[List[str]] = None):
        self.text = text
        self.author = author
        self.tags = tags if tags else []
    
    def to_dict(self) -> Dict:
        """Convert the quote to a dictionary for serialization."""
        return {
            "text": self.text,
            "author": self.author,
            "tags": self.tags
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Quote':
        """Create a Quote instance from a dictionary."""
        return cls(
            text=data.get("text", ""),
            author=data.get("author", "Unknown"),
            tags=data.get("tags", [])
        )
    
    def __str__(self) -> str:
        return f'"{self.text}" - {self.author}'
    
    def __repr__(self) -> str:
        return f'Quote(text="{self.text[:20]}...", author="{self.author}")'

class QuoteCollection:
    """Manages a collection of inspirational quotes."""
    
    def __init__(self, quotes: Optional[List[Quote]] = None):
        self.quotes = quotes if quotes else []
        self._load_default_quotes()
    
    def _load_default_quotes(self) -> None:
        """Load default quotes if the collection is empty."""
        if not self.quotes:
            default_quotes = [
                Quote("The only way to do great work is to love what you do.", "Steve Jobs", ["work", "passion"]),
                Quote("Innovation distinguishes between a leader and a follower.", "Steve Jobs", ["innovation", "leadership"]),
                Quote("Your time is limited, so don't waste it living someone else's life.", "Steve Jobs", ["time", "life"]),
                Quote("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt", ["future", "dreams"]),
                Quote("The only thing we have to fear is fear itself.", "Franklin D. Roosevelt", ["fear", "courage"]),
                Quote("In the middle of difficulty lies opportunity.", "Albert Einstein", ["difficulty", "opportunity"]),
                Quote("Life is what happens to you while you're busy making other plans.", "John Lennon", ["life", "plans"]),
                Quote("The purpose of our lives is to be happy.", "Dalai Lama", ["purpose", "happiness"]),
                Quote("Get busy living or get busy dying.", "Stephen King", ["life", "action"]),
            ]
            self.quotes.extend(default_quotes)
    
    def get_random_quote(self) -> Optional[Quote]:
        """Return a random quote from the collection."""
        if not self.quotes:
            return None
        return random.choice(self.quotes)
    
    def get_all_quotes(self) -> List[Quote]:
        """Return all quotes in the collection."""
        return self.quotes
    
    def add_quote(self, text: str, author: str, tags: Optional[List[str]] = None) -> Quote:
        """Add a new quote to the collection."""
        new_quote = Quote(text, author, tags)
        self.quotes.append(new_quote)
        return new_quote
    
    def remove_quote(self, index: int) -> bool:
        """Remove a quote by its index."""
        if 0 <= index < len(self.quotes):
            self.quotes.pop(index)
            return True
        return False
    
    def clear_quotes(self) -> None:
        """Remove all quotes from the collection."""
        self.quotes.clear()
    
    def get_quote_count(self) -> int:
        """Return the number of quotes in the collection."""
        return len(self.quotes)
    
    def get_quotes_by_author(self, author: str) -> List[Quote]:
        """Return all quotes by a specific author."""
        return [quote for quote in self.quotes if quote.author.lower() == author.lower()]
    
    def get_quotes_by_category(self, category: str) -> List[Quote]:
        """Return all quotes with a specific tag."""
        return [quote for quote in self.quotes if category.lower() in [tag.lower() for tag in quote.tags]]
    
    def get_categories(self) -> List[str]:
        """Return all unique tags across all quotes."""
        categories = set()
        for quote in self.quotes:
            categories.update(quote.tags)
        return list(categories)
    
    def get_authors(self) -> List[str]:
        """Return all unique authors."""
        authors = set(quote.author for quote in self.quotes)
        return list(authors)

# Fonctions globales pour compatibilité avec l'interface existante
DEFAULT_QUOTES = QuoteCollection().quotes

def get_random_quote(quotes=None):
    """Return a random quote."""
    if quotes is None:
        quotes = DEFAULT_QUOTES
    if not quotes:
        return None
    return random.choice(quotes)

def get_all_quotes(quotes=None):
    """Return all quotes."""
    if quotes is None:
        quotes = DEFAULT_QUOTES
    return quotes

def add_quote(quotes, text, author, tags=None):
    """Add a new quote."""
    new_quote = Quote(text, author, tags)
    quotes.append(new_quote)
    return new_quote

def remove_quote(quotes, index):
    """Remove a quote by index."""
    if 0 <= index < len(quotes):
        quotes.pop(index)
        return True
    return False

def clear_quotes(quotes):
    """Clear all quotes."""
    quotes.clear()

def get_quote_count(quotes):
    """Get quote count."""
    return len(quotes)

def get_quotes_by_author(quotes, author):
    """Get quotes by author."""
    return [quote for quote in quotes if quote.author.lower() == author.lower()]

def get_quotes_by_category(quotes, category):
    """Get quotes by category."""
    return [quote for quote in quotes if category.lower() in [tag.lower() for tag in quote.tags]]

def get_categories(quotes):
    """Get all categories."""
    categories = set()
    for quote in quotes:
        categories.update(quote.tags)
    return list(categories)

def get_authors(quotes):
    """Get all authors."""
    authors = set(quote.author for quote in quotes)
    return list(authors)
