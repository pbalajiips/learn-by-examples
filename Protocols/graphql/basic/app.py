from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    def resolve_hello(self, info, name):
        return f"Hello, {name}!"

class AddNumbers(graphene.Mutation):
    class Arguments:
        a = graphene.Int(required=True)
        b = graphene.Int(required=True)

    result = graphene.Int()

    def mutate(self, info, a, b):
        return AddNumbers(result=a + b)

class Mutation(graphene.ObjectType):
    add_numbers = AddNumbers.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

@app.route('/playground')
def playground():
    return jsonify({'message': 'Use /graphql endpoint for GraphQL queries'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
