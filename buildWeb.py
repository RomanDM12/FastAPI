from fastapi import FastAPI
import uvicorn
import json

#Init
app = FastAPI(debug = True)

#Data
with open("works.json") as f:
	books = json.load(f)



#Route
@app.get('/api/v2/books')
async def get_books():
	return {"books": books}

@app.get('/api/v2/books/{title}')
async def get_book(title: str) -> str:
	book = [book for book in book if book["title"] == title]
	return {"books": book}

if __name__ == '__main__':
	uvicorn.run(app, host = "127.0.0.1", port = "7500")