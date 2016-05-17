from google.appengine.ext import ndb


class Weatherpic (ndb.Model):
    image_url = ndb.StringProperty()
    caption = ndb.StringProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now_add=True)