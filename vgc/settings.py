import os
import warnings
import exceptions

warnings.filterwarnings(
        'ignore', r"DateTimeField .* received a naive datetime",
        RuntimeWarning, r'django\.db\.models\.fields')

from .private_settings import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# fake trans
ugettext = _ = lambda s: s

# This is an utility function for accessing project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)
path = lambda name: os.path.abspath(os.path.join(PROJECT_ROOT, name))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

SECRET_KEY = SECRET_KEY
# CSRF_COOKIE_SECURE = True


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

HTML_MINIFY = True

ALLOWED_HOSTS = ['vgc.com', 'vipgymclub-dev.com']

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard', 
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party
    
    'grappelli',
    'filebrowser',
    'tinymce',
    
    'south',
    
    # project specific
    'core',
    'home',
    'videogallery',
    'photogallery',
    'contacts',
    'mailit',
    'personnel',
    
    
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# debug_toolbar settings
if DEBUG:
    INTERNAL_IPS = ('127.0.0.1','192.168.137.10', '192.168.137.1')
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.profiling.ProfilingDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        #'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

ROOT_URLCONF = 'vgc.urls'

WSGI_APPLICATION = 'vgc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': 'vgc',                      # Or path to database file if using sqlite3.
        # 'USER': 'vgc',                      # Not used with sqlite3.
        # 'PASSWORD': DB_PASSWORD,                  # Not used with sqlite3.
        # 'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        # 'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    # }
    'default': {
         'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
         'NAME': path('vgc.db'),                      # Or path to database file if using sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = path('static')
MEDIA_URL = '/media/'
MEDIA_ROOT = path('media')


# STATICFILES_DIRS = (
    # path('static'), #store site-specific media here.
    # )
TEMPLATE_DIRS = (
    path('templates'),)

# User Image and file settings 
IMG_UPLD_DIR = 'uploaded_images'
FILE_UPLD_DIR = 'uploaded_files'
BANNER_SIZE = (1024, 200)
THUMBNAIL_SIZE = (300, 200) 
ENDLESS_PAGINATION_PER_PAGE = 10
SLIDER_THUMBNAIL_SIZE = (300, 180)
STANDARD_THUMBNAIL_SIZE = (100, 100)
GLRY_THUMB_SIZE = (210, 130)
GLRY_ZOOM_IN_SIZE = (1024, 768)
YOUTUBE_IMAGE_URL = 'http://img.youtube.com/vi/'


TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = STATIC_ROOT + 'tiny_mce'
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = False
TINYMCE_FILEBROWSER = True
TINYMCE_DEFAULT_CONFIG = {
    'skin': "o2k7",
    'plugins': "autolink,lists,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,autosave,visualblocks",
    'theme_advanced_buttons1' : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2' : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
    'theme_advanced_buttons3' : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
    'theme_advanced_buttons4' : "insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak,restoredraft,visualblocks",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : True,
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'file_browser_callback': 'CustomFilebrowser',
    'width': '700',
    'height': '300',
}
# Filebrowser settings
#URL_FILEBROWSER_MEDIA = getattr(settings, "FILEBROWSER_URL_FILEBROWSER_MEDIA", settings.STATIC_URL + "filebrowser/")
#PATH_FILEBROWSER_MEDIA = getattr(settings, "FILEBROWSER_PATH_FILEBROWSER_MEDIA", os.path.join(settings.STATIC_ROOT, 'filebrowser/'))

FILEBROWSER_PATH_TINYMCE = STATIC_ROOT + 'tiny_mce'
FILEBROWSER_URL_TINYMCE = STATIC_URL + 'tiny_mce'
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
    'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p']
}
# Email settings
# EMAIL_HOST_PASSWORD = email_settings['EMAIL_HOST_PASSWORD']
# EMAIL_HOST = 'mail.oosov.org'
# EMAIL_PORT = 26
# DEFAULT_FROM_EMAIL = 'noreply@oosov.org'
# EMAIL_HOST_USER = 'noreply@oosov.org'

# EMAIL_USE_TLS = False

EMAIL_HOST_PASSWORD = email_settings['DEVELOPMENT_EMAIL_HOST_PASSWORD']
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'ognev.victor@gmail.com'
EMAIL_HOST_USER = 'ognev.victor@gmail.com'
EMAIL_USE_TLS = True

SITEMESSAGE_RECEPIENTS = ['ognev.victor@gmail.com',]

