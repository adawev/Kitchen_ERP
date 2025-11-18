kitchen_menu = {
    "1": {"name": "Osh", "price": 25000},
    "2": {"name": "Manti", "price": 30000},
    "3": {"name": "Lag'mon", "price": 22000},
    "4": {"name": "Shurva", "price": 18000},
    "5": {"name": "Chuchvara", "price": 20000},
    "6": {"name": "Shashlik", "price": 35000},
    "7": {"name": "Somsa", "price": 12000},
    "8": {"name": "Qovurma", "price": 28000},
    "9": {"name": "Beshbarmoq", "price": 26000},
    "10": {"name": "Tovuq go'shti", "price": 30000}
}


while True:
    print("Welcome to our Kitchen!")
    role = int(input(f"""Who are you? Please select👇:
    1.Client
    2.Waiter
    3.Manager
    4.Cooker
    5.Exit
"""))
    if role == 1:
        print("Welcome dear client!")
    if role == 2:
        print("Whats up man!")
    if role == 3:
        print("Welcome dear manager!")
    if role == 4:
        print("How is it going man?")
    if role == 5:
        break