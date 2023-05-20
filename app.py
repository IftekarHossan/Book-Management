from flask import Flask, request, jsonify

app = Flask(__name__)

books = []

# Example book model
def create_book(title, author, id, available=True):
    return {
        'title': title,
        'author': author,
        'id': id,
        'available': available
    }

@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    id = data.get('id')

    book = create_book(title, author, id)
    books.append(book)

    return jsonify({'message': 'Book added successfully'})

@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book['id'] == id:
            return jsonify(book)
    return jsonify({'message': 'Book not found'})

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    for book in books:
        if book['id'] == id:
            book['title'] = data.get('title', book['title'])
            book['author'] = data.get('author', book['author'])
            book['available'] = data.get('available', book['available'])
            return jsonify({'message': 'Book updated successfully'})
    return jsonify({'message': 'Book not found'})

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'message': 'Book not found'})

if __name__ == '__main__':
    app.run(debug=True)


