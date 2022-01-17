from django.utils import timezone
from graphene_django import DjangoObjectType
from apps.users.models import User 
from apps.appointments.models import Appointment 
import re
import graphene
from datetime import datetime
class AppointmentType(DjangoObjectType):
    class Meta:
        model=Appointment

class CreateAppointment(graphene.Mutation):
    appointment = graphene.Field(AppointmentType )
   
    class Arguments:
        date = graphene.String()
        interval = graphene.Int()

    def mutate(self,info,date,interval):
        c = Appointment(date=datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f'),interval=interval)
        c.user = info.context.user

        c.save()


        return CreateAppointment(appointment=c)


class DeleteAppointment(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()



    def mutate(self,info,id):
        appo = Appointment.objects.get(id=id)
        appo.delete()


        return DeleteAppointment(ok=True)


class UpdateAppointment(graphene.Mutation):
    card = graphene.Field(AppointmentType )

    class Arguments:
        id = graphene.Int()
        date = graphene.String()
        interval = graphene.String()

    def mutate(self,info,id,date,interval):
        c = Appointment.objects.get(id=id)


        # if date:
        c.date=date

        c.interval=interval
        c.save()

        return UpdateAppointment(Appointment=c)





