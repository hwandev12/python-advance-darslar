def decorative_func(func):
    def inner(values):
        return [func(val[0], val[1]) for val in values]
    return inner


@decorative_func
def add(a, b):
    print(a + b)
    
print(add([(10, 20), (30, 40)]))

# uyga vazifa alohida, alohida qoshiv, ayiruv, boluv, kopaytiruv ga decorative funksiya oshimiz kerak
    