AUTHOR = 'frontov'
SITENAME = ''
# SITEURL = '/gryadka'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

# THEME = 'simple'
THEME = 'themes/pelican-alchemy/alchemy'
FAVICON = 'images/g.png'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# RFG_FAVICONS = True


# Blogroll
LINKS_WIDGET_NAME = 'мы в запрещенных соцсетях'
# FOOTER_LINKS = (
#     ('огурец', 'https://instagram.com/igushkinm'),
#     ('тыква', 'https://instagram.com/pashutop'),
#     ('баклажан', 'https://instagram.com/shelkanzo'),
#     ('картошка', 'https://instagram.com/fronteno'),
#     ('gryadka', 'https://instagram.com/gryadka_club'),
# )

FOOTER_LINKS = (('telegram', 'https://t.me/gryadka_club'),
         ('instagram', 'https://instagram.com/gryadka_club'),
         )


# Social widget
# SOCIAL_WIDGET_NAME = 'instagram'
# SOCIAL = (('inst', 'https://instagram.com/gryadka_club'),
#           )

DEFAULT_PAGINATION = 100
# NEST_HEADER_IMAGES = 'logo.png'
SITEIMAGE = '/images/logo.png'

STATIC_PATHS = ['images', 'extra/CNAME', 'images/tereskol']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGINS = [
    # ...
    'pelican_youtube',
    # ...
]
