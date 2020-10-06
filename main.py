import sys

class Menu:

    def __init__(self):
        self.choices={
            "1" : self.add_code,
            "2" : self.quit
        }
        self.company_choice={
            "1" : "AW",
            "2" : "KTK",
            "3" : "WSR",
            "4" : "EVO",
            "5" : "PS"
        }
        self.company=""
        self.sku=""
        self.uni_identifier=""
        self.variant="A"
        self.formu_type=""
        self.group_code=""

    def display_menu(self):
        print(""" 
        
            Program Menu  
 

             1. Create code
 
             2. Quit program
             """)

    def display_company(self):
        print("""
        Select The company
        
        1. Awba                 4.EVO

        2. Kaung Thu Kha        5.Pahtama Seeds

        3. WiSarRa
        """)
    
    def run(self):
        while True:
            self.display_menu()
            choice=input("Enter an option :   ")
            action=self.choices.get(choice)

            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def add_code(self):
        self.display_company()
        choize=str(input("Enter a company ooption : "))
        self.company = self.company_choice[choize]

        self.uni_identifier = input("Enter Unique Identifier:         " )
        self.formu_type = input("Enter Formula Type:         " )
        self.group_code = input("Enter Group code:         " )
        self.sku = input("Enter SKU : ")

        print("Your item code is : "+self.company + self.uni_identifier +'-'+ self.variant +'-'+ self.formu_type+'-' +self.group_code + self.sku)

    def quit(self):
        print("Thank you for using the program")
        sys.exit()

if __name__ == "__main__":
    Menu().run()
