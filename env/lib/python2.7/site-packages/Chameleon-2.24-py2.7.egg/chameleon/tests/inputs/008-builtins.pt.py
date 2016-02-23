# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_35829392 = {}
_static_36669456 = {}
_static_36669712 = {u'class': u'static', }
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
    _backup_attrs_35754928 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222b690> name=None at 222bb50> -> _value
    _value = _static_35829392
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35872992 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8810> name=None at 22f8210> -> _value
    _value = _static_36669456
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')

    # <Expression u'nothing' (3:6)> -> _content_139955154988272
    try:
        _content_139955154988272 = getitem('nothing')
    except:
        rcontext.setdefault('__error__', []).append((u'nothing', 3, 6, '<string>', _sys.exc_info()[1], ))
        raise

    if (_content_139955154988272 is None):
        pass
    else:
        if (_content_139955154988272 is False):
            _content_139955154988272 = None
        else:
            _tt = type(_content_139955154988272)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _content_139955154988272 = unicode(_content_139955154988272)
            else:
                try:
                    if (_tt is str):
                        _content_139955154988272 = decode(_content_139955154988272)
                    else:
                        if (_tt is not unicode):
                            try:
                                _content_139955154988272 = _content_139955154988272.__html__
                            except:
                                _content_139955154988272 = convert(_content_139955154988272)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _content_139955154988272 = _content_139955154988272()
                else:
                    if ((_content_139955154988272 is not None) and (re_needs_escape(_content_139955154988272) is not None)):
                        if ('&' in _content_139955154988272):
                            if (';' in _content_139955154988272):
                                _content_139955154988272 = re_amp.sub('&amp;', _content_139955154988272)
                            else:
                                _content_139955154988272 = _content_139955154988272.replace('&', '&amp;')
                        if ('<' in _content_139955154988272):
                            _content_139955154988272 = _content_139955154988272.replace('<', '&lt;')
                        if ('>' in _content_139955154988272):
                            _content_139955154988272 = _content_139955154988272.replace('>', '&gt;')
                        if ('\x00' in _content_139955154988272):
                            _content_139955154988272 = _content_139955154988272.replace('\x00', '&#34;')
    _content_139955154988272 = ('%s%s%s' % ((u'\n    ' if (u'\n    ' is not None) else ''), (_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u'\n    ' if (u'\n    ' is not None) else ''), ))
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_35755576 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8910> name=None at 22f8f10> -> _value
    _value = _static_36669712
    econtext['attrs'] = _value

    # <div ... (4:4)
    # --------------------------------------------------------
    append(u'<div')
    _backup_default_35755720 = get('default', _marker)
    _value = u'static'
    econtext['default'] = _value

    # <Expression u'string:dynamic' (4:31)> -> _attr_class
    try:
        _attr_class = u'dynamic'
    except:
        rcontext.setdefault('__error__', []).append((u'string:dynamic', 4, 31, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_class is None):
        pass
    else:
        if (_attr_class is False):
            _attr_class = None
        else:
            _tt = type(_attr_class)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_class = unicode(_attr_class)
            else:
                try:
                    if (_tt is str):
                        _attr_class = decode(_attr_class)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_class = _attr_class.__html__
                            except:
                                _attr_class = convert(_attr_class)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_class = _attr_class()
                else:
                    if ((_attr_class is not None) and (re_needs_escape(_attr_class) is not None)):
                        if ('&' in _attr_class):
                            if (';' in _attr_class):
                                _attr_class = re_amp.sub('&amp;', _attr_class)
                            else:
                                _attr_class = _attr_class.replace('&', '&amp;')
                        if ('<' in _attr_class):
                            _attr_class = _attr_class.replace('<', '&lt;')
                        if ('>' in _attr_class):
                            _attr_class = _attr_class.replace('>', '&gt;')
                        if (u'"' in _attr_class):
                            _attr_class = _attr_class.replace(u'"', '&#34;')
    if (_attr_class is not None):
        append((u' class="%s"' % _attr_class))
    if (_backup_default_35755720 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_35755720
    append(u'>')

    # <Expression u"attrs['class']" (5:8)> -> _content_139955154988272
    try:
        _content_139955154988272 = getitem('attrs')['class']
    except:
        rcontext.setdefault('__error__', []).append((u"attrs['class']", 5, 8, '<string>', _sys.exc_info()[1], ))
        raise

    if (_content_139955154988272 is None):
        pass
    else:
        if (_content_139955154988272 is False):
            _content_139955154988272 = None
        else:
            _tt = type(_content_139955154988272)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _content_139955154988272 = unicode(_content_139955154988272)
            else:
                try:
                    if (_tt is str):
                        _content_139955154988272 = decode(_content_139955154988272)
                    else:
                        if (_tt is not unicode):
                            try:
                                _content_139955154988272 = _content_139955154988272.__html__
                            except:
                                _content_139955154988272 = convert(_content_139955154988272)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _content_139955154988272 = _content_139955154988272()
                else:
                    if ((_content_139955154988272 is not None) and (re_needs_escape(_content_139955154988272) is not None)):
                        if ('&' in _content_139955154988272):
                            if (';' in _content_139955154988272):
                                _content_139955154988272 = re_amp.sub('&amp;', _content_139955154988272)
                            else:
                                _content_139955154988272 = _content_139955154988272.replace('&', '&amp;')
                        if ('<' in _content_139955154988272):
                            _content_139955154988272 = _content_139955154988272.replace('<', '&lt;')
                        if ('>' in _content_139955154988272):
                            _content_139955154988272 = _content_139955154988272.replace('>', '&gt;')
                        if ('\x00' in _content_139955154988272):
                            _content_139955154988272 = _content_139955154988272.replace('\x00', '&#34;')
    _content_139955154988272 = ('%s%s%s' % ((u'\n      ' if (u'\n      ' is not None) else ''), (_content_139955154988272 if (_content_139955154988272 is not None) else ''), (u'\n    ' if (u'\n    ' is not None) else ''), ))
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_35755576 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35755576
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_35872992 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35872992
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_35754928 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_35754928
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass