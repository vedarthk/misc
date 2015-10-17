import sys
import json

import inventory

if __name__ == '__main__':

    try:
        with open('data.json', 'r') as f:
            input_data = json.loads(f.read())
    except IOError as e:
        sys.stdout.write('[error] data.json file is missing,'
                         ' rename the data.json.example to data.json\n')
        sys.exit(1)

    for book, authors in input_data['inventory'].items():
        inventory.insert(book=book, authors=authors)

    sys.stdout.write('Missing books:\n')
    for i, b in enumerate(inventory.compare(
            my_list=input_data['my_list'],
            input_list=input_data['input_list'])):
        sys.stdout.write('{}. {}\n'.format(i + 1, b))
