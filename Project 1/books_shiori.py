from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import copy

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    category: str
    id: int | None = None

BOOKS: list[Book] = [
    {'id': 1, 'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'id': 2, 'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'id': 3, 'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'id': 4, 'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'id': 5, 'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'id': 6, 'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]



def filter_books_by_field(book, field, value):
    if book.get(field) and book.get(field).casefold() == value.casefold():
        return True
    return False
    

@app.get("/books/" , responses={
    404: {
        "description": "Books not found"
    }
})
async def read_books(title: str = None, author: str = None, category: str = None):
    try:
        return_books = BOOKS
        if title:
            if len(return_books) > 0:
                return_books = list(filter(lambda book: filter_books_by_field(book, field='title', value=title), return_books))
        if author:
            if len(return_books) > 0:
                return_books = list(filter(lambda book: filter_books_by_field(book, field='author', value=author), return_books))
        if category:
            if len(return_books) > 0:
                return_books = list(filter(lambda book: filter_books_by_field(book, field='category', value=category), return_books))
        
        if len(return_books) == 0:
            raise HTTPException(status_code=404, detail="No books found matching the criteria.")
        return list(return_books)
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the request.")


@app.get("/books/{book_id}" , responses={
    404: {
        "description": "Book not found",
    }
})
async def read_book_by_id(book_id: int):
    for book in BOOKS:
        if book.get('id') == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found.")


@app.post("/books/create_book", responses={
    201: {
        "description": "Book created successfully",
    },
    400: {
        "description": "Invalid book data",
    },
    500: {
        "description": "Internal server error",
    }
})
async def create_book(new_book: Book = Body()):
    try:
        new_book.id = len(BOOKS) + 1
        BOOKS.append(new_book.dict())
        return new_book
    
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=f"Unable to create a book. {e.detail}")