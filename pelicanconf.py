AUTHOR = 'frontov'
SITENAME = 'gryadka'
# SITEURL = '/gryadka'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

THEME = 'notmyidea'
FAVICON = 'images/g.png'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = False


# Blogroll
LINKS_WIDGET_NAME = 'мы в запрещенных соцсетях'
LINKS = (('картошка', 'https://instagram.com/fronteno'),
         ('огурец', 'https://instagram.com/igushkinm'),
         ('тыква', 'https://instagram.com/pashutop'),
         ('баклажан', 'https://instagram.com/shelkanzo'),
         ('gryadka', 'https://instagram.com/gryadka_rc'),
         )



# Social widget
# SOCIAL_WIDGET_NAME = 'instagram'
# SOCIAL = (('inst', 'https://instagram.com/gryadka_rc'),
#           )

DEFAULT_PAGINATION = 10
NEST_HEADER_IMAGES = 'logo.png'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True