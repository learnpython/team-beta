# -*- coding: utf-8 -

from time import strftime, localtime, gmtime
import os


def app(environ, start_response):
    time_format = '%H:%M:%S'
    local_time = strftime(time_format, localtime())
    gmt_time = strftime(time_format, gmtime())
    user = os.getlogin()
    user_id = os.geteuid()
    browser = environ['HTTP_USER_AGENT']
    response_body = '''
        <html>
        <body>
        Local time: %s<br>
        UTC: %s<br>
        User: %s<br>
        User ID: %s<br>
        User agent: %s
        </body>
        </html>''' % (
        local_time, gmt_time, user, user_id, browser)
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body
