# Programmers:  Max Rice
# Course:  CS151, Dr. Yalew
# Due Date: 11/21
# Programming Assignment:  Lab 10
# Problem Statement: reads a list of movies and calculates movie profits and highest profiting movie
# Data In: file name
# Data Out:  highest profit movie, cost of movie, movie information
# Credits: the readme file

import os

# Name: read_file_name
# Parameters: None
# Return: f_name
# Processes user's input and output's if user's input is invalid
def read_file_name():
    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name

# Name: read_file
# Parameters: f_name
# Return:table
def read_file(f_name):
    table = []
    try:
        file = open(f_name, "r")
        for line in file:
            row = line.strip().split(',')
            for i in range(len(row)):
                if row[i].isdigit():
                    row[i] = int(row[i])
            table.append(row)

    except FileNotFoundError:
        print('File does not exist')
    return table

# Name: movie_profit
# Parameters: table
# Return: none
def movie_profit(table):
    for row in table:
        budget = int(row[2])
        gross = int(row[3]) + int(row[4])
        profit = gross - budget
        row.append(profit)

# Name: write_file
# Parameters: f_name
# Return: none
def write_file(f_name, table):
        file = open(f_name, "w")
        for row in table:
            line = ','.join(str(row))
            file.write(line + "\n")
        file.close()

# name: output_highest_profit
# Parameter: table
# Return: none
def output_highest_profit(table):
    maximum = 0
    h_row = []
    for row in table:
        try:
            profit = int(row[5])
            if profit > maximum:
                maximum = profit
                h_row = row
        except ValueError:
            print('Something went wrong')

    if h_row:
        print(f'The highest profit is ${maximum}.')
        print(f'Movie Information: {h_row}')
    else:
        print('No data found')

# name: main
# Parameter: none
# Return: none
def main():
    f_name = read_file_name()
    table = read_file(f_name)
    movie_profit(table)
    write_file(f_name, table)
    output_highest_profit(table)


main()
