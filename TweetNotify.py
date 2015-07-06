#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
from gi.repository import Notify
from gi.repository import Gtk

consumer_key= 'GkpqleGNa8rORO6UNDdJs4451'
consumer_secret = 'BfjvtaAIZkPo7Plk6hHzLPvsSM3lXy7VyOR3vptPwoX0mzwfwT'
access_token = '465628371-gEzExM9fc6q3HlJmJ9K6KDmsu3rchqqTjjozvdv3'
access_token_secret= 'JkGjuHfJ7ZNgceg2Zcfji7DdzsNBeqKztosflfWowhRqB'

# définition de la callback exécutée lors du clic sur le bouton
def callback(notif_object, action_name, users_data):
# on peut faire des choses ici
    notif_object.close()
    Gtk.main_quit()

Notify.init ("Tweeter")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    Tweet=Notify.Notification.new ("Tweeter",tweet.text,"messagebox-info")
    # ajout de notre action sur la notification
    Tweet.show ()


