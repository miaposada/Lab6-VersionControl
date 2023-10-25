#Mia Posada
#functions

def encode(password):
  encode = ""
  for digit in str(password):
      encoded_digit = int(digit) +3
      encode += str(encoded_digit)
  return encode


  # decoded by Loubna Benchakouk
def decode(encoded_password):
    decode = ""
    for digit in str(encoded_password):
        decoded_digit = int(digit) - 3
        decode += str(decoded_digit)
    return decode

  
#Menu
if __name__ == '__main__':
    menu_Option = 0
    while menu_Option != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
    
        menu_Option = int(input("Please enter an option: "))
        if menu_Option == 1:
            password = int(input("Please enter your password to encode: "))
            if len(str(password)) == 8:
                print("Your password has been encoded and stored!")
            else:
                print("Password must be an 8 digits and contain only integers")
        
        # changes made by Loubna Benchakouk

        elif menu_Option == 2:
            encoded_password = input("Please enter the encoded password: ")
            original_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
        elif menu_Option == 3:
            break
        else:
            print("Invalid option. Please choose a valid option (1, 2, or 3).")
