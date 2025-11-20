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

staff = [
    { "name": "Diyor", "role": "Chef" },
    { "name": "Bexzod", "role": "Manager" },
    { "name": "Rayxona", "role": "Waitress" },
    { "name": "Sunnatjon", "role": "Waiter" },
]
orders = {}

# Manager rules
# Checks staff - cook, waiter
# calculates money, withdraws money from balance
# complaints from user side (Insurance provided)

complaints = {}
balance = 0

def get_complaints():
    print("Complaints:")
    for i , n in complaints.items():
        print(f"{i}. {n}")

def get_menu(menu):
    print("Menu:")
    for id, info in kitchen_menu.items():
        print(f"{id}. {info['name']} - {info['price']} so'm")


def get_orders(order_list):
    if orders:
        for id, info in orders.items():
            print(f"\nOrder ID: {id}")
            print(f"Status: {info['status']}")
            print(f"Payment: {info['payment']}")
            print("Items:")
            for i in info['items']:
                print(f"- {i['name']} x{i['count']} = {i['total']} so'm")
            print(f"Total: {info['total']} so'm")
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
>>> """))
    ## Client
    if role == 1:
        print("Welcome dear client!")
        while True:
            firstSelectClient = input("""What do you want? Please select👇:
    1. Order food
    2. My orders
    3. Menu
    4. Complaint
    5. Back to main menu
    >>> """)

            if firstSelectClient == "1":
                order_items = []
                order_total = 0

                while True:
                    get_menu(kitchen_menu)
                    foodId = input("Enter food ID (or X to finish): ")

                    if foodId.lower() == "x":
                        break

                    if foodId in kitchen_menu:
                        count = input("How many? ")
                        if count.isdigit() and int(count) > 0:
                            count = int(count)
                            food = kitchen_menu[foodId]
                            total = food["price"] * count
                            order_total += total

                            order_items.append({
                                "name": food["name"],
                                "price": food["price"],
                                "count": count,
                                "total": total
                            })
                        else:
                            print("Quantity must be positive.")
                    else:
                        print("Invalid food ID!")

                if len(order_items) == 0:
                    print("Order cancelled.")
                    continue

                print(f"Total order price: {order_total} so'm")

                payment = input("Payment method (naqd/karta): ")

                orderId = len(orders) + 1

                orders[orderId] = {
                    "items": order_items,
                    "total": order_total,
                    "status": "In proccess",
                    "payment": payment if payment in ["naqd", "karta"] else "naqd"
                }

                balance += order_total
                print(f"Your order #{orderId} has been placed!")
            elif firstSelectClient == "2":
                print("Your orders:")
                get_orders(orders)

            elif firstSelectClient == "3":
                get_menu(kitchen_menu)
            elif firstSelectClient == "4":
                complaint = input("Write your complaint: ")
                complaints[len(complaints)+1] = complaint
            elif firstSelectClient == "5":
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
                get_orders(orders)
                selectedOrder = int(input("Select order to submit: "))
                if selectedOrder in orders:
                    orders[selectedOrder]["status"] = "Completed"
                    print("Your order has been submitted!")
                else:
                    print("Please type correct order.")

            elif waiterRequest == "3":
                break
            else:
                print("Invalid input, please enter between 1-3")

    ## Manager
    if role == 3:
        print("Welcome dear manager!")
        while True:
            choice = input("""Please select the section you want
            1. Check Staff
            2. Budget
            3. Complaints
            4. Back to main menu
            >>> """)

            if choice == "1":
                for i in staff:
                    print(f"{i['name']} - {i['role']}")

            if choice == "2":
                while True:
                    choice = input("""Please select the section you want
                    1. Check Balance
                    2. Withdraw Money
                    0. Back to main menu
                    >>> """)
                    
                    if choice == "1":
                        print(f"Your balance: {balance} sum")
                    if choice == "2":
                        money = int(input(f"Enter the amount of money you want to withdraw, Balance: {balance}: "))
                        if balance - money >= 0:
                            balance -= money
                            print("Withdraw done successfully!")
                        elif money < 0:
                            print("Please valid amount of money.")
                        else:
                            print("Balance has no enough money to withdraw money.")
                    if choice == "0":
                        break

            if choice == "3":
                get_complaints()
            if choice == "4":
                break

    ## Cooker
    if role == 4:
        print("How is it going man?")
        while True:
            cookerRequest = input("""What do you want? 
            1. See Orders
            2. See Menu
            3. Back to main menu
            >>>""")

            if cookerRequest == "1":
                get_orders(orders)
            elif cookerRequest == "2":
                get_menu(kitchen_menu)
            elif cookerRequest == "3":
                break
            else:
                print("Invalid input, please enter between 1-3")

    if role == 5:
        break
