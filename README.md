MailSnake-GAE
=============
Python wrapper for MailChimp API 3.0 for Google App Engine.

Usage
=====
    >>> from mailsnake import MailSnake 
    >>> ms = MailSnake('YOUR MAILCHIMP API KEY')
    >>> ms.resource(**params)
    u "Everything's Chimpy!"

Note
====
API parameters must be passed by name. For example:

    >>> ms.lists(id='YOUR LIST ID', resource=['members'], post_data=post_data, method_type=urlfetch.POST)

MailChimp API v3.0 documentation
================================
http://kb.mailchimp.com/api/?utm_source=apidocs&utm_medium=internal_ad&utm_campaign=api_v3


Created by: John-Kim Murphy (https://github.com/leftium)
Converted to 3.0 on App Engine by: Tadeu Luis Pires Gaudio @anestesya
