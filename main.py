import asyncio

books = {
    "math_book": True  
}


async def borrow_book(user: str, book: str):
    print(f"{user} is trying to borrow {book}...")
    await asyncio.sleep(1)  # simulate delay

    if books.get(book):
        books[book] = False
        print(f"{user} successfully borrowed {book}")
    else:
        print(f"{book} is not available for {user}")


async def return_book(user: str, book: str):
    print(f"{user} is returning {book}...")
    await asyncio.sleep(1)  
    books[book] = True
    print(f"{user} returned {book}")



async def main():
    tasks = [
        borrow_book("jacob", "science_book"),
        borrow_book("clement", "math_book"),
        return_book("isreal", "science_book"),
        borrow_book("fatmata", "Biology_book")
    ]

    await asyncio.gather(*tasks)


asyncio.run(main())