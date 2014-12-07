#!/usr/bin/python
# -*- coding: utf-8 -*-

from evernote.api.client import EvernoteClient

dev_token = "S=s1:U=8fc2a:E=150a5efbf8d:C=1494e3e92a0:P=1cd:A=en-devtoken:V=2:H=05d3a244b14e316a712279a27211ee7a"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username
