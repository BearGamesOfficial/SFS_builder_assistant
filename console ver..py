from os import listdir
from math import tan, pi, sin

# By default, this 3 values are False
# ---
# If you suspect that the program is not working correctly, change the value to True
CHECKING_MODE = False
# If you don't have files to evaluate the entire scale of beauty in this program, set the value to True
TEST_MODE = True
# If you are a project developer and you need debug, set the value to True
DEBUG_MODE = True

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


def circle_calc(inner_radius, min_n=3, max_n=-1, min_a=1, max_a=-1, outer_radius=-1, sep_from_surface=-1):
    # Declare base variables
    global DEBUG_MODE
    ideal_h, max_n_border, max_a_border, out_rad_border, max_iter_border = False, False, False, False, 10 ** 12
    circle = [inner_radius, outer_radius, min_n, min_a, sep_from_surface]
    # Checking input data
    if sep_from_surface >= 0:
        ideal_h = True
    if min_n < 3:
        min_n = 3
    if max_n > min_n:
        max_n_border = True
    else:
        max_n = max_iter_border
    if min_a < 0.5:
        min_a = 0.5
    if max_a > min_a:
        max_a_border = True
    if outer_radius > inner_radius:
        out_rad_border = True
    # Debug of checker
    if DEBUG_MODE:
        print(f"Inner radius: {inner_radius} meters;\n\
Outer radius enabled ({out_rad_border}){': ' + str([outer_radius for i in [0] if out_rad_border]) + ' meters'};\n\
Minimal number of angles is {min_n};\n\
Maximal number of angles enabled ({max_n_border}){': '+ str([max_n for i in [0] if max_n_border])};\n\
Minimal length of module is {min_a} meters;\n\
Maximal length of module enabled ({max_a_border}){': '+ str([max_a for i in [0] if max_a_border])};\n\
Ideal separation from the surface enabled({ideal_h}){': ' + str([sep_from_surface for i in [0] if ideal_h])};\n\
Not ideal circle ({'; '.join([str(x) for x in circle])}) when variables correspond to:\n\
(<inner_radius>; <outer_radius>; <number of angles (n)>; <length of module (a)>, <separation_from the_surface>)")
    for n in range(min_n, max_n):
        # We need to limit of iterations because is unknown how much iterations will be need for search optimal variant
        # Calculating base parameters of circle
        module_length = 2 * inner_radius * tan(pi/n)
        outer_radius = module_length / 2 / sin(pi/n)
        separation = outer_radius - inner_radius
        # Checking accuracy of parameters
        pass


def blueprints_finder(way):
    print(next(iter(listdir(way))))


if __name__ == "__main__":
    mode_checker()
    blueprints_finder(way)
    print("It's working")
    circle_calc(3500000)
