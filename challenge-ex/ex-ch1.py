with open('./fruit_tansactions.txt', 'r') as file:
    data = file.readlines()

length = len(data)
print(f'the length of data is {length}')

first_line = data(0)
print(f'the first line is: {first_line}')

all_dict_data = []
for line in data:

    # new v = []
    line_dictionary = {
    'name': 'test',
    'action': 'test',
    'quantity': 'adsf',
    'item': '0',
    'price': '0'
    }
    cleaned_first_line = first_line.replace('\n', '')
    splitted_line = cleaned_first_line.split(',')
    print(splitted_line)
    
    line_dictionary['name'] = splitted_line[0]
    line_dictionary['action'] = splitted_line[1]
    line_dictionary['quantity'] = splitted_line[2]
    line_dictionary['item'] = splitted_line[3]
    line_dictionary['price'] = splitted_line[4]
    all_dict_data.append(line_dictionary)

    # print sum(v)

    # counter variable app = 0



total_sales = 0
for item in all_dict_data:
    sale = item

