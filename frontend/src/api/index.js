<<<<<<< HEAD
const url = "http://127.0.0.1:5000/api/bookreactions/";
=======
const url = "process.env.REACT_APP_URL";
>>>>>>> bd98f44 (image upload)

const headers = {
    accept: 'application/json',
    'content-type': 'application/json'
}

export const fetchAllBooks = () => {
    return fetch(url + 'Books').then((response) => {
        return response.json();
    });
}

export const addBook = (book) => {
    return fetch(url + 'Books', 
    {   
        method: 'post',
        mode: 'cors',
        headers: headers,
        body: JSON.stringify(book)
    }).then((response) => {
        return response.json();
    });
}

export const fetchReviews = (bookId) => {
    return fetch(url + "Reviews/" + bookId)
        .then(function (response) {
            return response.json();
        });
}
