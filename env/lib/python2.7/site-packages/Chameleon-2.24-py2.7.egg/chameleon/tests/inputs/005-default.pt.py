# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_35707984 = {}
_static_35803088 = {}
_static_36671184 = {}
_static_35779600 = {}
_static_36670416 = {u'class': u'default', }
_static_36668432 = {u'class': u'default', }
_static_35802384 = {}
_marker_default = _Placeholder()
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
    _backup_attrs_38643400 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2224d10> name=None at 2224a10> -> _value
    _value = _static_35802384
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38494936 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2224fd0> name=None at 2224290> -> _value
    _value = _static_35803088
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38642320 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8410> name=None at 2224dd0> -> _value
    _value = _static_36668432
    econtext['attrs'] = _value

    # <img ... (3:4)
    # --------------------------------------------------------
    append(u'<img')
    _backup_default_38494504 = get('default', _marker)
    _value = u'default'
    econtext['default'] = _value

    # <Expression u'default' (3:47)> -> _attr_class
    try:
        _attr_class = getitem('default')
    except:
        rcontext.setdefault('__error__', []).append((u'default', 3, 47, '<string>', _sys.exc_info()[1], ))
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
    if (_backup_default_38494504 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38494504
    append(u' />')
    if (_backup_attrs_38642320 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38642320
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38495800 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8bd0> name=None at 22f8810> -> _value
    _value = _static_36670416
    econtext['attrs'] = _value

    # <img ... (4:4)
    # --------------------------------------------------------
    append(u'<img')
    _backup_default_38495728 = get('default', _marker)
    _value = None
    econtext['default'] = _value

    # <Expression u'default' (4:31)> -> _attr_class
    try:
        _attr_class = getitem('default')
    except:
        rcontext.setdefault('__error__', []).append((u'default', 4, 31, '<string>', _sys.exc_info()[1], ))
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
                        if ('"' in _attr_class):
                            _attr_class = _attr_class.replace('"', '&#34;')
    if (_attr_class is not None):
        append((u' class="%s"' % _attr_class))
    if (_backup_default_38495728 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38495728
    append(u' />')
    if (_backup_attrs_38495800 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38495800
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38571832 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8ed0> name=None at 22f8f90> -> _value
    _value = _static_36671184
    econtext['attrs'] = _value

    # <span ... (5:4)
    # --------------------------------------------------------
    append(u'<span>')
    _backup_default_37019016 = get('default', _marker)

    # <Marker name='default' at 22f8890> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'default' (5:23)> -> _cache_36670032
    try:
        _cache_36670032 = getitem('default')
    except:
        rcontext.setdefault('__error__', []).append((u'default', 5, 23, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'default' (5:23)> value=<Marker name='default' at 22f8990> at 22f89d0> -> _condition
    _expression = _cache_36670032

    # <Marker name='default' at 22f8990> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _content_139955154988272 = u'Default'
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    else:
        _content = _cache_36670032
        if (_content is None):
            pass
        else:
            if (_content is False):
                _content = None
            else:
                _tt = type(_content)
                if ((_tt is int) or (_tt is float) or (_tt is long)):
                    _content = unicode(_content)
                else:
                    try:
                        if (_tt is str):
                            _content = decode(_content)
                        else:
                            if (_tt is not unicode):
                                try:
                                    _content = _content.__html__
                                except:
                                    _content = convert(_content)
                                else:
                                    raise RuntimeError
                    except RuntimeError:
                        _content = _content()
                    else:
                        if ((_content is not None) and (re_needs_escape(_content) is not None)):
                            if ('&' in _content):
                                if (';' in _content):
                                    _content = re_amp.sub('&amp;', _content)
                                else:
                                    _content = _content.replace('&', '&amp;')
                            if ('<' in _content):
                                _content = _content.replace('<', '&lt;')
                            if ('>' in _content):
                                _content = _content.replace('>', '&gt;')
                            if ('\x00' in _content):
                                _content = _content.replace('\x00', '&#34;')
        if (_content is not None):
            append(_content)
    if (_backup_default_37019016 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_37019016
    append(u'</span>')
    if (_backup_attrs_38571832 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38571832
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38604240 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x220dc50> name=None at 22f8e90> -> _value
    _value = _static_35707984
    econtext['attrs'] = _value

    # <span ... (6:4)
    # --------------------------------------------------------
    append(u'<span>')
    _backup_default_38601360 = get('default', _marker)

    # <Marker name='default' at 22f8b50> -> _value
    _value = _marker_default
    econtext['default'] = _value

    # <Expression u'default' (6:23)> -> _cache_36670672
    try:
        _cache_36670672 = getitem('default')
    except:
        rcontext.setdefault('__error__', []).append((u'default', 6, 23, '<string>', _sys.exc_info()[1], ))
        raise


    # <Identity expression=<Expression u'default' (6:23)> value=<Marker name='default' at 22f88d0> at 22f8590> -> _condition
    _expression = _cache_36670672

    # <Marker name='default' at 22f88d0> -> _value
    _value = _marker_default
    _condition = (_expression is _value)
    if _condition:
        _content_139955154988272 = u'\n      '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        _backup_attrs_38632624 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x221f410> name=None at 221f490> -> _value
        _value = _static_35779600
        econtext['attrs'] = _value

        # <em ... (7:6)
        # --------------------------------------------------------
        append(u'<em>')

        # <Expression u"'Computed default'" (7:12)> -> _content_139955154988272
        try:
            _content_139955154988272 = 'Computed default'
        except:
            rcontext.setdefault('__error__', []).append((u"'Computed default'", 7, 12, '<string>', _sys.exc_info()[1], ))
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
        _content_139955154988272 = _content_139955154988272
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'</em>')
        if (_backup_attrs_38632624 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_38632624
        _content_139955154988272 = u'\n    '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    else:
        _content = _cache_36670672
        if (_content is None):
            pass
        else:
            if (_content is False):
                _content = None
            else:
                _tt = type(_content)
                if ((_tt is int) or (_tt is float) or (_tt is long)):
                    _content = unicode(_content)
                else:
                    try:
                        if (_tt is str):
                            _content = decode(_content)
                        else:
                            if (_tt is not unicode):
                                try:
                                    _content = _content.__html__
                                except:
                                    _content = convert(_content)
                                else:
                                    raise RuntimeError
                    except RuntimeError:
                        _content = _content()
                    else:
                        if ((_content is not None) and (re_needs_escape(_content) is not None)):
                            if ('&' in _content):
                                if (';' in _content):
                                    _content = re_amp.sub('&amp;', _content)
                                else:
                                    _content = _content.replace('&', '&amp;')
                            if ('<' in _content):
                                _content = _content.replace('<', '&lt;')
                            if ('>' in _content):
                                _content = _content.replace('>', '&gt;')
                            if ('\x00' in _content):
                                _content = _content.replace('\x00', '&#34;')
        if (_content is not None):
            append(_content)
    if (_backup_default_38601360 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38601360
    append(u'</span>')
    if (_backup_attrs_38604240 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38604240
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_38494936 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38494936
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_38643400 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38643400
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass