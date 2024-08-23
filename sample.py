def get_name(userinput):
    name = userinput
    if name == "":
        return 
    
    return name

def get_age(userinput):
        ageInput = userinput
        if ageInput.strip() == "":  #.strip ensures to continue the loop when input is empty
            print("input invalid")
            return None
        
        if isinstance(ageInput, str):
            try:
                ageInput = int(ageInput)
            except ValueError:
                print("Invalid Age, Input a Number")
                return
        return ageInput            


def get_address(userinput):
    address = userinput
    if address == "":
        return
    
    return address
     


        
while True:
    name2 = get_name(input("enter your name: "))
    print(f'hi {name2}')

    age = get_age(input("and how old are you?: "))
    print(f'youre {age} years old')

    address = get_address(input("Where did you live: "))
    print(f'{address} ? Sounds familliar')