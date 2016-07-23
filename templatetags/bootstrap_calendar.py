from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django_bootstrap_calendar import help_texts
try:
    from django.utils.encoding import force_unicode as force_text
except ImportError:  # python3
    from django.utils.encoding import force_text
import json

register = template.Library()

@register.simple_tag
def bootstrap_calendar(calendar_id, language, events):
    '''Show the bootstrap-calendar in a template'''

    html = '''
        <div class="pull-right form-inline">
            <div class="btn-group">
                <button class="btn btn-primary" data-calendar-nav="prev"><< Anterior</button>
                <button class="btn" data-calendar-nav="today">Hoje</button>
                <button class="btn btn-primary" data-calendar-nav="next">Próximo >></button>
            </div>
            <div class="btn-group">
                <button class="btn btn-warning" data-calendar-view="year">Ano</button>
                <button class="btn btn-warning" data-calendar-view="month">Mês</button>
                <button class="btn btn-warning" data-calendar-view="week">Semana</button>
                <button class="btn btn-warning" data-calendar-view="day">Dia</button>
            </div>
        </div>
        <br><br>
        <div id="%s"></div>
        %s
    ''' % (calendar_id, help_texts.CLASS_HELP)

    js = '''
        <script>
            $(document).ready(function(){

                var calendar = $("#%(calendar_id)s").calendar({
                    tmpl_path: "%(static_url)sbootstrap_calendar/calendar/tmpls/",
                    events_source: "%(events)s"
                });

                calendar.setLanguage("%(language)s");
                calendar.view();

                $('.btn-group button[data-calendar-nav]').each(function() {
                    var $this = $(this);
                    $this.click(function() {
                        calendar.navigate($this.data('calendar-nav'));
                    });
                });

                $('.btn-group button[data-calendar-view]').each(function() {
                    var $this = $(this);
                    $this.click(function() {
                        calendar.view($this.data('calendar-view'));
                    });
                });
            });
        </script>
    ''' % {
            'calendar_id': calendar_id,
            'static_url': settings.STATIC_URL,
            'events': events,
            'language': language,
        }

    return mark_safe(force_text(html + js))

@register.simple_tag
def bootstrap_calendar_imports(language):
    '''Peforms imports in a page'''

    html = '''
        <link href="%(static_url)sbootstrap_calendar/calendar/css/calendar.min.css" rel="stylesheet">
        <script src="%(static_url)sbootstrap_calendar/calendar/js/calendar.min.js"></script>
        <script src="%(static_url)sbootstrap_calendar/calendar/js/language/%(language)s.js"></script>
        <script src="%(static_url)sunderscore/underscore-min.js"></script>
    ''' % {'static_url': settings.STATIC_URL, 'language': language}

    return mark_safe(force_text(html))
