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
    translation_score = []
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
    for keyy, valuee in new_json.items():  # dictionary/JSON
        for list1 in valuee:  # first list
            for item in list1:  # second list
                for key, value in item.items():  # dictionaries
                    if key == 'translation':
                        translation_list.append(value)  # append translation data in a list
                    if key == 'translation_score':
                        translation_score.append(value)    # append translation_score data in a list
    #translation_list = [x.encode('utf-8') for x in translation_list]
    zipped = zip(translation_list, translation_score)
    return zipped, json_response


def index(request):
    if request.GET.get('search'):
        message = request.GET.get('search')
        result, json = translator_request(message)
        return render(request, 'labs_form.html', {
            'search': message, 'result': result, 'raw_json': json,
        })

    else:
        #result = ''
        return render(request, 'labs_form.html', {
            #'result': result,
            })
