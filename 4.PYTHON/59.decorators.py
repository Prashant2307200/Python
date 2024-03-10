def greet(fx):
    def mfx():
        print('Good Morning')
        fx()
        print('Thanks for using this function')
    return mfx

@greet
def hello():
    print('hello')

hello() 
# - decorated func()
# greet(hello)() 
# - decorator func(decorated func)()