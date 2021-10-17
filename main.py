import re

# 1. input one string, define another one, concatenate them and print the result.
message_one = input('Enter the message that you want: ')
message_two = 'this is the second message'

print(f'{message_one} {message_two}')

# 2. Define multiline string and print it.
multiline_message = '''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for 
Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.'''

print(multiline_message)

# 3. Input a string and get substring from start to some position.
message_three = input('Enter a message here: ')

message_substring = message_three[:-1:2]
print(message_substring)

# 4. Input a string, print it from start to half if its length is even, otherwise from half to the end.
message_four = input('Enter the message: ')


def half_substring(message):
    message_half = len(message) // 2

    if len(message) % 2 == 0:
        print(message[:message_half])
    else:
        print(message[message_half:])

half_substring(message_four)

# 5. Calculate number of ‘d’ chars in inputted string.
message_five = input('Enter the message: ')


def char_searching(message):
    counter = 0

    for character in message:
        if 'd' in character:
            counter += 1
    return counter

char_searching(message_five)


# 6. Input string, find how many ‘ab’-s are inside.
message_six = input('enter the text here: ')


def string_checkup(message):
    counter = 0
    for index in range(len(message) - 1):
        if message[index] == 'a' and message[index + 1] == 'b':
            counter += 1
    return counter

string_checkup(message_six)

# 7. Input string and replace all ‘1’ with ‘one'
replaced_string = message_five.replace('1', 'one')

print(replaced_string)

# 8. Define a string with values inside using format() method and print result.
formatted_string = 'We are learning {0}'.format('python')
formatted_string_two = 'We are learning at {place}'.format(place='European University')

print(f'{formatted_string}\n{formatted_string_two}')

# 9. Create a regular expressions to check if string meets some requirements
message_nine = input('Enter the text here: ')


def regex_checkup(message):
    message_pattern = r'^[a-zA-Z]+$'
    alphabet_only = re.match(message_pattern, message)
    if alphabet_only:
        return message
    else:
        print('this is not containing only alphabets')

regex_checkup(message_nine)

# 10. Define a collection of numbers, generate a new collection selecting only odd or dividable by 6 numbers and print it
numbers = [5, 6, 7, 8, 9, 10, 11, 12, 13]

numbers_checkup = [number for number in numbers if number % 2 == 1 or number % 6 == 0]

print(numbers_checkup)

# 11. Create a collection of 6 names inputted from console , generate a new collection selecting only the names starting from ‘A’ and print it


def specific_name_generator():
    inputted_names = []
    for name in range(6):
        names = input('enter the name: ')
        name_pattern = r'^A'
        selected_names = re.match(name_pattern, names)
        if selected_names:
            inputted_names.append(names)
    return inputted_names

specific_name_generator()


# 12. Define a collection of color names, generate a new collection selecting only color name having more than 1 ‘o’ and print it
colors = ['blue', 'orange', 'broown', 'grey']

colors_checkup = [name for name in colors if name.count('o') > 1]

print(colors_checkup)

# 13. Define a collection of pets, that stores types of pet and its name, find how many pets have name Johny and print the number

pets = {'shepard': 'Johny', 'cats': 'Pete', 'bulldog': 'Max', 'persian_cat': 'Johny'}


def pets_names(dictionary_name):
    counter = 0
    for name in dictionary_name:
        if dictionary_name[name] == 'Johny':
            counter += 1
    return counter

pets_names(pets)

# 14. Create a collection for storing hotel visitors (name, country), input several visitors from console,
#print how many visitors are now in hotel, what is their country, what is their name.
hotel = {'Norvik': 'Armenia', 'Mohammad': 'Iran', 'Max': 'USA', 'Andranik': 'Syria'}


def hotel_visitors(hotel):
    for new_visitors in range(3):
        new_visitors_info = input('enter their name and their country using ":" to separate: ')
        visitors_names = new_visitors_info.split(':')[0]
        visitors_country = new_visitors_info.split(':')[1]
        hotel[visitors_names] = visitors_country
    hotel_info = f'Name of the visitors in hotel: {hotel.keys()}\nName of their countries {hotel.values()}\nAmount of visitors in the hotel {len(hotel)}'
    return hotel_info

hotel_visitors(hotel)

# 15. Create a collection of students with their scores and input them from console, remove students with score less than 40 and print final collection.
school = {'Norvik': 90, 'Mohammad': 87, 'Peter': 77, 'John': 35, 'Alex': 40}


def school_students(school):
    for new_students in range(3):
        new_students_info = input('enter their name and their score using ":" to separate: ')
        students_name = new_students_info.split(':')[0]
        students_score = new_students_info.split(':')[1]
        school[students_name] = students_score
    scores = {i: school[i] for i in school if school[i] > 40}
    return scores

school_students(school)

#16. Input string of words separated by coma, get number of words and print it
message_sixteen = input('Enter the numbers separated by come: ')


def word_counting(message):
    splitted_message = message.split(',')
    message_length = len(splitted_message)
    print(message_length)

word_counting(message_sixteen)

#17. Create a regular expression to find occurrences of regular expression in strings.
text = 'Hello my name is Norvik and my last name is Alexian'


def regular_expression(text):
    text_pattern = r'[A-Z]+'
    text_output = re.findall(text_pattern, text)
    text_length = len(text_output)
    print(text_length)

regular_expression(text)

# 18. Define a string and get substring of even elements
text_eighteen = 'This is a Python language'


def even_substring(text):
    even_substring = text[1::2]
    print(even_substring)

even_substring(text)

# 19. Create a collection of dates (date like ‘1/11/2018’ with weekday like ‘Monday’), print total number of date, dates for non-working days (Saturday, Sunday)
dates = {'1/11/2018': 'Monday', '2/11/2018': 'Tuesday', '3/11/2018': 'Wednesday', '6/11/2018': 'Saturday', '7/11/2018': 'Sunday'}

print(len(dates))


def non_workingday(dates):
    for day in dates:
        if day == '6/11/2018' or day == '7/11/2018':
            print('this is nonworking day')

non_workingday(dates)

# 20. Create a collection of filenames with their size, print how many files are greater than 15Mb, how many filenames start from ‘a’ letter, increase size of the file which name ends with ‘.txt’

filenames = {'data.pdf': 20, 'all_pictures.png': 12, 'presentation.txt': 120, 'artificial.py': 18}


def filenames_details(filenames):
    increasing_size = 100
    file_pattern = r'^a'
    extension_pattern = r'.txt$'

    for files in filenames:
        file = re.match(file_pattern, files)
        extension = re.findall(extension_pattern, files)

        if file:
            print(files)
        if extension:
            filenames[files] += increasing_size
            print(filenames[files])


filenames_details(filenames)

file_size = {filenames[files] for files in filenames if filenames[files] > 15}

print(len(file_size))
