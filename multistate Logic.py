import itertools
import numpy as np

def make_table(operators):
    numbers = [0b000,0b001,0b010,0b011,0b100,0b101,0b110,0b111]
    all_combs = list(itertools.product(range(0,8), repeat=2))

    collector = []

    for comb in all_combs:
        collector2 = [comb[0], comb[1]]
        for op in operators:
            collector2.append(op(comb))
        collector.append(collector2)

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
tablemaker(table)