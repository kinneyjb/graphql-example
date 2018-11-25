#!/usr/bin/env python
import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, argument):
        return f"Hello {argument}"


schema = graphene.Schema(query=Query)


result = schema.execute('{ hello }')
print(result.data['hello'])

result = schema.execute('{ hello (argument: "graph") }')
print(result.data['hello'])
