"""
InspireQuote - A Python package for generating and managing inspirational quotes.
"""

__version__ = "1.0.0"
__author__ = "InspireQuote Team"
__license__ = "MIT"

from inspirequote.core import (
    get_random_quote,
    get_all_quotes,
    add_quote,
    remove_quote,
    clear_quotes,
    get_quote_count,
    get_quotes_by_author,
    get_quotes_by_category,
    get_categories,
    get_authors,
    DEFAULT_QUOTES
)

from inspirequote.storage import (
    load_quotes_from_file,
    save_quotes_to_file,
    export_quotes_to_json,
    import_quotes_from_json
)

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "get_random_quote",
    "get_all_quotes",
    "add_quote",
    "remove_quote",
    "clear_quotes",
    "get_quote_count",
    "get_quotes_by_author",
    "get_quotes_by_category",
    "get_categories",
    "get_authors",
    "DEFAULT_QUOTES",
    "load_quotes_from_file",
    "save_quotes_to_file",
    "export_quotes_to_json",
    "import_quotes_from_json"
]