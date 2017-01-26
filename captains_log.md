100 meals
=========
Alpha-0.0.1
----------
functional requirements:
------------------------
* As a guest I want to be able to…
* See a list of meals with a photo and title.
* When i click on a meal, I want the panel to open with more info. 
* I want the panel to have two tabs (ingredients, method).
* I want to be able to switch tabs.
* I want to be able to close the panel with an ‘X’ in the corner.

DONE:
-----
*JIM-00*
Make github repo on Jim’s account.

*JIM-0*
Set up local environment
Python 
Virtualenv (explain)
Pip
    `pip install django`

*JIM-1*
Install pycharm ide

*JIM-2*
Create a new django project
    `django-admin startproject onehundredmeals`

*JIM-3*
Made first PR
    `git checkout master` #copy code from github
    `git pull origin master` #make sure it’s uptodate
    `git checkout -b JIM-6` #make a new branch locally (copy of master)
    //code changes
    `git add -A` #add all changes to branch JIM-6
    `git commit -m “I did a thing”` #commit changes to branch JIM-6
    `git push origin JIM-6` #push branch JIM-6 to github
Go to github and create a new PR

*JIM-4*
Added a new app to django project
Added a view called hello
    `django-admin startapp hello`
    
 *JIM-5*
Added unit test
Ran test using `./manage test`
Made second PR

*JIM-6/7*
Add Travis - continuous integration
Added .travis.yml file in root
Added requirements.txt to store dependencies needed to run the app.
Git commit d38e775501de996aa2bf63fc867947fc508f6ce2

*JIM-8*
Added stuff needed to deploy to heroku
Commit no. 80dad3e096fa7d54ca84d2d2edcf23aaf2afc18b
Procfile: `web: gunicorn onehundredmeals.wsgi`
In settings.py:
`import dj_database_url`
`SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')`
`DEBUG = False`
`ALLOWED_HOSTS = ['*']`
`try:
    from .local_settings import *
 except ImportError:
    pass`
`db_from_env = dj_database_url.config(conn_max_age=500)`
`DATABASES['default'].update(db_from_env)`
`STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'`
Changed sqlite3 with postgresql
In Wsgi.py:
`from whitenoise.django import DjangoWhiteNoise`
`application = DjangoWhiteNoise(application)`
`os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onehundredmeals.settings")`
In Requirements.txt:
`dj-database-url==0.4.2`
`Django==1.10.5`
`gunicorn==19.6.0`
`whitenoise==3.2.3`
`psycopg2==2.6.2`
Added runtime.txt:
`python-3.5.2`
Added local_settings.py so we can run sqllite3 locally and postgresql on heroku.



