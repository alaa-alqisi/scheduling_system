# from django.utils import timezone
from apps.reservations.models import Reservation
from graphene_django import DjangoObjectType
from apps.users.models import User 
from apps.appointments.models import Appointment
from apps.appointments.schema import(
    CreateAppointment, 
    DeleteAppointment,
    UpdateAppointment,
    AppointmentType
)
from apps.reservations.schema import  (

    CreateReservation,
    ReservationType
)

from apps.users.schema import (UserType,CreateUser)
from graphql_auth.schema import UserQuery,MeQuery
from graphql_auth import mutations
import graphql_jwt
import graphene
from graphql_jwt.decorators import login_required

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Mutation(AuthMutation,graphene.ObjectType):
    create_appointment = CreateAppointment.Field()
    delete_appointment = DeleteAppointment.Field()
    update_appointment = UpdateAppointment.Field()
    create_reservation = CreateReservation.Field();
    create_user = CreateUser.Field()
    register = mutations.Register.Field()




class Query(UserQuery,MeQuery, graphene.ObjectType):
    users = graphene.List(UserType)
    appointments = graphene.List(AppointmentType)
    reservations = graphene.List(ReservationType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_reservations(self, info):
        return Reservation.objects.all()

    @login_required
    def resolve_appointments(self, info):
        user = info.context.user

        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        return Appointment.objects.all()




schema = graphene.Schema(query=Query,mutation=Mutation )