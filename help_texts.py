EVENT_CLASS = (
    ('event-important', 'Importante'),
    ('event-success', 'Sucesso'),
    ('event-warning', 'Cuidado'),
    ('event-info', 'Informação'),
    ('event-inverse', 'Inverso'),
    ('event-special', 'Especial'),
)

CLASS_HELP = '''
                <h4>TIPOS DE EVENTOS <span class="label label-default">LEGENDA</span></h4>
                <ul class="list-group" style="width:180px">
                    <li class="list-group-item">%s <span class="pull-left event event-important"></li>
                    <li class="list-group-item">%s <span class="pull-left event event-success"></li>
                    <li class="list-group-item">%s <span class="pull-left event event-warning"></li>
                    <li class="list-group-item">%s <span class="pull-left event event-info"></li>
                    <li class="list-group-item">%s <span class="pull-left event event-inverse"></li>
                    <li class="list-group-item">%s <span class="pull-left event event-special"></li>
                </ul>
                <br>
            ''' % (EVENT_CLASS[0][1],
                   EVENT_CLASS[1][1],
                   EVENT_CLASS[2][1],
                   EVENT_CLASS[3][1],
                   EVENT_CLASS[4][1],
                   EVENT_CLASS[5][1],)
