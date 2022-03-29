from flask import Flask, g  
from flask_restful import Api
from routes import BookList, Book, ReviewList, Review
from flask_cors import CORS
import os
from psycopg2 import pool

BASE_URL = os.environ.get("BASE_URL")
HOST = os.environ.get("HOST")
DATABASE = os.environ.get("DATABASE")
DB_PORT = os.environ.get("DB_PORT")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
MIN = os.environ.get("MIN")
MAX = os.environ.get('MAX')
DEBUG: os.environ.get("DEBUG")

app = Flask(__name__)
CORS(app)

app.config['pSQL_pool'] = pool.SimpleConnectionPool(MIN, MAX,
                                                    host=HOST,
                                                    database=DATABASE,
                                                    port=DB_PORT,
                                                    user=USER,
                                                    password=PASSWORD)

api = Api(app)

# routes

api.add_resource(BookList, f'{BASE_URL}/Books')
api.add_resource(Book, f'{BASE_URL}/Books/<book_id>')
api.add_resource(ReviewList, f'{BASE_URL}/Reviews/<book_id>')
api.add_resource(Review, f'{BASE_URL}/Review/<review_id>')

@app.teardown_appcontext
def close_conn(e):
    db = g.pop('db', None)
    if db is not None:
        app.config['pSQL_pool'].putconn(db)
        print('released connection back to pool')

if __name__ == '__main__':
    app.run(debug=DEBUG)
    
  
