# Programmers:  [Max and Cody]
# Course:  CS151, [Professor Zee]
# Due Date: [11/21/2024]
# Lab Assignment:  [Lab 10]
# Problem Statement:  [Our program adds the profits to each movie in the list, then outputs the maximum profit and the movie it is associated with]
# Data In: [the file they want to read from]
# Data Out:  [maximum profit/ movie information]
# Credits: [class notes and class program]

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
# Return: table
# Opens file from user input, checks the length of each list in the table and then appends it
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

#Name: movie_profit
#Parameters: f_name
#Return: table
#for each row it finds the budget and the gross revenue then finds the profit, and adds it to each list
def movie_profit(table):
    for row in table:
        budget = int(row[2])
        gross = int(row[3]) + int(row[4])
        profit = gross - budget
        row.append(profit)

#Name: write_file
#Parameters: f_name, table
#Return: None
#splits each index in the table with white space so it is formatted better
def write_file(f_name, table):
        file = open(f_name, "w")
        for row in table:
            line = ''.join(str(row))
            file.write(line + "\n")
        file.close()

#Name: output_highest_profit
#Parameters: table
#Return: None
#finds the highest profit and then outputs the highest one, with the movie information
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
            print('something went wrong')


    print(f'The highest profit is ${maximum}.')
    print(f'Movie Information: {h_row}')

#Name: main
#Paramteres: None
#Return: None
#Calls all the functions
def main():
    f_name = read_file_name()
    table = read_file(f_name)
    movie_profit(table)
    write_file(f_name, table)
    output_highest_profit(table)

#call main
main()
