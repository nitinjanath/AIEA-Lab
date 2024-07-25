from pyswip import Prolog

# Initialize the Prolog interpreter
prolog = Prolog()

# Load the Prolog file
prolog.consult(r'C:\Users\nitin\Desktop\family_tree.pl')

# Query 1: Find all children of John
children_of_john = list(prolog.query("parent(john, Child)"))
print("Children of John:")
for result in children_of_john:
    print(result["Child"])

# Query 2: Find all grandchildren of John
grandchildren_of_john = list(prolog.query("grandparent(john, Grandchild)"))
print("\nGrandchildren of John:")
for result in grandchildren_of_john:
    print(result["Grandchild"])

# Query 3: Check if Mary is a parent of Susan
is_mary_parent_of_susan = list(prolog.query("parent(mary, susan)"))
print("\nIs Mary a parent of Susan?")
print(bool(is_mary_parent_of_susan))

# Query 4: Find all parents in the KB
all_parents = list(prolog.query("parent(Parent, _)"))
print("\nAll parents in the KB:")
for result in all_parents:
    print(result["Parent"])

# Query 5: Find all grandparents and their grandchildren
all_grandparents = list(prolog.query("grandparent(Grandparent, Grandchild)"))
print("\nAll grandparents and their grandchildren:")
for result in all_grandparents:
    print(f"{result['Grandparent']} is a grandparent of {result['Grandchild']}")
