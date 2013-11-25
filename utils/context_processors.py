from django.conf import settings
from django.contrib.sites.models import Site

from menu_control.models import MenuItem



def project_constants(HttpRequest):
    site_name = Site.objects.get(id=settings.SITE_ID)
    return {'STATIC_URL': settings.STATIC_URL,
            'IMG_UPLD_DIR': settings.IMG_UPLD_DIR,
            'site_name': site_name
            }


def menu_variables(HttpRequest):
    menu_items = MenuItem.objects.values(
        'title', 'short_descr', 'section', 'side', 'content__slug'
    )
    result = {
        MenuItem.ABOUT: {
            MenuItem.LEFT: [],
            MenuItem.RIGHT: []
        },
        MenuItem.ARTICLES: {
            MenuItem.LEFT: [],
            MenuItem.RIGHT: []
        }
    }

    for item in menu_items:
        result[item["section"]][item["side"]].append(item)

    return {
        'menu_about_left': result[MenuItem.ABOUT][MenuItem.LEFT],
        'menu_about_right': result[MenuItem.ABOUT][MenuItem.RIGHT],
        'menu_articles_left': result[MenuItem.ARTICLES][MenuItem.LEFT],
        'menu_articles_right': result[MenuItem.ARTICLES][MenuItem.RIGHT],
    }
