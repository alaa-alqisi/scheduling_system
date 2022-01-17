from django.utils import timezone
from graphene_django import DjangoObjectType
from apps.users.models import User 
from apps.reservations.models import Reservation 

import graphene

class ReservationType(DjangoObjectType):
    class Meta:
        model=Reservation




class CreateReservation(graphene.Mutation):
    reservation = graphene.Field(ReservationType )
   
    class Arguments:
        appointment = graphene.Int()
        username = graphene.String()
        email = graphene.String()


    def mutate(self,info,appointment,username,email):
        c = Reservation(full_name=username,email=email)
        c.appointment =appo
        c.save()


        return CreateReservation(appointment=c)


