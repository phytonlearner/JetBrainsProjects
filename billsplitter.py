# write your code here
import random

print('Enter the number of friends joining (including you):')
how_many_people = int(input())
friends = {}
if how_many_people > 0:
    print('\nEnter the name of every friend (including you), each on a new line:')
    for _ in range(how_many_people):
        name = input()
        friends[name] = 0
    print('\nEnter the total bill value:')
    bill = int(input())
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    if lucky == 'Yes':
        lucky_name = random.choice(list(friends.keys()))
        print(f'\n{lucky_name} is the lucky one!')
        friends.pop(lucky_name)
        payment = round(bill / (how_many_people - 1), 2)
        friends_dict = dict.fromkeys(friends, payment)
        friends_dict[lucky_name] = 0
        print(friends_dict)
    if lucky == 'No':
        print('No one is going to be lucky')
        payment = round(bill / how_many_people, 2)
        friends_dict = dict.fromkeys(friends, payment)
        print(friends_dict)

else:
    print('No one is joining for the party')
