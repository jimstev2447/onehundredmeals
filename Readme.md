
100 meals
---------
A blog about food...

To use sqlite3 locally:
-----------------------
Copy the settings file and save as local_settings.py
Replace DATABASES with:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

And remove lines:

    import dj_database_url
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
    try:
        from .local_settings import *
    except ImportError:
        pass

To run the app: 

    ./manage.py runserver --settings=onehundredmeals.local_settings


