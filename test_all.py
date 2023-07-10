# test_all.py by khhs

# This is a program that tests 20 numbers on every script in the directory.
# If all programs succeded, it exits with code 0, otherwise with code 1.

# This program is under the GNU General Public License, aka the GPL

import glob
import subprocess
import random
import sys
import importlib.util

files = glob.glob("./*.py")
failed = False
for file in [f for f in files if not f.endswith("test_all.py")]:
    print("Testing " + file)
    mod_spec = importlib.util.spec_from_file_location("even", file)
    mod = importlib.util.module_from_spec(mod_spec)
    mod_spec.loader.exec_module(mod)
    for i in range(20):
        number = random.randint(0, 10 * 1000)
        prediction = mod.is_even(number)
        if number % 2 == 0 and prediction == "even":
            continue
        if number % 2 != 0 and prediction == "odd":
            continue
        else:
            print("Test " + str(i) + " failed! Number was: " + str(number) + ", it returned: " + prediction)
            failed = True


if failed:
    print("Not all test passed!")
    sys.exit(1)

print("All tests passed!")
sys.exit(0)
        

