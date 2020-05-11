water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def start_message():
    print('The coffee machine has:')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(coffee_beans) + ' of coffee beans')
    print(str(disposable_cups) + ' of disposable cups')
    print(str(money) + ' of money')
    func_action()


def func_buy():
    global water, milk, coffee_beans, disposable_cups, money
    a = 'I have enough resources, making you a coffee!'
    b = 'Sorry, not enough water!'
    c = 'Sorry, not enough coffee beans!'
    d = 'Sorry, not enough disposable cups!'
    e = 'Sorry, not enough milk!'
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    usr_input = input('> ')
    if usr_input == '1':
        if water < 250:
            print(b)
            func_action()
        elif coffee_beans < 16:
            print(c)
            func_action()
        elif disposable_cups < 1:
            print(d)
            func_action()
        else:
            water = water - 250
            coffee_beans = coffee_beans - 16
            disposable_cups = disposable_cups - 1
            money = money + 4
            print(a)
            func_action()
    elif usr_input == '2':
        if water < 350:
            print(b)
            func_action()
        elif milk < 75:
            print(e)
            func_action()
        elif coffee_beans < 20:
            print(c)
            func_action()
        elif disposable_cups < 1:
            print(d)
            func_action()
        else:
            water = water - 350
            milk = milk - 75
            coffee_beans = coffee_beans - 20
            disposable_cups = disposable_cups - 1
            money = money + 7
            print(a)
            func_action()
    elif usr_input == '3':
        if water < 200:
            print(b)
            func_action()
        elif milk < 100:
            print(e)
            func_action()
        elif coffee_beans < 12:
            print(c)
            func_action()
        elif disposable_cups < 1:
            print(d)
            func_action()
        else:
            water = water - 200
            milk = milk - 100
            coffee_beans = coffee_beans - 12
            disposable_cups = disposable_cups - 1
            money = money + 6
            print(a)
            func_action()
    else:
        func_action()


def func_fill():
    global water, milk, coffee_beans, disposable_cups, money
    print('Write how many ml of water do you want to add:')
    fill_water = int(input('> '))
    water = water + fill_water
    print('Write how many ml of milk do you want to add:')
    fill_milk = int(input('> '))
    milk = milk + fill_milk
    print('Write how many grams of coffee beans do you want to add:')
    fill_coffee_beans = int(input('> '))
    coffee_beans = coffee_beans + fill_coffee_beans
    print('Write how many disposable cups of coffee do you want to add:')
    fill_disposable_cups = int(input('> '))
    disposable_cups = disposable_cups + fill_disposable_cups
    func_action()


def func_take():
    global money
    print('I gave you ' + str(money))
    money = 0
    func_action()


def func_action():
    my_list = ['buy', 'fill', 'take', 'remaining', 'exit']
    for _ in my_list:
        print('Write action (buy, fill, take, remaining, exit):')
        usr_input = input('> ')
        if usr_input == 'buy':
            func_buy()
        elif usr_input == 'fill':
            func_fill()
        elif usr_input == 'take':
            func_take()
        elif usr_input == 'remaining':
            start_message()
        break


func_action()
