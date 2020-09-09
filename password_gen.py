# Super simple password gen made on a meeting with other classmates when talking about algorithms

def password_gen() -> str:
    voc = "abcdehijklmnopqrstuvwxyz"
    num = "1234567890"
    length = random.randrange(8, 12)
    password = []
    switch = [i for i in range(20)]
    for i in range(length):
        if random.choice(switch) >= 16:
            password.append(random.choice(num))
        else:
            password.append(random.choice(voc))

        if type(password[i]) == str and random.choice(switch) <= 5:
            password[i] = password[i].upper()
    return password
