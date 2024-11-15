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

def movie_profit(table):
    for row in table:
        budget = int(row[2])
        gross = int(row[3]) + int(row[4])
        profit = gross - budget
        row.append(profit)

def write_file(f_name, table):
    file = open(f_name, "w")
    for row in table:
        row = str(row)
        line = ','.join(row)
        file.write(line + "\n")


def main():
    f_name = read_file_name()
    table = read_file(f_name)
    movie_profit(table)
    write_file(f_name, table)


main()
