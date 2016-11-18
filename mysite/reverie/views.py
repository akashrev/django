#!/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
import datetime
from django.http import HttpResponse
import requests, json

# Create your views here.
'''

def reverie_labs(request):
    now = datetime.datetime.now()
    return render(request, 'labs_form.html', {'current_date': now})


def search(request):
    if 'q' in request.GET and request.GET['q']:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

'''

def translator_request(message):
    engine_list = []
    translation_list = []
    #message = "Buy puma casual shoes at a discount of 50 at select stores."
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    def data():
        return {
            "data": [
                message
            ]
        }

    response = requests.post('http://52.163.231.207:8000/translator/', headers=headers, json=data())
    json_response = json.dumps(response.json(), ensure_ascii=False, indent=4, sort_keys=True).encode('utf-8')
    #return json_response
    new_json = json.loads(json_response)
    # print new_json
    for key, value in new_json.items():  # dictionary/JSON
        for list1 in value:  # first list
            for item in list1:  # second list
                for key, value in item.items():  # dictionaries
                    if key == 'engine':
                        engine_list.append(value)
                        #return engine_list
                    if key == 'translation':
                        translation_list.append(value)
    engine_list = [x.encode('utf-8') for x in engine_list]
    translation_list = [x.encode('utf-8') for x in translation_list]
    zipped = zip(engine_list, translation_list)
    return zipped, json_response

def index(request):
    #message1 = []
    #message2 = []
    if request.GET.get('search'):
        message = request.GET.get('search')
        result , json = translator_request(message)
        return render(request, 'labs_form.html', {
            'search': message, 'result': result, 'raw_json': json,
            #        'engine': message1, 'translation': message2,
        })

    else:
        result = 'You submitted an empty form.'
        return render(request, 'labs_form.html', {
            'result': result,
            })
