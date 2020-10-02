import os.path

EXECUTE_COUNT_FILE = 'ExecuteCount.txt'


# Execution count helpers
def check_for_count_file():
    if not os.path.isfile(EXECUTE_COUNT_FILE):
        open(EXECUTE_COUNT_FILE, "w+")


def get_count():
    check_for_count_file()
    count = open(EXECUTE_COUNT_FILE, "r").read()
    return int(count) if count else 0


def increment_count():
    check_for_count_file()
    current_count = get_count()
    open(EXECUTE_COUNT_FILE, "w").write(str(current_count + 1))
