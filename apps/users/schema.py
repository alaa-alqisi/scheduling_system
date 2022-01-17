# from django.utils import timezone
from graphene_django import DjangoObjectType
from apps.users.models import User


import graphene




class UserType(DjangoObjectType):
    class Meta:
        model = User


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String()
        password = graphene.String()
        username = graphene.String()


    def mutate(self,info,email,password,username):
        currentUser = User(email=email,password=password)
        # c.user = request.user
        currentUser.save()
        print(currentUser)

        return CreateUser(user=currentUser)