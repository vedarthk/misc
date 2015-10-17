Library Manager
===============

Program to compare personal list of books/authors with that of any other list of books.

### data.json

This JSON file consists of 3 keys as follow:

- `invenotry` - dictionary of book names and their author
- `my_list` - list of books with me containing book/author names
- `input_list` - list of books from a friend for comparison

### Assumptions

- This is for personal library management, which means there will be finite number of books and authors which can be stored in memory at any given point of time
- There is only one author for a book
- Author name can be of two words i.e. `Firstname Lastname` OR `Lastname Firstname`
- Author names entered are consistent in the list of books and the map which is created by the maintainer

Example input is given in `data.json.example`, rename it to `data.json` to run the program with default input provided in the file.

To execute tests or the program please install the requirements with following command:

```shell
$ pip install -r requirements.txt
```

Running tests:

```shell
$ py.test
```

Running program:

```shell
$ python main.py
```
