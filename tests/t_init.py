"""
Sample usage of functions from __init__.py
"""

import userinput_vrb

###########################################################
# SAMPLE USAGE: input_with_default
###########################################################

c = userinput_vrb.input_with_default("Input Color", "red")
print(f"You have entered '{c}'")

###########################################################
# SAMPLE USAGE: getpass_not_empty
###########################################################

p = userinput_vrb.getpass_not_empty("Enter hidden password: ")
print(f"You have entered '{p}'")

###########################################################
# SAMPLE USAGE: choose_from
###########################################################

if "y" != userinput_vrb.choose_from("Do you want to continue? ", "yn", ": ", "n"):
    print("ABORTED!")
else:
    print("GO AHEAD!")

print("Choose again, this time w/o default", end=": ")
c = userinput_vrb.choose_from()
print(f"You have chosen '{c}'")


