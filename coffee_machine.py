menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
global coffee_price
global choice
global stat

stat='on'
quarters=0.25
dimes=0.10
nickles=0.05
pennies=0.01

coffee_price={"espresso":1.5,"latte":2.5,"cappuccino":3.0}

#asking the user

def ask():
  key=list(menu.keys())
  print("menu:")
  for i in key:
    print(i) 
  x=input("what would you like to have? :")
  if(x=='espresso'):
    resources["water"]-=100
    resources["milk"]-=50
    resources["coffee"]-=20
  elif (x=='latte'):
    resources["water"]-=75
    resources["milk"]-=45
    resources["coffee"]-=15
  elif (x=="cappuccino"):
    resources["water"]-=105
    resources["milk"]-=55
    resources["coffee"]=30
  else:
    print("invalid choice") 
  print(f"here is your {x}..enjoy")     
  return x
#payment function
def payment():
  print("please insert coin....")
  tot=coffee_price[choice]
  print("the cost is",tot)
  qt=float(input("please insert quarter"))
  dym=float(input("please input dimes"))
  nck=float(input("please input nickels"))
  pen=float(input("please input pennies"))
  cst=qt*quarters+dym*dimes+nickles*nck+pen*pennies
  if tot==cst:
    print('payment has been made....')
  elif tot>cst:
    print("sorry transacrion failed due to insufficient balance")  
    print("please make payment once again")
    print(cst)
    
  else :
    print("your balance is : ",tot-cst) 
def resource_report() :
  print("Resources report")
  print(resources)    
# status of machine
def status():
  user_action=input("switch on or switch off?:")
  print(user_action)
  if stat=='on':
    if stat == user_action :
      print("the machine is currently: ",stat)
    else:
      machine_status=user_action 
      print("the machine has been turned :",stat)
  else:
    print("the machine is off" )
   
  
status()
resource_report()
choice=ask()
resource_report()
payment()

