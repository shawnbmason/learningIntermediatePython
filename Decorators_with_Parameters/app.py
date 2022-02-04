def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Professor:", "\n")
        print_name_function(*args, **kwargs)
    return wrapper

@title_decorator
def print_my_name(name):
    print(name)
    
print_my_name("Shawn Mason")
