import graphene

class Query(graphene.ObjectType):
    """
    The root Query class for our GraphQL API.
    It defines all the top-level fields that can be queried.
    """
    hello = graphene.String(default_value="Hello, GraphQL!")

# Define the overall schema using our root Query class.
schema = graphene.Schema(query=Query)