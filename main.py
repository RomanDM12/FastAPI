#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/index", tags = ["Пример"])
def index():
	"""Пример простого вызова"""
	return "Hello, World!"

@app.get("/messages", tags = ["Сообщения"])
def messages():
	return {
		"hello": "Формирует приветствие для кого-то",
		"bye": "Формирует прощание для кого-то",
	}

@app.get("/message/hello/{name}", tags = ["Сообщения"])
def hello(name: str) -> str:
	"""Формирует приветствие для кого-то"""
	return f"Hello, {name}"

@app.get("/message/bye{name}", tags = ["Сообщения"])
def bye(name: str) -> str:
	"""Формирует прощание для кого-то"""
	return f"Goodbye, {name}"

