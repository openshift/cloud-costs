# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_39103696 = {u'href': u'http://repoze.org', u'id': u'link-id', u'rel': u'self', }
_static_39100880 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
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
    _backup_attrs_37098488 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x254a1d0> name=None at 254a7d0> -> _value
    _value = _static_39100880
    econtext['attrs'] = _value

    # <div ... (1:0)
    # --------------------------------------------------------
    append(u'<div')
    _attr_xmlns = u'http://www.w3.org/1999/xhtml'
    if (_attr_xmlns is not None):
        append((u' xmlns="%s"' % _attr_xmlns))
    append(u'>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36810832 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x254acd0> name=None at 254ab10> -> _value
    _value = _static_39103696
    econtext['attrs'] = _value

    # <a ... (3:2)
    # --------------------------------------------------------
    append(u'<a')
    _attr_rel = u'self'
    if (_attr_rel is not None):
        append((u' rel="%s"' % _attr_rel))
    _backup_default_36710736 = get('default', _marker)
    _value = u'http://repoze.org'
    econtext['default'] = _value

    # <Expression u"'http://python.org'" (4:26)> -> _attr_href
    try:
        _attr_href = 'http://python.org'
    except:
        rcontext.setdefault('__error__', []).append((u"'http://python.org'", 4, 26, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_href is None):
        pass
    else:
        if (_attr_href is False):
            _attr_href = None
        else:
            _tt = type(_attr_href)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_href = unicode(_attr_href)
            else:
                try:
                    if (_tt is str):
                        _attr_href = decode(_attr_href)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_href = _attr_href.__html__
                            except:
                                _attr_href = convert(_attr_href)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_href = _attr_href()
                else:
                    if ((_attr_href is not None) and (re_needs_escape(_attr_href) is not None)):
                        if ('&' in _attr_href):
                            if (';' in _attr_href):
                                _attr_href = re_amp.sub('&amp;', _attr_href)
                            else:
                                _attr_href = _attr_href.replace('&', '&amp;')
                        if ('<' in _attr_href):
                            _attr_href = _attr_href.replace('<', '&lt;')
                        if ('>' in _attr_href):
                            _attr_href = _attr_href.replace('>', '&gt;')
                        if (u'"' in _attr_href):
                            _attr_href = _attr_href.replace(u'"', '&#34;')
    if (_attr_href is not None):
        append((u' href="%s"' % _attr_href))
    if (_backup_default_36710736 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36710736
    _attr_id = u'link-id'
    if (_attr_id is not None):
        append((u' id="%s"' % _attr_id))
    append(u' />')
    if (_backup_attrs_36810832 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36810832
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_37098488 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_37098488
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass