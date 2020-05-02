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


def func_buy():
    global water, milk, coffee_beans, disposable_cups, money
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    usr_input = input('> ')
    if usr_input == '1':
        water = water - 250
        coffee_beans = coffee_beans - 16
        disposable_cups = disposable_cups - 1
        money = money + 4
    elif usr_input == '2':
        water = water - 350
        milk = milk - 75
        coffee_beans = coffee_beans - 20
        disposable_cups = disposable_cups - 1
        money = money + 7
    else:
        water = water - 200
        milk = milk - 100
        coffee_beans = coffee_beans - 12
        disposable_cups = disposable_cups - 1
        money = money + 6


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


def func_take():
    global money
    print('I gave you ' + str(money))
    money = 0


start_message()
print('Write action (buy, fill, take):')
action = input('> ')
if action == 'buy':
    func_buy()
elif action == 'fill':
    func_fill()
else:
    func_take()
start_message()
