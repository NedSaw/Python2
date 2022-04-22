price_all = 0
while True:
    try:
        ticket_number = input('How many tickets do you need?')
        ticket_number = int(ticket_number)
        if type(ticket_number) == int:
            break
    except ValueError:
        print('Type an integer number')
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age_for_ticket = input(f'How old are you {i}? ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('The ticket is free')
            elif 25 > age_for_ticket >= 18:
                price_all += 990
                print('Ticket price: 990 RUB.')
            else:
                price_all += 1390
                print('Ticket price: 1390 RUB.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Type an integer number')
if ticket_number > 5:
    price_all = price_all - ((price_all / 100) * 20)
    print(f'sum is for payment {price_all} RUB. including a 20% discount on the total cost of the order for registration of 5 people')
else:
    print(f'sum is for payment {price_all} RUB.')
