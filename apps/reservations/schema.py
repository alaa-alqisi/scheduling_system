from django.utils import timezone
from graphene_django import DjangoObjectType
from apps.users.models import User 
from apps.reservations.models import Reservation 
from apps.appointments.models import Appointment

import graphene

class ReservationType(DjangoObjectType):
    class Meta:
        model=Reservation



class MyException(Exception):
    pass
class CreateReservation(graphene.Mutation):
    reservation = graphene.Field(ReservationType )
   
    class Arguments:
        appointment = graphene.Int()
        username = graphene.String()
        email = graphene.String()


    def mutate(self,info,appointment,username,email):
        newReservation = Reservation(full_name=username,email=email)

        checkReservation = Reservation.objects.filter(appointment=appointment).exists()

        if checkReservation:
            raise MyException('Reservation alreay taken')

            
        appo = Appointment.objects.get(id=appointment)
        newReservation.appointment = appo
        newReservation.save()


        return CreateReservation(appointment=newReservation)


