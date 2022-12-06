#--This Code Is Copyrighted By Manjeet Singh Please Use It Properly But Don't Claim it's Your ThankYou For More "github.com/CodeManjeet"-


def terminal():
            num = int(input("Enter The Number Of Rows"))

            for i in range (1 , num + 1):
                for k in range (1 , i + 1):
                    print("*" , end="")
                print()
            r = int(input("Would You Like To Try Again ? If Yes Type '1' If No Type '0'"))
            if r == 1:
                terminal()
            elif r == 0:
                print("Thanks For Using This Code Is Provided By Manjeet Singh")
            else:
                print("Invalid Input Found 'Your Script Is Automaticlly Terminated Thank You'")
terminal()


# Thanks For Using Our Source Code Share With Your Friend To sharing Knowledge To Each Other 
# Copyrighted © 2022-23 By Manjeet Singh