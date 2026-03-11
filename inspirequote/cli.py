import argparse
import sys
from inspirequote.core import get_random_quote, get_all_quotes, add_quote, remove_quote
from inspirequote.storage import load_quotes, save_quotes

def main():
    parser = argparse.ArgumentParser(
        description="InspireQuote - A command-line tool to manage and display inspiring quotes."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # show command
    show_parser = subparsers.add_parser("show", help="Display a random inspiring quote")
    show_parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Display all quotes instead of a random one"
    )

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new quote to the collection")
    add_parser.add_argument(
        "text",
        type=str,
        help="The text of the quote"
    )
    add_parser.add_argument(
        "-a", "--author",
        type=str,
        default="Unknown",
        help="Author of the quote (default: 'Unknown')"
    )

    # remove command
    remove_parser = subparsers.add_parser("remove", help="Remove a quote by its ID")
    remove_parser.add_argument(
        "quote_id",
        type=int,
        help="ID of the quote to remove"
    )

    # list command
    list_parser = subparsers.add_parser("list", help="List all quotes with their IDs")

    args = parser.parse_args()

    quotes = load_quotes()

    if args.command == "show":
        if args.all:
            all_quotes = get_all_quotes(quotes)
            if not all_quotes:
                print("No quotes available.")
                sys.exit(0)
            for quote in all_quotes:
                print(f'"{quote["text"]}" - {quote["author"]}')
        else:
            quote = get_random_quote(quotes)
            if quote:
                print(f'"{quote["text"]}" - {quote["author"]}')
            else:
                print("No quotes available.")
                sys.exit(1)

    elif args.command == "add":
        new_quote = add_quote(quotes, args.text, args.author)
        save_quotes(quotes)
        print(f"Quote added successfully (ID: {new_quote['id']}).")

    elif args.command == "remove":
        success = remove_quote(quotes, args.quote_id)
        if success:
            save_quotes(quotes)
            print(f"Quote with ID {args.quote_id} removed successfully.")
        else:
            print(f"Quote with ID {args.quote_id} not found.")
            sys.exit(1)

    elif args.command == "list":
        all_quotes = get_all_quotes(quotes)
        if not all_quotes:
            print("No quotes available.")
            sys.exit(0)
        for quote in all_quotes:
            print(f"[{quote['id']}] \"{quote['text']}\" - {quote['author']}")

    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()