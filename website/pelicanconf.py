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
    "pages/index.html": "index.html",             # Force the redirect -> about-us
    "pages/about-us.html": "about-us.html",       # Details about PyData
    "pages/sponsorship.html": "sponsorship.html", # Link out to contact form
    "pages/jobs-board.html": "jobs-board.html",   # Job Board
}

# Static paths of the website
STATIC_PATHS = ["images"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Settings for URLs :: Note: Articles = Events
ARTICLE_PATHS = ["events"]                   # The folder in website > content to look for events
ARTICLE_URL = "events/{slug}/"               # The URL redirect for the events
ARTICLE_SAVE_AS = "events/{slug}/info.html"  # The location to save the event information
INDEX_SAVE_AS = "events.html"                # The location to save the list of all events?

# Settings for URLs :: Note: Authors = Jobs
# AUTHOR_PATH = ["jobs"]                         # The folder in website > content to look for jobs
# AUTHOR_URL = "jobs/{slug}/"                    # The URL redirect for the jobs
# AUTHOR_SAVE_AS = "jobs/{slug}/info.html"       # The location to save the job information
# AUTHORS_SAVE_AS = "jobs.html"                  # The location to save the list of all jobs?

# Disable unneeded blog features
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