# ranged_list_check.py by khhs

# This is a simple and efficient python program that checks if the entered
# number is even, and prints "even" if that is the case. Otherwise it prints
# "odd".

# This program is under the GNU General Public License, aka the GPL.

print("odd" if int(input("Input a number: ")) not in range(0, 10 ** 100, 2) else "even")
