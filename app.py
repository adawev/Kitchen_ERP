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
orders = {}

def get_menu(menu):
    print("Menu:")
    for id, info in kitchen_menu.items():
        print(f"{id}. {info['name']} - {info['price']} so'm")

def get_orders(order_list):
    if orders:
        for id, info in orders.items():
            print(f"{id}. {info['name']} x{info['count']} - {info['total']} so'm")
    else:
        print("No orders yet.")

while True:
    print("Welcome to our Kitchen!")
    role = int(input(f"""Who are you? Please select👇:
    1.Client
    2.Waiter
    3.Manager
    4.Cooker
    5.Exit
"""))
    ## Client
    if role == 1:
        print("Welcome dear client!")
        while True:
            firstSelectClient = input("""What do you want? Please select👇:
    1. Order food
    2. My orders
    3. Menu
    4. Back to main menu
    """)

            if firstSelectClient == "1":
                get_menu(kitchen_menu)
                # for id, info in kitchen_menu.items():
                #     print(f"{id}. {info['name']} - {info['price']} so'm")

                foodId = input("Which food do you want? Enter id: ")

                if foodId in kitchen_menu:
                    count = input("How many do you want? ")
                    if count.isdigit() and int(count) > 0:
                        count = int(count)
                        orderId = len(orders) + 1
                        food_info = kitchen_menu[foodId]
                        orders[orderId] = {
                            "name": food_info["name"],
                            "price": food_info["price"],
                            "count": count,
                            "total": food_info["price"] * count
                        }
                        print(
                            f"Your order has been placed: {food_info['name']} x{count} - {food_info['price'] * count} so'm")
                    else:
                        print("Quantity must be a positive number.")
                else:
                    print("Invalid food ID!")

            elif firstSelectClient == "2":
                print("Your orders:")
                get_orders(orders)
                # if orders:
                #     for id, info in orders.items():
                #         print(f"{id}. {info['name']} x{info['count']} - {info['total']} so'm")
                # else:
                #     print("No orders yet.")

            elif firstSelectClient == "3":
                get_menu(kitchen_menu)
                # for id, info in kitchen_menu.items():
                #     print(f"{id}. {info['name']} - {info['price']} so'm")

            elif firstSelectClient == "4":
                break

            else:
                print("Invalid input. Please select from 1-4")

    ## Waiter
    if role == 2:
        print("Whats up man!")
        while True:
            waiterRequest = input("""What you want to do?
            1. Read orders
            2. Submit orders
            3. Back to main menu
            >>> """)
            if waiterRequest == "1":
                get_orders(orders)
            elif waiterRequest == "2":
                print("Submitted✅")
            elif waiterRequest == "3":
                break
            else:
                print("Invalid input, please enter between 1-3")
            



    ## Manager
    if role == 3:
        print("Welcome dear manager!")

    ## Cooker
    if role == 4:
        print("How is it going man?")
        while True:
            cookerRequest = int(input())
    if role == 5:
        break
