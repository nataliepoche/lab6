def main():
    print("Menu")
    print("-" * 13)
    print("1. Encode \n2. Decode \n3. Quit")

def encode(number):
    coded_pass = []
    number_list =number.split() # split password entered as a list
    for num in num_list:
        coded_pass += num*3 # encode numbers by multiplying by 3
    coded = list.join(coded_pass) # return list to a string
    return coded

def decode(number):
    number_list = number.split()
    for num in num_list:
        decoded_pass += num/3
    decoded = list.join(decoded_pass)
    return decoded

if __name__ == "__main__":
    condition = True
    while condition == True:
        main()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            number = encode(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored!")
            print(number)
        elif choice == 2:
            decode(coded)
            print(f"The encoded password is {new_number}, and the original password is {number}")
        elif choice == 3:
            condition = False