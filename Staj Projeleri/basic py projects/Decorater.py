def my_decorater(func):
    def wrapper():
        print(f"Running  {func.__name__}")
        func()
        print("Complete")
    return wrapper
    

@my_decorater
def  do_this():
    print("Doing this")

    
@my_decorater
def do_that():
    print("Doing that")


do_this()
do_that()