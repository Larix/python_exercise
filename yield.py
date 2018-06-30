# -*- coding: utf-8 -*-
# yield 可用來在函數中產生數值，使函數變成產生器(Generator)的物件

#reference:https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

#Generators
"""
Generators are iterators, a kind of iterable you can only iterate over once. 
Generators do not store all the values in memory, they generate the values on the fly:
"""
def generator(n):
	num_generator = (x*x for x in range(3))
	for i in num_generator:
		print (i)
#It is just the same except you used () instead of []. ()=>generator []=>list
#cannot perform for i in num_generator a second time since generators can only be "used once".

#iterables
def list_fib(n):
    i, a, b = 0, 0, 1
    fib_list = []
    while True:
        if n <= 0 or i == n:
            break
        a, b = b, a + b
        fib_list.append(a)
        i += 1
    return fib_list

#yield is a keyword that is used like return, except the function will return a generator.
#when you call the function, the code you have written in the function body does not run
def fib_generator(n):
    i, a, b = 0, 0, 1
    while True:
        if n <= 0 or i == n:
            break
        a, b = b, a + b
        yield a
        i += 1 

def main():
	x, y = list_fib(10), fib_generator(10)
	print (type(x), type(y))
	for i in y:
		print (i)

if __name__ == '__main__':
	main()