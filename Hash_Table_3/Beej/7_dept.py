records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Engineering"),
]

# Who are all the people working in a given department?

dept = "Engineering"
# dept = "Sales"

dept_idx = {}

def add_dept_idx(name, dept):
    if dept not in dept_idx:
        dept_idx[dept] = []

    dept_idx[dept].append(name) # O(1)

# Build initial index
for name, dept in records: # O(n) over the number of records
    add_dept_idx(name, dept)

print(dept_idx)

# import sys;sys.exit() this allows you to exit from the code

"""
Naive O(n)
for r in records: # O(n) over the number of records
    if r[1] == dept:
        print(r[0])
"""

print(dept_idx["Engineering"])

records.append(("Beej", "Engineering"))
add_dept_idx("Beej", "Engineering")

print(dept_idx["Engineering"])

# Instead of rebuilding index, you can refactor index





