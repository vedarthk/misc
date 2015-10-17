_BOOKS_TO_AUTHOR_MAP = {}
_AUTHOR_TO_BOOKS_MAP = {}  # reverse index of authors to books


def _validate_input_data(book, authors):
    """Validates book and author names

    :param book: name of the book
    :param authors: list of author names
    :returns: tuple with validation status and error message if any
    :rtype: ``tuple``

    """
    if not book:
        return (False, 'Book name cannot be empty!')

    if not len([a for a in authors if a]):
        return (False, 'Author name cannot be empty!')

    return (True, None)


def _create_set_of_books(my_list):
    """Creates a set of books by replacing author names by book names.

    :param my_list: list of books containing author names
    :returns: set of book names
    :rtype: ``set``

    """
    my_books = []
    for name in my_list:
        books = get_books_for_author(name)
        my_books.extend(books if books else [name.lower().strip()])

    return set(my_books)


def insert(book, authors):
    """Inserts book and authors information in database and creates
    reverse index for authors and books.

    :param book: name of the book
    :param authors: list of authors
    :returns: tuple with insertion status and error if any
    :rtype: ``tuple``

    """
    book = book.lower().strip()
    authors = [n.lower().strip() for n in authors]

    validation_result, err = _validate_input_data(book=book, authors=authors)
    if not validation_result:
        return (False, err)

    if book in _BOOKS_TO_AUTHOR_MAP:
        return (False, None)

    _BOOKS_TO_AUTHOR_MAP[book] = authors

    for author in authors:
        if author in _AUTHOR_TO_BOOKS_MAP:
            _AUTHOR_TO_BOOKS_MAP[author].append(book)
        else:
            _AUTHOR_TO_BOOKS_MAP[author] = [book]

    return (True, None)


def get_books_for_author(author):
    """Returns book for the given author if present in the inventory.

    :param author: author name can be in any format (first name first or last name first)
    :returns: list of books by that author if present
    :rtype: ``list``

    """
    author = author.lower().strip()
    names = author.split()
    if len(names) > 1:
        name_combinations = (
            u'{}'.format(names[0]),
            u'{}'.format(names[1]),
            u'{} {}'.format(names[0], names[1]),
            u'{} {}'.format(names[1], names[0])
        )
    else:
        name_combinations = (author, )

    books = []
    for combination in name_combinations:
        books.extend(_AUTHOR_TO_BOOKS_MAP.get(combination, []))
    return books


def compare(my_list, input_list):
    """Compare list of book names containing authors with another list
    of only book names.

    :param my_list: list of books containing author names
    :param input_list: list of book names from friend
    :returns: list of missing books from my collection
    :rtype: ``list``

    """

    books_set = _create_set_of_books(my_list=my_list)
    return [name for name in input_list if name.lower() not in books_set]
