import os
from idlelib.debugger_r import tracebacktable
from zlib import Z_RLE


# Name: read_file_name
# Parameters: None
# Return: f_name
# Processes user's input and output's if user's input is invalid
def read_file_name():
    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name

def read_file(f_name):
    table = []
    try:
        file = open(f_name, "r")
        for line in f_name:
            row = line.split()
            for i in range(len(row)):
                if row[i].isdigit():
                    row[i] = int([i])


    except:
        print('File does not exist')
    return table

def movie_profit(table):
    for row in table:
        budget = row[2]
        gross = row[3] + row[4]
        profit = gross - budget
        row.append(profit)

def write_file(table, profit):
    file = open(table, "w")
    for row in table:
        line = row.join(',')
        line += '\n'
        print(line)

def main():
    f_name = read_file_name()
    table = read_file(f_name)
    write_file(table, movie_profit(table))


main()
