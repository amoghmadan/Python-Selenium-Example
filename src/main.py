import sys
from quotestoscrape import QuotesToScrape


if __name__ == '__main__':
    """Call the class by context manager and get quotes data"""

    try:
        with QuotesToScrape() as quotes_to_scrape:
            quotes_data = quotes_to_scrape.parse()

        print(quotes_data)

    except Exception as exc:
        tc, te, tb = sys.exc_info()
        print(f'Class: {tc.__name__} | Exception: {exc} | Line Number: {tb.tb_lineno} | File: {__name__}')
