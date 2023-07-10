# if_check.py by khhs

# This is one of the simpler ones, it is simply a series of if statements.
# However, to keep code length down, it has to be on-the-fly generated.
# This means it doesn't use best practices(exec) but it still works.

# This program is under the GNU General Public License, aka the GPL

exec("def is_even(x):\n" + "\n".join([("\tif x == " + str(f) + ":\n\t\treturn " + ("'even'" if f % 2 == 0 else "'odd'")) for f in range(0,10000)]))
