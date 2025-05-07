from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from starlette import status

from typing import Optional

app = FastAPI()

class Book():
    id: int
    title: str
    author: str
    description: str
    rating: int
    year: int

    def __init__ (self, id, title, author, description, rating, year):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.year = year

class BookRequest(BaseModel):
    id: Optional[int] = Field(description = 'ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    year: int = Field(gt=1999, lt=2031)

    # set defulat value
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Test",
                "description": "A new description of the book",
                "rating": 5,
                "year": 2025
            }
        }
    }




BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    
    raise HTTPException(status_code = 404, detail='Item not found')

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(
    book_rating: Optional[int] = Query(gt=0,lt=6,default = None), 
    published_year: Optional[int] = Query(gt=1999,lt=2050,default = None)
    ):
    books_to_return = []
    for book in BOOKS:
        if (book_rating and published_year):
            if book.rating == book_rating and book.year == published_year:
                books_to_return.append(book)
        if(not book_rating and published_year):
            if book.year == published_year:
                books_to_return.append(book)
        if(not published_year and book_rating):
            if book.rating == book_rating:
                books_to_return.append(book)

    if (len(books_to_return) > 0):
        return books_to_return
    
    raise HTTPException(status_code = 404, detail='Item not found')


@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    find_book_id(new_book)
    BOOKS.append(new_book)

    return new_book
    

def find_book_id(book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest, book_id: int = Path(gt=0)):
    book_changed =False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS[i] = book
            book_changed = True
    
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found.')


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int = Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break
    
    if not book_deleted:
        raise HTTPException(status_code=404, detail='Item not found.')

            