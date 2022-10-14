"""
"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message':'Hello World'}

@app.get('/blog/{id}')
def get_blog(id):
    return {'message': f'Blog with id {id}'}
