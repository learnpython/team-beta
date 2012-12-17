# -*- coding: utf-8 -

from time import strftime, localtime, gmtime
import os


def app(environ, start_response):
    time_format = '%H:%M:%S'
    local_time = strftime(time_format, localtime())
    gmt_time = strftime(time_format, gmtime())
    user = os.getlogin()
    response_body = 'Local time: %s\nUTC: %s\nUser: %s' % (
        local_time, gmt_time, user)
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]
