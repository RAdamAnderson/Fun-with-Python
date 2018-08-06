def name():
    orig=input("Hello. Nice to meet you. What is your name? ")
    if len(orig)>0 and orig.isalpha() and orig!="Fart":
        print("Hello, %s. %s isn't a silly enough name. Your name is Fart now." % (orig, orig))
        name()
    elif orig=="Fart":
        print("Hello, Fart.")
name()
