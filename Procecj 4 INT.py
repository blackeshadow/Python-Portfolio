#programer: Ignashious Harrison
#Date: 3/4/2023
#Declare variables
import Welcome
import Retail
i=0
d=2
if i<d:
    
    def main():
        discount=0
        dprice=0
        adisc=0
        price=0
        total=0
        packages=inputp()
        discount=cdiscount(packages)
        fprice=fullprice(Retail.retail,packages)
        dprice=ddiscount(fprice,discount,dprice)
        total=totalp(dprice,fprice)
        printa(dprice,total)
        restart()
        #tell user
    def inputp():
        packages= int(input("enter how many packages:"))
        return packages
    def ddiscount(fprice,discount,dprice):
        dprice= fprice*discount
        return dprice
    def cdiscount(packages):
        if packages >99:

                discount = 0.50
        elif packages > 49:
                discount =0.40
        elif packages >19:
                discount =0.30
        elif packages >9:
                discount=0.20
        else:
                  discount = 0.0
        return discount
    def fullprice(retail,packages):
        fprice= packages*retail
        return fprice
    def totalp(dprice,fprice):
        total= fprice-dprice
        return total
    #tell user their total
    def printa(dprice,total):
        print("Your discount is:$", format(dprice,',.2f'), "Your total is:$", format(total,',.2f'))
    def restart():
        i=int(input("Do you wish to continue? 1 for yes 2 for no"))
        if i<2:
            main()
def restart():
    i=int(input("Do you wish to continue? 1 for yes 2 for no:"))
    if i<2:
        main()
restart()
        



