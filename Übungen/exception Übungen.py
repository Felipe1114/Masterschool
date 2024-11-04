"""
übung:
macht es einen unterschied, ob in zeiel 10 "error" oder "IndexError" steht?
"""
from logging import ERROR, error
from webbrowser import Error


def except_with_IndexError():
    try:
        items = ['a', 'b']
        third = items[2]
        print("This won't print")
    except IndexError as e:
        print("got an error:", e)


def except_with_Error():
    try:
        items = ['a', 'b']
        third = items[2]
        print("This won't print")
    except Exception as e:
        print("got an error:", e)

except_with_IndexError()
except_with_Error()