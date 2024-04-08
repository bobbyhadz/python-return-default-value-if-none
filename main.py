# How to Return a default value if None in Python

# 👇️ Return a default value if the variable is None
def example():
    my_var = None

    return "default value" if my_var is None else my_var


print(example())  # 👉️ "default value"

# ---------------------------------------------

# 👇️ Return a default value if the variable is None
my_var = None

my_var = "default value" if my_var is None else my_var

print(my_var) # 👉️ default value