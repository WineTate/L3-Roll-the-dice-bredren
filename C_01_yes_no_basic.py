want_instructions =input("Do you want to see instructions?"). lower()

# check the user says yes / no
if want_instructions == "yes" or want_instructions == "y":
    print("you said yes")
elif want_instructions == "no" or want_instructions == "n":
    print("you said no")
else:
    print("g pick yes or no, before i sasa your head")