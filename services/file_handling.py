import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = dict()


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    if start + page_size > len(text) - 1:
        return text[start:], len(text[start:])
    while (text[end := start + page_size - 1] not in (chars := ',.!:;?') or
           text[end + 1] in chars):
        page_size -= 1
    return str(text[start:end + 1]), page_size


def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as file:
        text = file.read()
    start_page, page_num = 0, 1
    while start_page < len(text):
        page_text,  page_size = _get_part_text(text, start_page, PAGE_SIZE)
        book[page_num] = page_text.lstrip(' ,.!:;?\n')
        start_page += page_size
        page_num += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
