import pandas as pd
import random
import string

random.seed(42)

def generate_password():
    length = random.randint(6, 16)

    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ''.join(random.choice(chars) for _ in range(length))

    return password


def extract_features(password):

    length = len(password)

    upper = sum(c.isupper() for c in password)

    lower = sum(c.islower() for c in password)

    digits = sum(c.isdigit() for c in password)

    special = sum(c in "!@#$%^&*" for c in password)

    score = 0

    if length >= 8:
        score += 1

    if upper > 0:
        score += 1

    if lower > 0:
        score += 1

    if digits > 0:
        score += 1

    if special > 0:
        score += 1

    if score <= 2:
        label = "Weak"

    elif score == 3 or score == 4:
        label = "Medium"

    else:
        label = "Strong"

    return [password, length, upper, lower, digits, special, label]


data = []

for i in range(2000):
    pwd = generate_password()
    data.append(extract_features(pwd))


df = pd.DataFrame(data, columns=[
    "password",
    "length",
    "uppercase",
    "lowercase",
    "digits",
    "special",
    "strength"
])

df.to_csv("password_dataset.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())