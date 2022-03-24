from models import BookModel, ReviewModel
import psycopg2
import os
from flask import current_app, g



book1 = BookModel('The Hobbit', 'J R R Tolkien', 1)
book2 = BookModel('The Lord Of The Rings', 'J R R Tolkien', 2)
review1 = ReviewModel('a timeless classic', 1)
review2 = ReviewModel('I hated it', 1)
review3 = ReviewModel('an even more timeless classic', 2)
review4 = ReviewModel('I hated it even more', 2)





class Repository():
    
    
    def get_db(self):
       if 'db' not in g:
           g.db = current_app.config['pSQL_pool'].getconn()
       return g.db
           
    
    
    
    def books_get_all(self):
      
       
            conn = self.get_db()
            if (conn):
               ps_cursor = conn.cursor()
               ps_cursor.execute(
               "select title, author, bookId, cover from book order by title")
               book_records = ps_cursor.fetchall()
               book_list = []
               for row in book_records:
                  book_list.append(BookModel(row[0], row[1], row[2], row[3])) 
               ps_cursor.close()
               
            return book_list

       
    
    def book_get_by_id(self, book_id):
       
            conn = self.get_db()
            if(conn):
                 ps_cursor = conn.cursor()
                 ps_cursor.execute("select title, author, bookId, cover from book where bookId =%s",[book_id])
                 row = ps_cursor.fetchone()
                 book = BookModel(row[0], row[1], row[2], row[3])
                 ps_cursor.close()
            return book
       
            
        
            
       
    
    def reviews_get_by_book_id(self, book_id):
       
             conn = self.get_db()
             if(conn):
                 ps_cursor = conn.cursor()
                 ps_cursor.execute("select title, author, bookId, cover from book where bookId =%s",[book_id])
                 row = ps_cursor.fetchone()
                 reviews = [review1,review2,review3,review4]
                 ps_cursor.close()
             return reviews
       
        
       
    
    def review_add(self, data):
       
            conn = self.get_db()
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute("INSERT INTO reviews(title,cover,author)VALUES (%s, %s, %s) RETURNING bookId",(data['title'], data['cover'], data['author']))        
                conn.commit()
                id = ps_cursor.fetchone()[0]
                ps_cursor.close()
                review = ReviewModel(data['content'],id, data['bookId'], data['id'])       
            return review
        
                 
            
    
    def book_add(self, data):
        
            conn = self.get_db()
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute("INSERT INTO book(title,cover,author)VALUES (%s, %s, %s) RETURNING bookId",(data['title'], data['cover'], data['author']))        
                conn.commit()
                id = ps_cursor.fetchone()[0]
                ps_cursor.close()
                book = BookModel(data['title'],id, data['author'], data['cover'])
            return book


        
    


    

    

