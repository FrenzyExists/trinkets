#!/usr/bin/env python3


# Database quiz functions of sort


def capacity(dn: int, dp: int, ds: int, dt: int, db: int, i: int):
    return dt * cylinder_capacity(dn, dp, ds, db, i)

def cylinder_capacity(dn: int, dp: int, ds: int, db: int, i: int):
    return dn * dp * ds * db * i

def cost(data_size, transfer_rate, seek, delay, unit="s"):
    if unit == "ms":
        u = 1000
    elif unit == "s":
        u = 1
    elif unit == "min":
        u = 1/60
    else:
        return None
    return (seek + delay + (data_size/transfer_rate)) * u

def sequential_cost(n, data_size, transfer_rate, seek, delay, unit="s"):
    if unit == "ms":
        u = 1000
    elif unit == "s":
        u = 1
    elif unit == "min":
        u = 1/60
    else:
        return None
    return (n * (data_size/transfer_rate) + seek + delay) * u

def random_cost(n, data_size, transfer_rate, seek, delay, unit="s"):
    return n * cost(data_size, transfer_rate, seek, delay, unit)

print("""
______  ___ _____ ___ ______ _____ ___ ______ ___________
|  _  \/ _ \_   _/ _ \| ___ \  ___/ _ \|  _  \  ___| ___ \\
| | | / /_\ \| |/ /_\ \ |_/ / |__/ /_\ \ | | | |__ | |_/ /
| | | |  _  || ||  _  |    /|  __|  _  | | | |  __||    /
| |/ /| | | || || | | | |\ \| |__| | | | |/ /| |___| |\ \\
|___/ \_| |_/\_/\_| |_|_| \_\____|_| |_/___/ \____/\_| \_|
""")

while True:
    print("""
Hey! What you wanna do?
Options:
- Help -> Explain this clusterfuck of a prorgram
- Cost ->
    * Standard-Cost | Random-Cost | Sequential-Cost
- Capacity ->
    *
    """)

    user_boi = input()
    if user_boi == "quit":
        break
