import os
import sys
import unittest
module_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, module_path + '/../../')
import inventory


class InventoryTestCase(unittest.TestCase):

    def test_insert_with_valid_input(self):
        book = 'Some book'
        authors = ['Some Author']

        response, err = inventory.insert(book=book, authors=authors)

        assert response
        assert err is None
        assert inventory._BOOKS_TO_AUTHOR_MAP[book.lower()]\
            == [a.lower() for a in authors]
        assert inventory._AUTHOR_TO_BOOKS_MAP[authors[0].lower()]\
            == [book.lower()]

    def test_insert_with_invalid_book(self):
        book = ''
        authors = ['Some Author']

        response, err = inventory.insert(book=book, authors=authors)

        assert response is False
        assert err == 'Book name cannot be empty!'
        assert book.lower() not in inventory._BOOKS_TO_AUTHOR_MAP
        assert authors[0].lower() not in inventory._AUTHOR_TO_BOOKS_MAP

    def test_insert_with_invalid_author(self):
        book = 'Some book'
        authors = ['']

        response, err = inventory.insert(book=book, authors=authors)

        assert response is False
        assert err == 'Author name cannot be empty!'
        assert book.lower() not in inventory._BOOKS_TO_AUTHOR_MAP
        assert authors[0].lower() not in inventory._AUTHOR_TO_BOOKS_MAP

    def test_get_books_for_author_with_books(self):
        book = 'Some book'
        authors = ['Some Author']

        response, err = inventory.insert(book=book, authors=authors)

        assert response

        books = inventory.get_books_for_author(author=authors[0])

        assert len(books) > 0
        assert books[0] == book.lower().strip()

    def test_get_books_for_author_with_empty_list(self):
        book = 'Some book'
        authors = ['Some Author']

        response, err = inventory.insert(book=book, authors=authors)

        assert response

        books = inventory.get_books_for_author(author='Random Author')

        assert len(books) == 0

    def test_compare_with_results(self):
        books = ['Some book', 'Another Book', 'The Book']
        authors = ['Some Author', 'Another Author', 'The Author']

        my_list = ['Some book', 'Another Author', 'Author']

        input_list = ['Another Book', 'Other Book', 'Some Book']
        #-----------------------------++++++++++++--------------

        for book, author in zip(books, authors):
            response, err = inventory.insert(book=book, authors=[author])
            assert response

        result = inventory.compare(my_list=my_list, input_list=input_list)

        assert result == ['Other Book']

    def test_compare_without_results(self):
        books = ['Some book', 'Another Book', 'The Book']
        authors = ['Some Author', 'Another Author', 'The Author']

        my_list = ['Some book', 'Another Author', 'Author', 'The Book']

        input_list = ['Another Book', 'The Book', 'Some Book']

        for book, author in zip(books, authors):
            response, err = inventory.insert(book=book, authors=[author])
            assert response

        result = inventory.compare(my_list=my_list, input_list=input_list)

        assert len(result) == 0

    def tearDown(self):
        inventory._BOOKS_TO_AUTHOR_MAP = {}
        inventory._AUTHOR_TO_BOOKS_MAP = {}
