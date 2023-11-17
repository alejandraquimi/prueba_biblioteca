# project BIBLIOTECA

## Django

### Database

After that we need the creation of the database that will hold all the information,
to create this database we need to run:

```
> python manage.py makemigrations
```

```
> python manage.py migrate
```

### User creation

superuser run the next command:

```
> python manage.py createsuperuser
```

...
Successfully created the user 'super_admin'

### Run Scripts rol and user

```
> python manage.py crear_roles
```

```
> python manage.py crear_usuarios
```

### Run server

To run the Django's server we start the server with the following options

```
> python manage.py runserver
```
