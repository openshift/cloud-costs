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

    # <Expression u"'<Hello world>'" (1:2)> -> _content_139955154988272
    try:
        _content_139955154988272 = '<Hello world>'
    except:
        rcontext.setdefault('__error__', []).append((u"'<Hello world>'", 1, 2, '<string>', _sys.exc_info()[1], ))
        raise

    if (_content_139955154988272 is not None):
        _tt = type(_content_139955154988272)
        if ((_tt is int) or (_tt is float) or (_tt is long)):
            _content_139955154988272 = str(_content_139955154988272)
        else:
            if (_tt is str):
                _content_139955154988272 = decode(_content_139955154988272)
            else:
                if (_tt is not unicode):
                    try:
                        _content_139955154988272 = _content_139955154988272.__html__
                    except AttributeError:
                        _content_139955154988272 = convert(_content_139955154988272)
                    else:
                        _content_139955154988272 = _content_139955154988272()
    _content_139955154988272 = ('%s%s' % ((_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u'<&>\n' if (u'<&>\n' is not None) else ''), ))
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass