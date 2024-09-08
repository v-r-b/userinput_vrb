"""
Sample usage of functions from __init__.py
"""

from userinput_vrb import *

print("""
###########################################################
# SAMPLE USAGE: input_with_default
###########################################################
""")

c = input_with_default("Input Color", "red")
print(f"You have entered '{c}'")

print("""
###########################################################
# SAMPLE USAGE: getpass_not_empty
###########################################################
""")

p = getpass_not_empty("Enter hidden non-empty password: ")
print(f"You have entered '{p}'")

def pass_check_fn(passwd: str) -> bool:
    if passwd.find(".") >= 0:
        return True
    else:
        print("Password must contain a '.' character! Please reenter.")
        return False
    
p = getpass_not_empty("Enter hidden non-empty password (must contain \".\"): ", check_fn=pass_check_fn)
print(f"You have entered '{p}'")

print("""
###########################################################
# SAMPLE USAGE: choose_from
###########################################################
""")

if "y" != choose_from("Do you want to continue? ", "yn", end=": ", dflt="n"):
    print("ABORTED!")
else:
    print("GO AHEAD!")

print("Choose again, this time w/o default", end=". ")
c = choose_from()
print(f"You have chosen '{c}'")
