#!/usr/bin/env python

# Author: Ilia Baranov
# Getting Gmail Status, feed to LCD if needed

import feedparser

#https://mail.google.com/mail/u/0/feed/atom

feed = feedparser.parse("https://mail.google.com/mail/u/0/feed/atom")

print feed