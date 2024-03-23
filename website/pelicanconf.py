AUTHOR = 'PyDataMCR'
SITENAME = 'PyDataMCR'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Set the theme
THEME = "themes/minimal/"

# Static pages of the website that will be generated
TEMPLATE_PAGES = {
    "pages/about-us.html": "about-us.html",
    "pages/404.html": "404.html",
    "pages/sponsorship.html": "sponsorship.html",
}

# Static paths of the website
STATIC_PATHS = ["images"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Settings for the URLs of the blog and the articles
ARTICLE_PATHS = ["events"]
ARTICLE_URL = "events/{slug}/"
ARTICLE_SAVE_AS = "events/{slug}/index.html"
INDEX_SAVE_AS = "events.html"

# Disbale unneeded blog features
ARCHIVES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""

# # Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# # Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = 50

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True