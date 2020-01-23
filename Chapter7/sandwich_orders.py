sandwich_orders = ['ham', 'turkey', 'roast beef', 'tuna', 'salami', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        sandwich = sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
        print(sandwich.title())

print(finished_sandwiches)