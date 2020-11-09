# Person library
For getting started:
1. pip install -r requirements.txt
2. in folder which contains _manage.py_ use `py manage.py runserver`.
After that u will get the following urls:

  1.  http://127.0.0.1:8000/ - List of books
  2.  http://127.0.0.1:8000/index/ - Infomation about library, and 2 addition homeworks
  3.  http://127.0.0.1:8000/redactions/ - Which redactions the books belong to
  4.  http://127.0.0.1:8000/admin/ - Administrator panel
  
For use administrator panel use `py manage.py createsuperuser`

NOTE:
  U can delete database, and after command makemigrations create new, but i'm add 2 redactions, ENG / RU for check homework specially.
```
***Superuser data***
login: ekke
pass: 1
********************
```
