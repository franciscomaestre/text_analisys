#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 17 de oct. de 2016

@author: jhuebra
'''
from __future__ import unicode_literals


import os
LOCALE_PATH = os.path.join(os.path.dirname(__file__), "../app/")


# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# Languages using BiDi (right-to-left) layout
LANGUAGES_BIDI = ["he", "ar", "fa", "ur"]

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
LOCALE_PATHS = []





"""Translation helper functions."""

import gettext as gettext_module
import os
import re
from threading import local

from utils.utils.encoding import force_text
from utils.utils.safestring import SafeData, mark_safe
from utils.utils import six

class TranslatorCommentWarning(SyntaxWarning):
    pass


# Translations are cached in a dictionary for every language.
# The active translations are stored by threadid to make them thread local.
_translations = {}
_active = local()

# The default translation is based on the settings file.
_default = None

# magic gettext number to separate context from message
CONTEXT_SEPARATOR = "\x04"

# Format of Accept-Language header values. From RFC 2616, section 14.4 and 3.9
# and RFC 3066, section 2.1
accept_language_re = re.compile(r'''
        ([A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*|\*)      # "en", "en-au", "x-y-z", "es-419", "*"
        (?:\s*;\s*q=(0(?:\.\d{,3})?|1(?:.0{,3})?))?   # Optional "q=1.00", "q=0.8"
        (?:\s*,\s*|$)                                 # Multiple accepts per header.
        ''', re.VERBOSE)

language_code_re = re.compile(
    r'^[a-z]{1,8}(?:-[a-z0-9]{1,8})*(?:@[a-z0-9]{1,20})?$',
    re.IGNORECASE
)

language_code_prefix_re = re.compile(r'^/([\w@-]+)(/|$)')


def to_locale(language, to_lower=False):
    """
    Turns a language name (en-us) into a locale name (en_US). If 'to_lower' is
    True, the last component is lower-cased (en_us).
    """
    p = language.find('-')
    if p >= 0:
        if to_lower:
            return language[:p].lower() + '_' + language[p + 1:].lower()
        else:
            # Get correct locale for sr-latn
            if len(language[p + 1:]) > 2:
                return language[:p].lower() + '_' + language[p + 1].upper() + language[p + 2:].lower()
            return language[:p].lower() + '_' + language[p + 1:].upper()
    else:
        return language.lower()


def to_language(locale):
    """Turns a locale name (en_US) into a language name (en-us)."""
    p = locale.find('_')
    if p >= 0:
        return locale[:p].lower() + '-' + locale[p + 1:].lower()
    else:
        return locale.lower()


class SeologiesTranslation(gettext_module.GNUTranslations):
    """
    This class sets up the GNUTranslations context with regard to output
    charset.

    This translation object will be constructed out of multiple GNUTranslations
    objects by merging their catalogs. It will construct an object for the
    requested language and add a fallback to the default language, if it's
    different from the requested language.
    """
    def __init__(self, language):
        """Create a GNUTranslations() using many locale directories"""
        gettext_module.GNUTranslations.__init__(self)
        self.set_output_charset('utf-8')  # For Python 2 gettext() (#25720)

        self.__language = language
        self.__to_language = to_language(language)
        self.__locale = to_locale(language)
        self._catalog = None

        self._init_translation_catalog()
        if self.__language == LANGUAGE_CODE and self._catalog is None:
            # default lang should have at least one translation file available.
            raise IOError("No translation files found for default language %s." % LANGUAGE_CODE)
        self._add_fallback()
        if self._catalog is None:
            # No catalogs found for this language, set an empty catalog.
            self._catalog = {}

    def __repr__(self):
        return "<SeologiesTranslation lang:%s>" % self.__language

    def _new_gnu_trans(self, localedir, use_null_fallback=True):
        """
        Returns a mergeable gettext.GNUTranslations instance.

        A convenience wrapper. By default gettext uses 'fallback=False'.
        Using param `use_null_fallback` to avoid confusion with any other
        references to 'fallback'.
        """
        return gettext_module.translation(
            domain='seologies',
            localedir=localedir,
            languages=[self.__locale],
            codeset='utf-8',
            fallback=use_null_fallback)

    def _init_translation_catalog(self):
        """Creates a base catalog using global django translations."""
        localedir = os.path.join(os.path.dirname(LOCALE_PATH), 'locale')
        translation = self._new_gnu_trans(localedir)
        self.merge(translation)


    def _add_fallback(self):
        """Sets the GNUTranslations() fallback with the default language."""
        # Don't set a fallback for the default language or any English variant
        # (as it's empty, so it'll ALWAYS fall back to the default language)
        if self.__language == LANGUAGE_CODE or self.__language.startswith('en'):
            return
        default_translation = translation(LANGUAGE_CODE)
        self.add_fallback(default_translation)

    def merge(self, other):
        """Merge another translation into this catalog."""
        if not getattr(other, '_catalog', None):
            return  # NullTranslations() has no _catalog
        if self._catalog is None:
            # Take plural and _info from first catalog found (generally Django's).
            self.plural = other.plural
            self._info = other._info.copy()
            self._catalog = other._catalog.copy()
        else:
            self._catalog.update(other._catalog)

    def language(self):
        """Returns the translation language."""
        return self.__language

    def to_language(self):
        """Returns the translation language name."""
        return self.__to_language


def translation(language):
    """
    Returns a translation object.
    """
    global _translations
    if language not in _translations:
        _translations[language] = SeologiesTranslation(language)
    return _translations[language]


def activate(language):
    """
    Fetches the translation object for a given language and installs it as the
    current translation object for the current thread.
    """
    if not language:
        return
    _active.value = translation(language)


def deactivate():
    """
    Deinstalls the currently active translation object so that further _ calls
    will resolve against the default translation object, again.
    """
    if hasattr(_active, "value"):
        del _active.value


def deactivate_all():
    """
    Makes the active translation object a NullTranslations() instance. This is
    useful when we want delayed translations to appear as the original string
    for some reason.
    """
    _active.value = gettext_module.NullTranslations()
    _active.value.to_language = lambda *args: None


def get_language():
    """Returns the currently selected language."""
    t = getattr(_active, "value", None)
    if t is not None:
        try:
            return t.to_language()
        except AttributeError:
            pass
    # If we don't have a real translation object, assume it's the default language.
    return LANGUAGE_CODE


def get_language_bidi():
    """
    Returns selected language's BiDi layout.

    * False = left-to-right layout
    * True = right-to-left layout
    """
    lang = get_language()
    if lang is None:
        return False
    else:
        base_lang = get_language().split('-')[0]
        return base_lang in LANGUAGES_BIDI


def catalog():
    """
    Returns the current active catalog for further processing.
    This can be used if you need to modify the catalog or want to access the
    whole message catalog instead of just translating one string.
    """
    global _default

    t = getattr(_active, "value", None)
    if t is not None:
        return t
    if _default is None:
        _default = translation(LANGUAGE_CODE)
    return _default


def do_translate(message, translation_function):
    """
    Translates 'message' using the given 'translation_function' name -- which
    will be either gettext or ugettext. It uses the current thread to find the
    translation object to use. If no current translation is activated, the
    message will be run through the default translation object.
    """
    global _default

    # str() is allowing a bytestring message to remain bytestring on Python 2
    eol_message = message.replace(str('\r\n'), str('\n')).replace(str('\r'), str('\n'))

    if len(eol_message) == 0:
        # Returns an empty value of the corresponding type if an empty message
        # is given, instead of metadata, which is the default gettext behavior.
        result = type(message)("")
    else:
        _default = _default or translation(LANGUAGE_CODE)
        translation_object = getattr(_active, "value", _default)

        result = getattr(translation_object, translation_function)(eol_message)

    if isinstance(message, SafeData):
        return mark_safe(result)

    return result


def gettext(message):
    """
    Returns a string of the translation of the message.

    Returns a string on Python 3 and an UTF-8-encoded bytestring on Python 2.
    """
    return do_translate(message, 'gettext')

if six.PY3:
    ugettext = gettext
else:
    def ugettext(message):
        return do_translate(message, 'ugettext')


def pgettext(context, message):
    msg_with_ctxt = "%s%s%s" % (context, CONTEXT_SEPARATOR, message)
    result = ugettext(msg_with_ctxt)
    if CONTEXT_SEPARATOR in result:
        # Translation not found
        # force unicode, because lazy version expects unicode
        result = force_text(message)
    return result


def gettext_noop(message):
    """
    Marks strings for translation but doesn't translate them now. This can be
    used to store strings in global variables that should stay in the base
    language (because they might be used externally) and will be translated
    later.
    """
    return message


def do_ntranslate(singular, plural, number, translation_function):
    global _default

    t = getattr(_active, "value", None)
    if t is not None:
        return getattr(t, translation_function)(singular, plural, number)
    if _default is None:
        _default = translation(LANGUAGE_CODE)
    return getattr(_default, translation_function)(singular, plural, number)


def ngettext(singular, plural, number):
    """
    Returns a string of the translation of either the singular or plural,
    based on the number.

    Returns a string on Python 3 and an UTF-8-encoded bytestring on Python 2.
    """
    return do_ntranslate(singular, plural, number, 'ngettext')

if six.PY3:
    ungettext = ngettext
else:
    def ungettext(singular, plural, number):
        """
        Returns a unicode strings of the translation of either the singular or
        plural, based on the number.
        """
        return do_ntranslate(singular, plural, number, 'ungettext')


def npgettext(context, singular, plural, number):
    msgs_with_ctxt = ("%s%s%s" % (context, CONTEXT_SEPARATOR, singular),
                      "%s%s%s" % (context, CONTEXT_SEPARATOR, plural),
                      number)
    result = ungettext(*msgs_with_ctxt)
    if CONTEXT_SEPARATOR in result:
        # Translation not found
        result = ungettext(singular, plural, number)
    return result



if __name__ == "__main__":
    
    ## from utils.translation import ugettext as _
    _ = ugettext
    
    # from utils.translation import activate
    activate("es")
    
    print _("Esto se traduce")
    
    pass
