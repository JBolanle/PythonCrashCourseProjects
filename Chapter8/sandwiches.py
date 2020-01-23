def items_on_sandwich(*items):
    print("\nYour sandwich includes: " )
    for item in items:
        print("- " + item)

items_on_sandwich('lettuce', 'cheese', 'mustard', 'ham', 'tomato')
