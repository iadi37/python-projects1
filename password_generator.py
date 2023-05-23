#Program to create a random password

import  random #to generate random sequence of Pw
import  string

print("Welcome to our program ")
def main():
    length=int(input("Enter the length of password you want:")) #type conversion
    lowerPw=string.ascii_lowercase# a-->z lowercases
    upperPw=string.ascii_uppercase #a-->z uppercase
    digitPw=string.digits
    symbolPw=string.punctuation #punctuation symbols
    combinedPw=lowerPw+upperPw+digitPw+symbolPw
    Pw=random.sample(combinedPw,length) #output in form of list in variable type from all combined
    # use sample module because return new character after every run
    Password="".join(Pw)
    print(Password)
    main()
main()






