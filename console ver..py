from os import listdir

# By default, this 3 values are False
# ---
# If you suspect that the program is not working correctly, change the value to True
CHECKING_MODE = False
# If you don't have files to evaluate the entire scale of beauty in this program, set the value to True
TEST_MODE = True
# If you are a project developer and you need debug, set the value to True
DEBUG_MODE = False

test_bp_way = "Test blueprints\\"
way = ""


def mode_checker():
    global TEST_MODE
    global DEBUG_MODE
    if CHECKING_MODE:
        TEST_MODE = True
        DEBUG_MODE = False
        checker()
    if TEST_MODE:
        test_mode()


def test_mode():
    global test_bp_way
    global way
    way = test_bp_way


def checker():
    pass


def blueprints_finder(way):
    print(next(iter(listdir(way))))


if __name__ == "__main__":
    mode_checker()
    blueprints_finder(way)
