print("Pet suggestion")

valid_size=['small','large']
valid_act=['playful','calm']

while True:
    size=input("Enter a Size of PET you want?").lower()
    act=input("Enter an activity of pet you want?").lower()
    if size in valid_size and act in valid_act:
        if size=="small" and act=="calm":
            print("A kitten for you!")
            rerun=input("Are you satisfied with the suggestion? (y/n)")
            if rerun=="y":
                print("Thank you")
                break
            else:
                print("okay give another input!")
                continue
        elif size=="small" and act=="playful":
            print("A rabbit!")
            break
        else:
            print("syntax error")
            
    else:
        print("invalid input, please try again!")
