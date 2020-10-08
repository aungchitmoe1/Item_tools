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
        self.metric_choice={
            "1" : "KG",
            "2" : "GM",
            "3" : "LT",
            "4" : "CC",
            "5" : "PACK"
        }
        self.formu_type_choice={
            "1" : "EC",
            "2" : "SC",
            "3" : "SL",
            "4" : "WP",
            "5" : "SP",
            "6" : "GR",
            "7" : "WG",
            "8" : "TA",
            "9" : "OD",
            "10": "FS",
            "11": "DF",
            "12": "CP",
            "13": "FB",
            "14": "OT",
            "15": "SE"
                    }
        
        self.group_choice={

            "1": "HE",
            "2": "IN",
            "3": "FU",
            "4": "NF",
            "5": "PG",
            "6": "NE",
            "7": "BA",
            "8": "RO",
            "9": "ST",
            "10": "NC",
            "11": "FB",
            "12": "MO",
            "13": "FT",
            "14": "BP",
            "15": "NS",
            "16": "NT",
            "17": "NA",
            "18": "IF",
            "19": "SU",
            "20": "SD",
            "21": "AF"

        }
        
        self.company=""
        #Create by MMC
        self.metric=""
        #Create by MMC
        self.quantity=""
        #Create by MMC
        self.quantity_int=0
        #Create by MMC
        self.quantity_str=""
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

    #Change by MMC
    def display_company(self,msg,criteria,input_msg):
        while True:
            print(msg)
            choize=input(input_msg)
            action=criteria.get(choize)
            if action:
                return action
            else:
                 print("{0} is not a valid choice".format(choize))
         

    #    print(
    #     Select The company
        
    #     1. Awba                 4.EVO

    #     2. Kaung Thu Kha        5.Pahtama Seeds

    #     3. WiSarRa
    #     )
    
    def run(self):
        while True:
            self.display_menu()
            choice=input("Enter an option :   ")
            action=self.choices.get(choice)

            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    #Create def by MMC
    def get_unit(self):
        while True:
            try:
                quantity_int1=int(input("Enter the Quantity (Quantity must be at most three digits:     "))
                if quantity_int1 < 1 or quantity_int1>999:
                   print("The value must be at most 3 digits integer")
                else:
                    return quantity_int1
            except ValueError:
                print("The value must be at most 3 digits integer")
                
           
                
    #End of def Creation by MMC


    def add_code(self):
        company_choice_msg= """Select The company
        
        1. Awba                 4.EVO

        2. Kaung Thu Kha        5.Pahtama Seeds

        3. WiSarRa"""

        metric_choice_msg= """Select The Metric
        
        1. KG                 2. GM

        3. LT                 4. CC

        5. PACK """

        formu_type_msg=""" 
                            1. EC           9.  OD
                            2. SC           10. FS
                            3. SL           11. DF
                            4. WP           12. CP
                            5. SP           13. FB
                            6. GR           14. OT
                            7. WG           15. SE
                            8. TA
                        """
        
        group_type_msg=""" 
                           1. HE    8. RO    15. NS
                           2. IN    9. ST    16. NT
                           3. FU    10. NC   17. NA
                           4. NF    11. FB   18. IF
                           5. PG    12. MO   19. SU
                           6. NE    13. FT   20. SD
                           7. BA    14. BP   21. AF

        """
 
        self.company=self.display_company(company_choice_msg,self.company_choice,"Enter a company option")
        self.uni_identifier = input("Enter Unique Identifier:         " )
        self.formu_type=self.display_company(formu_type_msg,self.formu_type_choice,"Enter a formula type")
        self.group_code=self.display_company(group_type_msg,self.group_choice,"Enter a group code")
        #Create by MMC for SKU Section
        self.metric=self.display_company(metric_choice_msg,self.metric_choice,"Enter a metric option")
        self.quantity_int=self.get_unit()
        self.quantity_str=str(self.quantity_int)
        self.quantity=self.quantity_str.zfill(3)
        self.sku = self.quantity+self.metric
        #End of Creation by MMC for SKU Section
        print("Your item code is : "+self.company + self.uni_identifier +'-'+ self.variant +'-'+ self.formu_type+'-' +self.group_code + self.sku)

    def quit(self):
        print("Thank you for using the program")
        sys.exit()

if __name__ == "__main__":
    Menu().run()
