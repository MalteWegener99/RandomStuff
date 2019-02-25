import itertools
import numpy as np

def make_table(operators):
    size = 3
    numbers = [0b0000,0b0001,0b0010,0b0011,0b0100,0b0101,0b0110,0b0111]#,0b1000,0b1001,0b1010,0b1011,0b1100,0b1101,0b1110,0b1111]
    all_combs = list(itertools.product(range(0,2**size), repeat=2))

    collector = []
    faulty_add = 0
    faulty_sub = 0
    faulty_mul = 0
    faulty_div = 0

    for comb in all_combs:
        collector2 = [comb[0], comb[1]]

        x = comb[0]
        y = comb[1]

        if x + y > 7:
            faulty_add += 1
        if x - y < 0:
            faulty_sub += 1
        if x*y > 7:
            faulty_mul += 1
        if y == 0:
            faulty_div += 1
        elif x%y != 0:
            faulty_div += 1

        for op in operators:
            collector2.append(op(comb))
        collector.append(collector2)

    print(faulty_add)
    print(faulty_sub)
    print(faulty_mul/(2**(2*size)))
    print(faulty_div)
    print((faulty_add+faulty_div+faulty_mul+faulty_sub)/(8*2**(2*size)))

    return collector

def stringify(row):
    string = ""
    for thing in row:
        if thing == None:
            string += "Divide by zero"
        else:
            string += format(thing, '03b') + " | "
    return string

def make_string(thing):
    if thing == None:
        return "Divide by zero"
    else:
        return format(thing, '03b')

AND = lambda x: (x[0]&x[1])&(0b111)
OR = lambda x: (x[0]|x[1])&(0b111)
XOR = lambda x: (x[0]^x[1])&(0b111)
NOT = lambda x: (x[0]!=x[1])&(0b111)
ADD = lambda x: (x[0]+x[1])&(0b111)
SUB = lambda x: (x[0]-x[1])&(0b111)
MULT = lambda x: (x[0]*x[1])&(0b111)
def DIV(x):
    if x[1] > 0:
      return int(x[0]/x[1])&(0b111)

def tablemaker(table):
    print(r'\begin{center}')
    print(r'\begin{tabular}{ |c|c|c|c|c|c|c|c|c|c| } ')
    print(r'\hline')
    print(r'1 & 2 & AND & OR & XOR & NOT & ADD & SUB & MUL & DIV  \\ \hline \hline')
    for row in table:
        for i in range(len(row)):
            print(make_string(row[i]), end='')
            if i == len(row)-1:
                print(r'\\ \hline')
            else:
                print(' & ', end = '')
    print(r'\end{tabular}')
    print(r'\end{center}')

table = make_table([AND, OR, XOR, NOT, ADD, SUB, MULT, DIV])
#tablemaker(table)