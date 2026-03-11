# InspireQuote

A Python package for generating and managing inspirational quotes with a command-line interface.

## Features

- 📜 Collection of inspirational quotes
- 🎲 Random quote generation
- 📝 Add and remove quotes
- 💾 Persistent storage in JSON format
- 🖥️ Easy-to-use CLI interface
- ✅ Comprehensive test suite

## Installation

### Using pip (from source)

```bash
# Clone the repository
git clone https://github.com/yourusername/inspirequote.git
cd inspirequote

# Install in development mode
pip install -e .
```

### Direct installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Requirements

- Python 3.7+
- No external dependencies required for basic functionality

## Usage

### Command Line Interface

```bash
# Display a random inspirational quote
inspirequote random

# Display a specific quote by ID
inspirequote get --id 1

# Add a new quote
inspirequote add --author "Albert Einstein" --text "Imagination is more important than knowledge."

# Remove a quote by ID
inspirequote remove --id 5

# List all quotes
inspirequote list

# Count total quotes
inspirequote count

# Display help
inspirequote --help
```

### Python API

```python
from inspirequote import get_random_quote, add_quote, remove_quote, list_quotes

# Get a random quote
quote = get_random_quote()
print(f"{quote['text']} - {quote['author']}")

# Add a new quote
add_quote("The only way to do great work is to love what you do.", "Steve Jobs")

# List all quotes
all_quotes = list_quotes()
for q in all_quotes:
    print(f"{q['id']}: {q['text']} - {q['author']}")

# Remove a quote
remove_quote(3)
```

## Project Structure

```
inspirequote/
├── __init__.py              # Package initialization
├── core.py                  # Core functionality and quote management
├── cli.py                   # Command-line interface
├── storage.py               # JSON storage management
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── test_core.py
│   └── test_storage.py
├── requirements.txt         # Dependencies
├── setup.py                 # Package setup
├── pyproject.toml          # Build system configuration
├── .gitignore              # Git ignore file
└── example_quotes.json     # Example quotes database
```

## Development

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=inspirequote
```

### Adding Custom Quotes

You can add your own quotes by modifying the `example_quotes.json` file or using the CLI:

```json
[
  {
    "id": 1,
    "text": "The only way to do great work is to love what you do.",
    "author": "Steve Jobs"
  },
  {
    "id": 2,
    "text": "Innovation distinguishes between a leader and a follower.",
    "author": "Steve Jobs"
  }
]
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by various quote APIs and generators
- Built with simplicity and usability in mind