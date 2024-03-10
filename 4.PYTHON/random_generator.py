def rand():
    import string as str
    posOp = str.ascii_letters + str.digits
    from random import choices
    rand_str = "".join(choices(posOp ,k=10))
    print(__name__)
    print(rand_str)

if __name__ == "__main__":
    rand()
