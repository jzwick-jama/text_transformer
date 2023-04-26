# python string transformations v0.1
# by Jenna Zwick
# ----------
# console version:

# Enter an option and it will output the result to the console and close. Options:
# (1) Swapcase
# (2) To uppercase
# (3) to lowercase

stt = ""
answer = ""

print("Jenna's text-transformer tool: Paste your text string, then choose the operation to perform and the output will be the string as you requested.")
stt = input("First, please paste your string into the console:")
print(" ---------------------- ")
print("Now, enter an option: # (1) Swap case # (2) Text-to-uppercase # (3) Text-to-lowercase")
answer = int(input("Please select the text transformation action you want to perform on your string: 1, 2 or 3"))
print(" ---------------------- ")

if answer == 1:
    ts = stt.swapcase()
    print(ts)
    quit_time = input("Swapped case. Press any key to quit.")
    if quit_time != None:
        print("Closing...")

elif answer == 2:
    ts = stt.upper()
    print(ts)
    quit_time = input("Text-to-Uppercase swapped. Press any key to quit.")
    if quit_time != None:
        print("Closing...")

elif answer == 3:
    ts = stt.lower()
    print(ts)
    quit_time = input("Text-to-Lowercase swapped. Press any key to quit.")
    if quit_time != None:
        print("Closing...")

else:
    print(f'ERROR - Debug Info: STT: {stt}, answer: {answer}')