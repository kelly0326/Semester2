'''
Author: Shu Liu
Date: 2024/12/10
Version: 1.0.0
License: MIT
'''
# Above all belong to 'file level doc string'


# below all belong to 'function level doc string'
def convert_type(lst):
    count = []
    for number in range(len(lst)):
        if number != 0:
            count.append(float(lst[number]))
    print(count)
    return count
    '''
    # Doc string
    Description: 
        This function takes a Python string list, and convert to the 
        correct data type.
    Parameter: lst(list)
    Return: (list)
    Precondition: lst must be a python list, data type is string. 

    # law regulated
    # (Precondition is most important. You cannot miss it at work!)
    '''


def get_column(data, column_number):
    lst = []
    for row in data:
        lst.append(row[column_number])
    print("in get_column", lst)
    return lst
    """
    Description:
        This function takes two parameters data and column_number
        and `append` the element into a new empty list(lst).
    Parameter: data, column_number
    Return: lst
    Precondition: data must be a 2D list, column_number must be an integar
                  smaller than the length of the first row
    """

def read_data(path):
    file = open(path)
    data = file.read()
    print(repr(data)) # return print (to see raw string)
    print(data)
    print("50",type(data)) # str

    data1 = data.split("\n")
    print("53",type(data1)) # list
    print(data1)

    data2 = []
    for row in data1:
        temp = row.split(",")
        print("temp=", temp)
        data2.append(temp)
    print(data2)
    return data2
    """
    Description:
        This function takes file name as path, `open`the file
        `read`the file and save it in the variable `data`
        Use `split('\\n')` and `split(",")` convert data to a nested list
        Then return the list
    Parameter: path(str)
    Return: (2d list)
    Precondition: 
        File must in the same folder with Python script, file name must correct
    """

def get_avg(lst):
    """
    Description:
        This function takes a list and return the average of this list.
    Parameter: lst(list)
    Return: float
    Precondition:
        List must be 1D python list.
        List element data type must be integar or float.
    """
    total = sum(lst)
    return total / len(lst)

def main():
    # Define the path to the file
    path = "amd.csv"

    # call read_data to get the 2d list
    data2 = read_data(path)

    # use the previous data and get_column to retrieve the column
    my_column = get_column(data2, 4)
    print("in main", my_column)

    # convert the column to float
    float_column = convert_type(my_column)
    print("in main", float_column)

    # print average
    average = get_avg(float_column)
    print(average)

    print("System exit successfully.")
print("in file parser",__name__)   # run first
if __name__ == '__main__':
    main()
# main() # run second