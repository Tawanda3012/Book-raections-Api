from models import BookModel, ReviewModel





book1 = BookModel('The Hobbit', 'J R R Tolkien', 1)
book2 = BookModel('The Lord Of The Rings', 'J R R Tolkien', 2)
review1 = ReviewModel('a timeless classic', 1)
review2 = ReviewModel('I hated it', 1)
review3 = ReviewModel('an even more timeless classic', 2)
review4 = ReviewModel('I hated it even more', 2)



class Repository():
    def books_get_all(self):
        return [book1, book2]
    
    def book_get_by_id(self, book_id):
        books=[book1, book2]
        return next((x for x in books if x.bookId == book_id), None)
    
    def reviews_get_by_book_id(self, book_id):
        reviews = [review1,review2,review3,review4]
        return [x for x in reviews if x.bookId == book_id]
    
    def review_add(self, data):
        return ReviewModel(data['content'], data['bookId'], 1)
    
    def book_add(self, data):
        return BookModel(data['title'], data['cover'], 3,data['author'])

    

    

