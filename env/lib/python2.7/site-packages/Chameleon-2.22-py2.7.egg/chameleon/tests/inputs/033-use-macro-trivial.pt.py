# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
import re
import functools
_marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def render(stream, econtext, rcontext):
    append = stream.append
    getitem = econtext.__getitem__
    get = econtext.get
    _i18n_domain = None
    re_amp = g_re_amp
    re_needs_escape = g_re_needs_escape
    decode = getitem('decode')
    convert = getitem('convert')
    translate = getitem('translate')

    # <Expression u"load('032-master-template.pt').macros['main']" (1:23)> -> _macro
    try:
        _macro = getitem('load')('032-master-template.pt').macros['main']
    except:
        rcontext.setdefault('__error__', []).append((u"load('032-master-template.pt').macros['main']", 1, 23, '<string>', _sys.exc_info()[1], ))
        raise

    _macro.include(stream, econtext.copy(), rcontext)
    econtext.update(rcontext)
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass