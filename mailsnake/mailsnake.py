#!/usr/bin/env python
# coding=utf-8
__author__ = 'tadgaudio@gmail.com (Tadeu luis Pires Gaudio)'

from google.appengine.api import urlfetch
import logging
import json

mailchimp_api_url = 'https://us8.api.mailchimp.com/3.0/'
mailchimp_api_key = 'f85e562bed97acd14553615c3d9215a7-us8'
list_id = ''

def mailchimp_subscribe(list_id=None, post_data={}):
    """
    Subscribes this email to your mailchimp newsletter. If list_id is not
    set it will default to settings.MAILCHIMP_LIST_ID.
    """
    #config = webapp2.get_app().config.get('mailchimp_api_key')
    ms = MailSnake(mailchimp_api_key)
    list_id = list_id or list_id
    res = ms.lists(id=list_id, resource=['members'], post_data=post_data, method_type=urlfetch.POST)
    logging.info("MailChimp: Subscribed. Result: %s" % res)
    return res

class MailSnake(object):
    """
    MailSnake is a simple MailChimp API Wrapper.
    - URL: https://github.com/leftium/mailsnake
    - Author: John-Kim Murphy (https://github.com/leftium)
    - Update By: Tadeu Luis Pires Gaudio
    """
    def __init__(self, apikey='', extra_params={}):
        if not apikey:
            raise ValueError("MailChimp API Key not valid. Set in settings.py")

        self.apikey = apikey
        self.default_params = {'apikey': apikey}
        self.default_params.update(extra_params)
        self.base_api_url = mailchimp_api_url

    def call(self, method, params={}):
        url = self.base_api_url + method
        params.update(self.default_params)

        post_data = json.dumps(params['post_data'])
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        headers['Authorization'] = 'apikey %s' % self.apikey

        result = urlfetch.fetch(url=url,
            payload=post_data,
            method=params['method_type'],
            headers=headers)

        return json.loads(result.content)

    def __getattr__(self, method_name):
        def get(self, *args, **kwargs):
            params = dict((i, j) for (i, j) in enumerate(args))
            params.update(kwargs)
            _method_name = method_name+'/'+params['id']
            if params['resource']:
                for resource in params['resource']:
                    _method_name = _method_name + '/' + resource

            return self.call(_method_name, params)

        return get.__get__(self)
