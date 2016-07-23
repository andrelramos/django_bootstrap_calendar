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
    
# Configurations

## Where is showed texts
You may want to change texts of calendar subtitles and buttons, but to do this you need know where are.

 - In project root, has a file called help_texts.py. That stores texts of subtitle on constant `EVENT_CLASS`.
 - In /templatetags/bootstrap_calendar.py you can change texts of buttons on html variable.

## Models
We need store some data to boostrap_calendar works well then you can use BootstrapCalendarModel to ensure that you have this data.

    from django_bootstrap_calendar.models import BootstrapCalendarModel
    class Exemple(BootstrapCalendarModel):
        img = models.ImageField(upload_to='imagens_upload/', null=True, blank=True)
        
With above code, you earn all atributes necessary to work with bootstrap_calendar and an extra field named img. 
Now you are prepared to build a rest API as specified by bootstrap_calendar project (More details: https://github.com/Serhioromano/bootstrap-calendar#feed-url)
