def title_decorator(print_name_function):
    def wrapper():
        print("Professor:")
        print_name_function()
    return wrapper

def title_student(print_name_function2):
    def wrapper():
        print("Student:")
        print_name_function2()
    return wrapper

@title_decorator
def print_my_name():
    print("Shawn", "\n")
    
@title_student
def print_other_name():
    print("Mason", "\n")
    
print_my_name()
print_other_name()