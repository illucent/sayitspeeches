from django.conf import settings

# use custom slugifying function if any
slugify = getattr(settings, 'SLUGGABLE_SLUGIFY_FUNCTION', None)

if not slugify:
    try:
        # python-slugify or awesome-slugify by preference
        from slugify import slugify
    except ImportError:
        try:
            # i18n-friendly approach, but doesn't downcase, collapse whitespace, etc.
            from unidecode import unidecode
            slugify = lambda s: unidecode(s).replace(' ', '-')
        except ImportError:
            try:
                # Cyrillic transliteration (primarily Russian)
                from pytils.translit import slugify
            except ImportError:
                # fall back to Django's default method
                slugify = 'django.template.defaultfilters.slugify'

# find callable by string
if isinstance(slugify, str):
    from django.core.urlresolvers import get_callable
    slugify = get_callable(slugify)


SLUGGABLE_SEPARATOR = getattr(settings, 'SLUGGABLE_SEPARATOR', '-')
