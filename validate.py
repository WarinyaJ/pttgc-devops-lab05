import os

token = os.environ['TOKEN']
print(f'The token retrieved is {token}')

if token == "aaa":
    print("The TOKEN retrieved from production environment")
elif token == "bbb":
    print("The TOKEN retrieved from dev environment")
elif token == "ccc":
    print("The TOKEN retrieved from repo secrets")
elif token == "ddd":
    print("The TOKEN retrieved from organization secrets")
else:
    print("The TOKEN doesn't exist")