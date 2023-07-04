#import sys
#import glob
#import os
import getpass
#
# Get the directory name
#if sys.platform == 'win32':
#hdir = os.environ['HOMEPATH']
#else:
#hdir = os.environ['HOME']

 # Construct a portable wildcard pattern
#print("Construct a portable wildcard pattern")
#pattern = os.path.join(hdir, '*.*')
#print(pattern)
# # TODO: Use the glob.glob() function to obtain the list of filenames
#filename = glob.glob(pattern)
# # TODO: use os.path.getsize to find each file's size
#print("use os.path.getsize to find each file's size")
#for f in glob.glob(pattern):
# print(f, os.path.getsize(f))
# # TODO: Add a test to only display files that do not have a size of zero
#print("Add a test to only display files that do not have a size of zero")
#for f in glob.glob(pattern):
#    if os.path.getsize(f) > 0:
#        print(f, os.path.getsize(f))
# # TODO: Remove the leading directory name(s) from each filename before you print it -This is a sample Python script.
# using os..path.basename()
#print("Remove the leading directory name(s) from each filename before you print it - using os.path.basename")
#for f in glob.glob(pattern):
#    if os.path.getsize(f) > 0:
#        print(os.path.basename(f), os.path.getsize(f))

import os
import glob

# Get the directory name
hdir = os.path.expanduser("~")

# Construct a portable wildcard pattern
print("Construct a portable wildcard pattern")
pattern = os.path.join(hdir, '*.*')
print(pattern)

# Use the glob.glob() function to obtain the list of filenames
filenames = glob.glob(pattern)

# Use os.path.getsize to find each file's size
print("Use os.path.getsize to find each file's size")
for f in filenames:
    print(f, os.path.getsize(f))

# Add a test to only display files that do not have a size of zero
print("Add a test to only display files that do not have a size of zero")
for f in filenames:
    if os.path.getsize(f) > 0:
        print(f, os.path.getsize(f))

# Remove the leading directory name(s) from each filename before you print it - using os.path.basename
print("Remove the leading directory name(s) from each filename before you print it - using os.path.basename")
for f in filenames:
    if os.path.getsize(f) > 0:
        print(os.path.basename(f), os.path.getsize(f))


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

#supplied_pin = ("Enter your pin")
#pin = 1234
#if input (f'Enter your pin"{pin}') == 'true':
#    print("correct")
#else:
#    print("incorrect")
#while supplied_pin != 'correct':
#    supplied_pin = input('Type "done" to complete:')
#    print('<',supplied_pin,'>')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#pin = "1234"  # Store the PIN as a string
#max_attempts = 3
#attempts = 0

#while attempts < max_attempts:
#    supplied_pin = input("Enter your PIN: ")

#    if supplied_pin == pin:
#        print("Correct")
#        break
#    else:
#        attempts += 1
#        remaining_attempts = max_attempts - attempts
#        print("Incorrect PIN. Remaining attempts:", remaining_attempts)

# getpass
#pin = "1234"
# Store the PIN as a string
#max_attempts = 3
#attempts = 0
#while attempts < max_attempts:
#    supplied_pin = getpass.getpass("Enter your PIN: ")

#    if supplied_pin == pin:
#        print("Correct")
#        break
#    else:
#        attempts += 1
#        remaining_attempts = max_attempts - attempts
#        print("Incorrect PIN. Remaining attempts:", remaining_attempts)

#if attempts == max_attempts:
#    print("Maximum number of attempts reached.")

import getpass

pin = "1234"  # Store the PIN as a string
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    supplied_pin = getpass.getpass("Enter your PIN: ")

    if supplied_pin == pin:
        print("Correct")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print("Incorrect PIN. Remaining attempts:", remaining_attempts)

        if remaining_attempts == 0:
            print("Maximum number of attempts reached. Your account is locked.")
