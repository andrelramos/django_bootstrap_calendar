# django_bootstrap_calendar
A simple implementation of https://github.com/Serhioromano/bootstrap-calendar for django

# How to use
After having install this app, add 'django_bootstrap_calendar' to your INSTALLED_APPS.
In head tag of your template, add this:


    {% load bootstrap_calendar %}
    <head>
        <title>Exemple</title>
        
        {% bootstrap_calendar_imports 'en-US' %} <!-- note that you can alter the language from en-US to other supported by the bootstrap-calendar -->
    </head>

Now just load the calendar:

    <body>
       {% bootstrap_calendar 'calendar_id' 'en-US' 'url_for_json_object' %} <!-- you can change all of theses values for your neccessity -->
    </body>
