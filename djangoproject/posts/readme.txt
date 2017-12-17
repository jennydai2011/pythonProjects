#django commands

#1.mkvirtualenv py1
#2.workon py1
#3.pip install django
#4.django-admin startproject *projectname
#5. cd into *projectname
#6. code . --> open project in Visual code studio
#7.python manage.py runserver --> run the empty application
#8.pip install mysqlclient
#9. create schema in mysql
#10. python manage.py migrate --> hook up db(create tables)
#11. python manage.py createsuperuser --username=* --email=*
#12. python manage.py startapp *modulename-->create module inside application
#13. add new module into project setting.py INSTALLED_APPS
#14. create urls.py under new module folder
#15. edit views.py to add function（handle request, return response)
#16. create templates folder, add index.html and layout.html
#17. edit models.py for binding variables
#18. python manage.py makemigrations
#19. python manage.py migrate - create new table in db
#20. admin.site.register
#21. add class Meta
#22. add __str__(self)
#23. set url ^$ - default to /posts
