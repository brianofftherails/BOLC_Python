#!/usr/bin/env python3
# FizzBuzz
#try:
#    testval = int(input("Enter a value...\t"))
i = int(input("Enter a value...\t"))
#except OSError as e:
#    print("Invalid input.\n")
print(f'Received {i} as input.\n')
mod3testcondn = i % 3
mod5testcondn = i % 5
if mod3testcondn and mod5testcondn:
    print(i,end='')
    #pass
elif not mod3testcondn and mod5testcondn:
    # Divisible by 3, not by 5
    print("fizz",end='')
elif mod3testcondn and not mod5testcondn:
    # Divisible by 5, not by 3
    print("buzz",end='')
else:
    # Divisible by both
    print("fizzbuzz",end='')
