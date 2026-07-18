from flask import Flask
from flask_graphql import GraphQLView
import graphene

books_data = [
    {"id": "1", "title": "The Sunlyn Guide", "author": "A. Author", "year": 2026},
    {"id": "2", "title": "Kubernetes Patterns", "author": "B. Builder", "year": 2024},
]

class Book(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    year = graphene.Int()

class Query(graphene.ObjectType):
    books = graphene.List(Book)
    book = graphene.Field(Book, id=graphene.ID(required=True))

    def resolve_books(self, info):
        return books_data

    def resolve_book(self, info, id):
        return next((book for book in books_data if book["id"] == id), None)

class AddBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        year = graphene.Int(required=True)

    book = graphene.Field(Book)

    def mutate(self, info, title, author, year):
        new_book = {"id": str(len(books_data)+1), "title": title, "author": author, "year": year}
        books_data.append(new_book)
        return AddBook(book=new_book)

class Mutation(graphene.ObjectType):
    add_book = AddBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
