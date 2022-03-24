from flask import Flask
from flask_restful import Api
from routes import BookList, ReviewList, Book, Review
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
MAX = os.environ.get("MAX")


app = Flask(__name__)
CORS(app)


api = Api(app)

app.config['pSQL_pool'] = pool.SimpleConnectionPool(MIN,
                                                    MAX,
                                                    user=USER,
                                                    password=PASSWORD,
                                                    host=HOST,
                                                    port=DB_PORT,
                                                    database=DATABASE)


api.add_resource(BookList, f'{BASE_URL}/Books')
api.add_resource(Book, f'{BASE_URL}/Books/<book_id>')
api.add_resource(ReviewList, f'{BASE_URL}/Reviews/<book_id>')
api.add_resource(Review, f'{BASE_URL}/Review')

@app.teardown_appcontext
def close_conn(e):
    db = g.pop('db', None)
    if db is not None:
       app.config['pSQL_pool'].putconn(db)
       print('released connection back to pool')



if __name__ == '__main__':
    app.run(debug=True)

