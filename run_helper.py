from datetime import datetime
import os.path
import random

"""
Helper file for the bot run.py file. Used to keep the run file clean while adding new features and methods.
"""

EXECUTE_COUNT_FILE = 'ExecuteCount.txt'
QUOTES_FILE = 'quotes.txt'
LOG_FILE = f"{os.getcwd()}/logs/{datetime.now().strftime('%Y')}/{datetime.now().strftime('%B')}/{datetime.now().date()}.log"


class Helper:
    def __init__(self, author):
        self.author = author

    def add_quote(self, quote):
        """
        Appends a new quote from Brady on a new line
        :param quote: String of the new quote
        :return: Integer value of the line the quote was added to
        """
        self.log(f'User {self.author} added a new quote: {quote}')
        quotes = self.get_quotes()
        open(QUOTES_FILE, 'w', encoding="utf8")\
            .write('\n'.join(map(str, quotes)) + f"\n{quote}\n")
        return len(quotes) + 1

    def check_for_count_file(self):
        if not os.path.isfile(EXECUTE_COUNT_FILE):
            open(EXECUTE_COUNT_FILE, "w+")

    def get_count(self):
        self.check_for_count_file()
        count = open(EXECUTE_COUNT_FILE, "r").read()
        return int(count) if count else 0

    def get_quotes(self):
        """
        Gets all the quotes from Brady stored currently in a text file
        :return: list of quotes
        """
        with open(QUOTES_FILE, 'r', encoding="utf8") as f:
            return [x.strip() for x in f.readlines()]

    def increment_count(self):
        self.check_for_count_file()
        current_count = self.get_count()
        open(EXECUTE_COUNT_FILE, "w").write(str(current_count + 1))

    def log(self, text):
        if not os.path.isfile(LOG_FILE):
            os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
            open(LOG_FILE, "w+")
        logs = open(LOG_FILE, "r").read()
        open(LOG_FILE, "w").write(logs + f"{datetime.now()}: {text}\n")

    def random_quote(self):
        """
        Gets a random quote from Brady
        :return: String random quote
        """
        quotes = self.get_quotes()
        chosen = random.randint(0, len(quotes) - 1)
        return quotes[chosen]

    def remove_quote(self, line):
        """
        Removes a quote from a line in the text file
        :param line: Integer line in the text file
        """
        quotes = self.get_quotes()
        self.log(f'User {self.author} removed quote on line {line}. Text: {quotes[line - 1]}')
        del quotes[line - 1]
        open(QUOTES_FILE, 'w', encoding="utf8").write('\n'.join(map(str, quotes)))

    def show_all_quotes(self):
        quotes = self.get_quotes()
        formatted_quotes = ''
        for n, line in enumerate(quotes, start=1):
            formatted_quotes = formatted_quotes + f"{n}. {line}\n"
        return formatted_quotes
