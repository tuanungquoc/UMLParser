import argparse
import copy
import math
import os
import random
import shutil
import string
import time

class Utilities:
    next_id = 1
    next_func = 0
    next_module = 0
    next_property = 0
    next_var_id = [0]
    file_num = 1

    # Defines creation of char based on number
    @staticmethod
    def create_char_name(num):
        if num > 25:
            return Utilities.create_char_name(math.floor(num / 26) - 1) + Utilities.create_char_name(math.floor(num % 26))
        return list(string.ascii_lowercase)[num]

    # Creates unique variable/constant name
    @staticmethod
    def create_unique_name():
        ids = [num for num in Utilities.next_var_id if num > -1]
        var_name = "".join([chr(ord('a') + x) for x in ids])

        # Resets each index that is larger than 25. If an index is reset, then another index is added
        #   to create more unique IDs.
        for index in reversed(range(len(Utilities.next_var_id))):
            Utilities.next_var_id[index] += 1
            if Utilities.next_var_id[index] > 25:
                Utilities.next_var_id[index] = 0
            else:
                break
        # This else is only called if break is never encountered above.
        else:
            Utilities.next_var_id.append(0)

        return var_name

    # Creates unique function name
    @staticmethod
    def create_function_name():
        name = "func" + str(Utilities.next_func)
        Utilities.next_func += 1
        return name

    # Creates unique module names
    @staticmethod
    def create_module_name():
        name = "module" + str(Utilities.next_module)
        Utilities.next_module += 1
        return name

    # Ensures HTML tag ids are unique
    @staticmethod
    def create_id():
        id = copy.deepcopy(Utilities.next_id)
        Utilities.next_id += 1
        return str(id)

    # Ensures property names are unique
    @staticmethod
    def create_property():
        property = "property" + str(Utilities.next_property)
        Utilities.next_property += 1
        return property

    # Source: http://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python
    @staticmethod
    def get_random_color():
        return "#%06x" % random.randint(0, 0xFFFFFF)

    # Removes the files in the directory.
    # Source: https://github.hpe.com/Fortify-SCA-QA/SwiftGenerator/blob/master/core.py
    @staticmethod
    def remove_files(folder):
        print("Deleting: " + folder)
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            try:
                if os.path.isfile(path):
                    if Properties.verbose:
                        print("Deleting: " + path)
                    os.unlink(path)
                elif os.path.isdir(path):
                    shutil.rmtree(path)
            except Exception as e:
                print(e)

    # Get current time in milliseconds.
    # Sources: http://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
    #          http://stackoverflow.com/questions/18169099/python-get-milliseconds-since-epoch-millisecond-accuracy-not-seconds1000
    @staticmethod
    def current_milli_time():
        return int(round(time.clock() * 1000))

    # Ensure value is not negative, for argument parsing
    # Source: http://stackoverflow.com/questions/14117415/using-argparse-allow-only-positive-integers
    @staticmethod
    def check_negative(value):
        ivalue = int(value)
        if ivalue < 0:
             raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
        return ivalue

    # No operation function, used for lambda
    @staticmethod
    def noop():
        pass

    # Get the directory to the top level of this project.
    @staticmethod
    def root_directory():
        file_dir = os.path.dirname(__file__)
        src_path = os.path.dirname(file_dir)
        top_level = os.path.dirname(src_path)
        return top_level

    # Source: http://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
    @staticmethod
    def nPr(n, r):
        f = math.factorial
        return f(n) / f(n - r)

    @staticmethod
    def nCr(n, r):
        f = math.factorial
        return f(n) / f(r) / f(n - r)

    @staticmethod
    def create_directories():
        if not os.path.exists(Properties.output_dir):
            os.makedirs(Properties.output_dir)
        if not os.path.exists(Properties.dirs[Properties.vanilla_name]):
            os.makedirs(Properties.dirs[Properties.vanilla_name])
        if not os.path.exists(Properties.dirs[Properties.angular_name]):
            os.makedirs(Properties.dirs[Properties.angular_name])
        if not os.path.exists(Properties.dirs[Properties.jquery_name]):
            os.makedirs(Properties.dirs[Properties.jquery_name])
        if not os.path.exists(Properties.dirs[Properties.node_name]):
            os.makedirs(Properties.dirs[Properties.node_name])
        if not os.path.exists(Properties.dirs[Properties.objectivec_name]):
            os.makedirs(Properties.dirs[Properties.objectivec_name])
        if not os.path.exists(Properties.dirs[Properties.swift_name]):
            os.makedirs(Properties.dirs[Properties.swift_name])
        if not os.path.exists(Properties.dirs[Properties.node_multifile_name]):
            os.makedirs(Properties.dirs[Properties.node_multifile_name])
        if not os.path.exists(Properties.dirs[Properties.test_name]):
            os.makedirs(Properties.dirs[Properties.test_name])

    # Return the tabs corresponding to the level requested in "tab"
    @staticmethod
    def tabLevel(tab):
        tabSpace = " "
        tabs = ""
        for num in range(tab*Properties.tab_size):
            tabs += tabSpace

        return tabs