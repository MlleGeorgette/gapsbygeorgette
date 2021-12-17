# I think we were all a bit excited when we first coded Hello World...at least I was :)

def hello_world():
    message = "Hello World!"
    name = "Georgette"
    print("." * len(f"{message} My name is {name}!"))
    print(f"{message} My name is {name}!")
    print("." * len(f"{message} My name is {name}!"))


hello_world()
