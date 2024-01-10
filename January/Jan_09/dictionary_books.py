# Create an empty dictionary to store book information
books_dict = {}

# Add books to the dictionary
books_dict['book1'] = {
    'title': 'The Catcher in the Rye',
    'author': 'J.D. Salinger',
    'publication_year': 1951
}

books_dict['book2'] = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'publication_year': 1960
}

books_dict['book3'] = {
    'title': '1984',
    'author': 'George Orwell',
    'publication_year': 1949
}

# Retrieve book details using dictionary methods
book1_details = books_dict.get('book1')
book2_details = books_dict.get('book2')
book3_details = books_dict.get('book3')

if book1_details:
    print("Book 1 Details:")
    print(f"Title: {book1_details['title']}")
    print(f"Author: {book1_details['author']}")
    print(f"Publication Year: {book1_details['publication_year']}")
else:
    print("Book 1 not found in the dictionary")

# Update book details using dictionary methods
if 'book2' in books_dict:
    books_dict['book2']['publication_year'] = 1962
    print("Updated Book 2 Publication Year to 1962")

# Print the updated book details
if 'book2' in books_dict:
    book2_details = books_dict['book2']
    print("Updated Book 2 Details:")
    print(f"Title: {book2_details['title']}")
    print(f"Author: {book2_details['author']}")
    print(f"Publication Year: {book2_details['publication_year']}")
