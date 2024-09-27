""" 
To Find the day at given date one common algorithm is Zeller's congurence
f=(day + [13(month+1)/5] + K + [K/4] + [J/4] - 2J) mod 7 
Where if month is Jan or Feb i.e if 1 or 2 Then Take previous year for calculation and consider 1(Jan) 
as 12+1=13 and Feb(2) as 12+2=14
[] -> means floor division //
K= year of the century, formula: year%100
J= century number, formula: year//100 
"""
def day_finder(day,month,year):
    if month==1 or month==2:
        year-=1 #previous year
        month+=12 # Add 12

    K=year%100
    J=year//100
    f=int((day + (13*(month+1))//5 + K + (K//4) + (J/4) - 2*J) % 7)
    print(f)
    days=["saturday","sunday","monday","Tuesday","Wednesday","Thursday","Friday"]
    return days[f]
    

def main():
        while True: 
            date=input("Enter the date in format(DD-MM-YY): ").split('-')
            day=int(date[0])
            month=int(date[1])
            year=int(date[2])    
            actual_day=day_finder(day,month,year)
            print(f"Day: {actual_day}")
            while True:
                choices  =['yes','y','n','no']
                choice=input("Do you want to continue ? (y or n):").lower()
                if choice in choices:
                        if choice!="yes" and choice!="y":
                         print("Exiting the program")
                         return
                        
                 
                else:
                    print("Invalid choice ") 
                
main()

