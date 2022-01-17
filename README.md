# scheduling_system
the user can create his own available dates do the people can reserve a meeting for that user.


##Recommended Technologies
1.Django 3.x
2.Poetry
3.Postgres version 12.x 

##Runing app
1.python -m venv venv
2.source venv/bin/activate
3.poetry install
4.python manage.py runserver


#queries 

##users queries

###user register
```
mutation {
	register(email:"test1@test.com",username :"testing",password1:"aa12345678",password2:"aa12345678"){
    token
    success
    errors
    
  }
}
```

###user login
```
mutation {
	tokenAuth(password:"1234",username:"alaa") {
	  token
	  success
	  errors
	  unarchiving
	}
}
```


###user create user
```
mutation {
 	createUser(email:"test@test.com",password:"nono1234",username:"testing"){
     user {
       id
     }
   }
}```


##appointments queries
###CRUD Operations
####Create appointment
```
mutation {
	createAppointment(date:"2018-06-29 08:15:27.243860",interval:1){
    appointment {
      id
    }
  }
}
```
####Update appointment
```
mutation {
	updateAppointment(id:1,date:"2018-06-29 08:15:27.243860",interval:1){
    appointment {
      id
      date
    }
  }
}
```
####Delete appointment
```
mutation {
	deleteAppointment(id:27){
    ok
  }
}
```
####get appointment
```
query{
    appointments {
      id
      interval
    }
}
```




##reservation queries
###create reservation 
```
mutation {
  createReservation(appointmentId: 28, email: "user@mail.com", username: "user") {
    reservation {
      id
    }
  }
}
```




