d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}
# tuple

items = list(d.items())

# sort by key
items.sort()
for i in items:
    print(f"{i[0]}: {i[1]}")

print()

# sort by value
# sort has a method that allows you to choose what you want to sort by

def sort_by(t):
    print(f"sort_by({repr(t)})called!")
    return t[1]

items.sort(key=sort_by)
for i in items:
    print(f"{i[0]}: {i[1]}")

items.sort(key=lambda t: t[1])
items.sort(key=lambda t: t[1], reverse=True) # reverse numerical order

# lambda is an anymous function
# can only do simple expressions not for loops or such