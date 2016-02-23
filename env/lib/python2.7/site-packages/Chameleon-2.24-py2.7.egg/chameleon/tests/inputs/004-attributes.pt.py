# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_36671184 = {u'a': u'1', u'c': u'3', u'b': u'2', }
_static_35828944 = {}
_static_35829584 = {u'class': u'None', }
_static_35889552 = {u'a': u'1', u'c': u'3', u'b': u'2', }
_static_35801168 = {u'a': u'1', u'c': u'3', u'b': u'2', }
_static_35707920 = {u'a': u'1', u'c': u'3', u'b': u'2', }
_static_35800848 = {u'a': u'1', u'c': u'3', u'b': u'2', }
_static_35830736 = {u'class': u"'hello'", }
_static_35890768 = {u'class': u'hello', }
_static_36668176 = {u'a': u'1', u'c': u'3', u'b': u'2', }
_static_35828624 = {}
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
    _backup_attrs_39099424 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222b4d0> name=None at 222b850> -> _value
    _value = _static_35828944
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36624936 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222b390> name=None at 222b250> -> _value
    _value = _static_35828624
    econtext['attrs'] = _value

    # <body ... (2:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36627376 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222bbd0> name=None at 222b990> -> _value
    _value = _static_35830736
    econtext['attrs'] = _value

    # <span ... (3:4)
    # --------------------------------------------------------
    append(u'<span')
    _backup_default_36629176 = get('default', _marker)
    _value = None
    econtext['default'] = _value

    # <Expression u"'hello'" (3:32)> -> _attr_class
    try:
        _attr_class = 'hello'
    except:
        rcontext.setdefault('__error__', []).append((u"'hello'", 3, 32, '<string>', _sys.exc_info()[1], ))
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
    if (_backup_default_36629176 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36629176
    append(u' />')
    if (_backup_attrs_36627376 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36627376
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36724032 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x222b750> name=None at 222bf90> -> _value
    _value = _static_35829584
    econtext['attrs'] = _value

    # <span ... (4:4)
    # --------------------------------------------------------
    append(u'<span')
    _backup_default_36724464 = get('default', _marker)
    _value = None
    econtext['default'] = _value

    # <Expression u'None' (4:32)> -> _attr_class
    try:
        _attr_class = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 4, 32, '<string>', _sys.exc_info()[1], ))
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
    if (_backup_default_36724464 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36724464
    append(u' />')
    if (_backup_attrs_36724032 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36724032
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36721872 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2224710> name=None at 2224090> -> _value
    _value = _static_35800848
    econtext['attrs'] = _value

    # <span ... (5:4)
    # --------------------------------------------------------
    append(u'<span')
    _backup_default_36721584 = get('default', _marker)
    _value = u'1'
    econtext['default'] = _value

    # <Expression u'None' (5:46)> -> _attr_a
    try:
        _attr_a = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 5, 46, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_a is None):
        pass
    else:
        if (_attr_a is False):
            _attr_a = None
        else:
            _tt = type(_attr_a)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_a = unicode(_attr_a)
            else:
                try:
                    if (_tt is str):
                        _attr_a = decode(_attr_a)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_a = _attr_a.__html__
                            except:
                                _attr_a = convert(_attr_a)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_a = _attr_a()
                else:
                    if ((_attr_a is not None) and (re_needs_escape(_attr_a) is not None)):
                        if ('&' in _attr_a):
                            if (';' in _attr_a):
                                _attr_a = re_amp.sub('&amp;', _attr_a)
                            else:
                                _attr_a = _attr_a.replace('&', '&amp;')
                        if ('<' in _attr_a):
                            _attr_a = _attr_a.replace('<', '&lt;')
                        if ('>' in _attr_a):
                            _attr_a = _attr_a.replace('>', '&gt;')
                        if (u'"' in _attr_a):
                            _attr_a = _attr_a.replace(u'"', '&#34;')
    if (_attr_a is not None):
        append((u' a="%s"' % _attr_a))
    if (_backup_default_36721584 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36721584
    _attr_b = u'2'
    if (_attr_b is not None):
        append((u' b="%s"' % _attr_b))
    _attr_c = u'3'
    if (_attr_c is not None):
        append((u' c="%s"' % _attr_c))
    append(u' />')
    if (_backup_attrs_36721872 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36721872
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36722376 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2224850> name=None at 2224050> -> _value
    _value = _static_35801168
    econtext['attrs'] = _value

    # <span ... (6:4)
    # --------------------------------------------------------
    append(u'<span')
    _attr_a = u'1'
    if (_attr_a is not None):
        append((u' a="%s"' % _attr_a))
    _backup_default_36722520 = get('default', _marker)
    _value = u'2'
    econtext['default'] = _value

    # <Expression u'None' (6:46)> -> _attr_b
    try:
        _attr_b = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 6, 46, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_b is None):
        pass
    else:
        if (_attr_b is False):
            _attr_b = None
        else:
            _tt = type(_attr_b)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_b = unicode(_attr_b)
            else:
                try:
                    if (_tt is str):
                        _attr_b = decode(_attr_b)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_b = _attr_b.__html__
                            except:
                                _attr_b = convert(_attr_b)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_b = _attr_b()
                else:
                    if ((_attr_b is not None) and (re_needs_escape(_attr_b) is not None)):
                        if ('&' in _attr_b):
                            if (';' in _attr_b):
                                _attr_b = re_amp.sub('&amp;', _attr_b)
                            else:
                                _attr_b = _attr_b.replace('&', '&amp;')
                        if ('<' in _attr_b):
                            _attr_b = _attr_b.replace('<', '&lt;')
                        if ('>' in _attr_b):
                            _attr_b = _attr_b.replace('>', '&gt;')
                        if (u'"' in _attr_b):
                            _attr_b = _attr_b.replace(u'"', '&#34;')
    if (_attr_b is not None):
        append((u' b="%s"' % _attr_b))
    if (_backup_default_36722520 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36722520
    _attr_c = u'3'
    if (_attr_c is not None):
        append((u' c="%s"' % _attr_c))
    append(u' />')
    if (_backup_attrs_36722376 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36722376
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36723312 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8310> name=None at 22f8650> -> _value
    _value = _static_36668176
    econtext['attrs'] = _value

    # <span ... (7:4)
    # --------------------------------------------------------
    append(u'<span')
    _attr_a = u'1'
    if (_attr_a is not None):
        append((u' a="%s"' % _attr_a))
    _attr_b = u'2'
    if (_attr_b is not None):
        append((u' b="%s"' % _attr_b))
    _backup_default_36723240 = get('default', _marker)
    _value = u'3'
    econtext['default'] = _value

    # <Expression u'None' (7:46)> -> _attr_c
    try:
        _attr_c = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 7, 46, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_c is None):
        pass
    else:
        if (_attr_c is False):
            _attr_c = None
        else:
            _tt = type(_attr_c)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_c = unicode(_attr_c)
            else:
                try:
                    if (_tt is str):
                        _attr_c = decode(_attr_c)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_c = _attr_c.__html__
                            except:
                                _attr_c = convert(_attr_c)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_c = _attr_c()
                else:
                    if ((_attr_c is not None) and (re_needs_escape(_attr_c) is not None)):
                        if ('&' in _attr_c):
                            if (';' in _attr_c):
                                _attr_c = re_amp.sub('&amp;', _attr_c)
                            else:
                                _attr_c = _attr_c.replace('&', '&amp;')
                        if ('<' in _attr_c):
                            _attr_c = _attr_c.replace('<', '&lt;')
                        if ('>' in _attr_c):
                            _attr_c = _attr_c.replace('>', '&gt;')
                        if (u'"' in _attr_c):
                            _attr_c = _attr_c.replace(u'"', '&#34;')
    if (_attr_c is not None):
        append((u' c="%s"' % _attr_c))
    if (_backup_default_36723240 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36723240
    append(u' />')
    if (_backup_attrs_36723312 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36723312
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36724248 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x22f8ed0> name=None at 22f8f90> -> _value
    _value = _static_36671184
    econtext['attrs'] = _value

    # <span ... (8:4)
    # --------------------------------------------------------
    append(u'<span')
    _attr_a = u'1'
    if (_attr_a is not None):
        append((u' a="%s"' % _attr_a))
    _backup_default_36723384 = get('default', _marker)
    _value = u'2'
    econtext['default'] = _value

    # <Expression u'None' (8:46)> -> _attr_b
    try:
        _attr_b = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 8, 46, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_b is None):
        pass
    else:
        if (_attr_b is False):
            _attr_b = None
        else:
            _tt = type(_attr_b)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_b = unicode(_attr_b)
            else:
                try:
                    if (_tt is str):
                        _attr_b = decode(_attr_b)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_b = _attr_b.__html__
                            except:
                                _attr_b = convert(_attr_b)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_b = _attr_b()
                else:
                    if ((_attr_b is not None) and (re_needs_escape(_attr_b) is not None)):
                        if ('&' in _attr_b):
                            if (';' in _attr_b):
                                _attr_b = re_amp.sub('&amp;', _attr_b)
                            else:
                                _attr_b = _attr_b.replace('&', '&amp;')
                        if ('<' in _attr_b):
                            _attr_b = _attr_b.replace('<', '&lt;')
                        if ('>' in _attr_b):
                            _attr_b = _attr_b.replace('>', '&gt;')
                        if (u'"' in _attr_b):
                            _attr_b = _attr_b.replace(u'"', '&#34;')
    if (_attr_b is not None):
        append((u' b="%s"' % _attr_b))
    if (_backup_default_36723384 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36723384
    _backup_default_36724680 = get('default', _marker)
    _value = u'3'
    econtext['default'] = _value

    # <Expression u'None' (8:53)> -> _attr_c
    try:
        _attr_c = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 8, 53, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_c is None):
        pass
    else:
        if (_attr_c is False):
            _attr_c = None
        else:
            _tt = type(_attr_c)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_c = unicode(_attr_c)
            else:
                try:
                    if (_tt is str):
                        _attr_c = decode(_attr_c)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_c = _attr_c.__html__
                            except:
                                _attr_c = convert(_attr_c)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_c = _attr_c()
                else:
                    if ((_attr_c is not None) and (re_needs_escape(_attr_c) is not None)):
                        if ('&' in _attr_c):
                            if (';' in _attr_c):
                                _attr_c = re_amp.sub('&amp;', _attr_c)
                            else:
                                _attr_c = _attr_c.replace('&', '&amp;')
                        if ('<' in _attr_c):
                            _attr_c = _attr_c.replace('<', '&lt;')
                        if ('>' in _attr_c):
                            _attr_c = _attr_c.replace('>', '&gt;')
                        if (u'"' in _attr_c):
                            _attr_c = _attr_c.replace(u'"', '&#34;')
    if (_attr_c is not None):
        append((u' c="%s"' % _attr_c))
    if (_backup_default_36724680 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36724680
    append(u' />')
    if (_backup_attrs_36724248 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36724248
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38641744 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x220dc10> name=None at 220ddd0> -> _value
    _value = _static_35707920
    econtext['attrs'] = _value

    # <span ... (9:4)
    # --------------------------------------------------------
    append(u'<span')
    _attr_a = u'1'
    if (_attr_a is not None):
        append((u' a="%s"' % _attr_a))
    _backup_default_38642032 = get('default', _marker)
    _value = u'2'
    econtext['default'] = _value

    # <Expression u'string:;' (9:46)> -> _attr_b
    try:
        _attr_b = u';'
    except:
        rcontext.setdefault('__error__', []).append((u'string:;', 9, 46, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_b is None):
        pass
    else:
        if (_attr_b is False):
            _attr_b = None
        else:
            _tt = type(_attr_b)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_b = unicode(_attr_b)
            else:
                try:
                    if (_tt is str):
                        _attr_b = decode(_attr_b)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_b = _attr_b.__html__
                            except:
                                _attr_b = convert(_attr_b)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_b = _attr_b()
                else:
                    if ((_attr_b is not None) and (re_needs_escape(_attr_b) is not None)):
                        if ('&' in _attr_b):
                            if (';' in _attr_b):
                                _attr_b = re_amp.sub('&amp;', _attr_b)
                            else:
                                _attr_b = _attr_b.replace('&', '&amp;')
                        if ('<' in _attr_b):
                            _attr_b = _attr_b.replace('<', '&lt;')
                        if ('>' in _attr_b):
                            _attr_b = _attr_b.replace('>', '&gt;')
                        if (u'"' in _attr_b):
                            _attr_b = _attr_b.replace(u'"', '&#34;')
    if (_attr_b is not None):
        append((u' b="%s"' % _attr_b))
    if (_backup_default_38642032 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38642032
    _attr_c = u'3'
    if (_attr_c is not None):
        append((u' c="%s"' % _attr_c))
    append(u' />')
    if (_backup_attrs_38641744 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38641744
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36721224 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x223a190> name=None at 223a1d0> -> _value
    _value = _static_35889552
    econtext['attrs'] = _value

    # <span ... (10:4)
    # --------------------------------------------------------
    append(u'<span')
    _attr_a = u'1'
    if (_attr_a is not None):
        append((u' a="%s"' % _attr_a))
    _backup_default_36721080 = get('default', _marker)
    _value = u'2'
    econtext['default'] = _value

    # <Expression u'string:&amp;' (10:46)> -> _attr_b
    try:
        _attr_b = u'&amp;'
    except:
        rcontext.setdefault('__error__', []).append((u'string:&amp;', 10, 46, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_b is None):
        pass
    else:
        if (_attr_b is False):
            _attr_b = None
        else:
            _tt = type(_attr_b)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_b = unicode(_attr_b)
            else:
                try:
                    if (_tt is str):
                        _attr_b = decode(_attr_b)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_b = _attr_b.__html__
                            except:
                                _attr_b = convert(_attr_b)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_b = _attr_b()
                else:
                    if ((_attr_b is not None) and (re_needs_escape(_attr_b) is not None)):
                        if ('&' in _attr_b):
                            if (';' in _attr_b):
                                _attr_b = re_amp.sub('&amp;', _attr_b)
                            else:
                                _attr_b = _attr_b.replace('&', '&amp;')
                        if ('<' in _attr_b):
                            _attr_b = _attr_b.replace('<', '&lt;')
                        if ('>' in _attr_b):
                            _attr_b = _attr_b.replace('>', '&gt;')
                        if (u'"' in _attr_b):
                            _attr_b = _attr_b.replace(u'"', '&#34;')
    if (_attr_b is not None):
        append((u' b="%s"' % _attr_b))
    if (_backup_default_36721080 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_36721080
    _attr_c = u'3'
    if (_attr_c is not None):
        append((u' c="%s"' % _attr_c))
    append(u' />')
    if (_backup_attrs_36721224 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36721224
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38642176 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x223a650> name=None at 223a250> -> _value
    _value = _static_35890768
    econtext['attrs'] = _value

    # <span ... (11:4)
    # --------------------------------------------------------
    append(u'<span')
    _backup_default_38642104 = get('default', _marker)
    _value = u'hello'
    econtext['default'] = _value

    # <Expression u"'goodbye'" (11:46)> -> _attr_class
    try:
        _attr_class = 'goodbye'
    except:
        rcontext.setdefault('__error__', []).append((u"'goodbye'", 11, 46, '<string>', _sys.exc_info()[1], ))
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
    if (_backup_default_38642104 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_38642104
    append(u' />')
    if (_backup_attrs_38642176 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38642176
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_36624936 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36624936
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_39099424 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39099424
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass