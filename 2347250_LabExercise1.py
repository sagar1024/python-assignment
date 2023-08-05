#1MCAB Python Programming
#Lab exercise 1

#My name is Sagar Gurung. I am currently pursuing MCA in Christ University. My domain is Employee information system. My registration number is 2347250. The current academic year is 2023-24.

#Q1. Write a python program to count the frequency of any specific word (in your domain) in the paragraph

print("Q1. Frequency of a specific word in the paragraph: ")

def main():

    name ="Sagar"
    reg = 2347250
    domain = "Employee Information System"
    course = "1MCAB"
    paragraph1 = f'My name is {name}, I have chosen {domain} as my domain my registration number is {reg}, from {course}'

    word = "my"
    frequency = count_word_frequency(paragraph1, word)
    print(f"The word '{word}' appears {frequency} times in the paragraph.")


def count_word_frequency(paragraph, word):
    words_list = paragraph.split()
    count = 0
    for w in words_list:
        if w.lower().strip('.,') == word.lower().strip('.,'):
            count += 1
    return count

main()


#Q2. Write a python program to display all the datatypes of selected specific elements in the paragraph. (For example:– name - string, reg.no - int, marks - float, etc.)

print("Q2. Datatypes of specific elements in the paragraph: ")

name = "Sagar Gurung"
reg_num = 2347250
domain = "Employee information system"
marks = 50.5

print(type(name))
print(type(reg_num))
print(type(domain))
print(type(marks))


#Q3. Write a python program to count the number of alphabets, numeric and other special symbols in the paragraph.

print("Q3. Counting the number of characters in the paragraph: ")

def count_symbols(paragraph):
    #Initializing counters for alphabets, numerics, and special symbols
    num_alphabets = 0
    num_numerics = 0
    num_special_symbols = 0

    #Looping through each character in the paragraph
    for char in paragraph:
        if char.isalpha():
            num_alphabets += 1
        elif char.isdigit():
            num_numerics += 1
        else:
            num_special_symbols += 1

    return num_alphabets + num_numerics + num_special_symbols

paragraph = '''My name is Sagar Gurung. I am currently pursuing MCA in Christ University. My domain is Employee information system. My registration number is 2347250. The current academic year is 2023-24.'''

print(count_symbols(paragraph))


#Sets and Tuples

#Q4. Create a Set with elements that consists of various data types (int, float, string, Boolean, etc. from your domain) and perform the functions pop(), clear(), discard() and del. Write the insights as docstring.

print("Q4. Creating a Set with elements that consists of various data types: ")

mySet = {"Sagar Gurung", "Employee information system", 2347250, 50.0, True}
print(mySet)

mySet.pop()
print(mySet)

mySet.clear()
print(mySet)

#Reintroducing the set
mySet = {"Sagar Gurung", "Employee information system", 2347250, 50.0, True}

mySet.discard("Employee information system")
print(mySet)

del mySet

#Q5. Update the Set with minimum 5 string attributes of your domain and arrange the Set in descending order.

print("Q5. Updating the set with 5 string attributes: ")

mySet = {"SagarGurung", "MCA", "EmployeeInformationSystem", "RegNum2347250", "Marks50.0"}

def descending_order():
    #Sorting the set in descending order
    sorted_set = sorted(mySet, reverse=True)

    return sorted_set

#Storing the values in a variable
sorted_values = descending_order()

#Printing the set
print(sorted_values)

#Q6. Create a Tuple and execute the packing and unpacking operations of tuples using the attributes of your domain.

print("Q6. Creating a tuple and performing packing and unpacking operations: ")

#Packing the tuple
myTuple = "Sagar", 2347250, "EmployeeInformationSystem", 50.0, True, "MCA"

#Unpacking the tuple
name, *course = myTuple

#Printing each value
print(name)
print(course)


#Q7. Enter your domain name as characters and count any number of characters and print the count (for example – (‘p’,’r’,’o’,’g’,’r’,’a’,’m’) count of ‘r’ = 2)

print("Q7. Counting any particular characters: ")

domain = "EmployeeInformationSystem"

def count_character(characters, target_char):
    
    #Converting the characters to a tuple
    my_tuple = tuple(characters)
    
    #Counting the occurrences of the target character in the tuple
    char_count = my_tuple.count(target_char)

    return char_count

count = count_character(domain, str(input("Enter target char: ")))
print(count)


#Q8. Enter your domain name, execute all the slicing possibilities and also negative indexing.

print("Q8. Executing all slicing and indexing possibilities: ")

domain_name = "EmployeeInformationSystem"

#Regular slicing
print(domain_name[0:8])
print(domain_name[2:8])
print(domain_name[8:19])
print(domain_name[:])
print(domain_name[::2])
print(domain_name[::-1])

#Negative indexing
print(domain_name[-1])
print(domain_name[-7:])
print(domain_name[:-5])
