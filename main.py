import sys
from cron_parser.parser import Parser

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cron_parser.py '<cron_expression>'")
        sys.exit(1)

    cron_expression = sys.argv[1]

    try:
        parser = Parser(cron_expression)
        parser.run()
    except ValueError as e:
        print(f"Error: {e}")
