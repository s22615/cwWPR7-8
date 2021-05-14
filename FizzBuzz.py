n=int(input("Podaj liczbe"))

#liczby
for i in range(1, n+1):
    if i%3==0:
        print(i, "Fizz")
    if i%5==0:
        print(i, "Buzz")
    if i%3==0 and i%5==0:
        print(i, "FizzBuzz")

#stringi
for i in range(1, n+1):
    fizz_buzz=[]
    if i % 3 == 0:
        fizz_buzz.append("Fizz")
    if i % 5 == 0:
        fizz_buzz.append("Buzz")`,`
    if fizz_buzz:
        print(i, "".join(fizz_buzz))