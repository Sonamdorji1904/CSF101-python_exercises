with open('fruit_transactions.txt', 'r') as file:
    data = file.readlines()

length = len(data)
print(f"The length of data is {length}")

first_line = data[0]
print(f"The first line is: {first_line}")

line1_dictionary = {
    'name': 'test',
    'action': 'test',
    'quantity': 'adsf',
    'item': '0',
    'price': '0'
}

cleaned_first_line = first_line.replace('\n','')
splitted_line = cleaned_first_line.split(',')
print(splitted_line)

line1_dictionary['name'] = splitted_line[0]
line1_dictionary['action'] = splitted_line[1]
line1_dictionary['quantity'] = splitted_line[2]
line1_dictionary['item'] = splitted_line[3]
line1_dictionary['price'] = splitted_line[4]
