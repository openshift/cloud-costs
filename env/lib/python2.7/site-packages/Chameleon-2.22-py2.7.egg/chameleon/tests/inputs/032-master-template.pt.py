# -*- coding: utf-8 -*-
pass
from chameleon.utils import Placeholder as _Placeholder
import sys as _sys
pass
_static_39973456 = {u'id': u'content', }
_static_38402704 = {}
_static_40208784 = {}
_static_38935504 = {}
_static_38935440 = {}
_static_39975056 = {u'id': u'footer', }
_marker_default = _Placeholder()
import re
import functools
_marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def render_main(stream, econtext, rcontext):
    try:
        _slot_title = getitem(u'_slot_title').pop()
    except:
        _slot_title = None

    try:
        _slot_content = getitem(u'_slot_content').pop()
    except:
        _slot_content = None

    try:
        _slot_body_footer = getitem(u'_slot_body_footer').pop()
    except:
        _slot_body_footer = None

    append = stream.append
    getitem = econtext.__getitem__
    get = econtext.get
    _i18n_domain = None
    re_amp = g_re_amp
    re_needs_escape = g_re_needs_escape
    decode = getitem('decode')
    convert = getitem('convert')
    translate = getitem('translate')
    _backup_content_36741456 = get('content', _marker)

    # <Expression u'nothing' (1:52)> -> _value
    try:
        _value = getitem('nothing')
    except:
        rcontext.setdefault('__error__', []).append((u'nothing', 1, 52, '<string>', _sys.exc_info()[1], ))
        raise

    econtext['content'] = _value
    _backup_attrs_39812776 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2658990> name=None at 2658710> -> _value
    _value = _static_40208784
    econtext['attrs'] = _value

    # <html ... (1:0)
    # --------------------------------------------------------
    append(u'<html>')
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_38435368 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2521bd0> name=None at 2521f90> -> _value
    _value = _static_38935504
    econtext['attrs'] = _value

    # <head ... (2:2)
    # --------------------------------------------------------
    append(u'<head>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    if (_slot_title is None):
        _backup_has_title_38932944 = get('has_title', _marker)

        # <Expression u'exists: title' (4:33)> -> _value
        try:
            try:
                _ignore = getitem('title')
            except (AttributeError, LookupError, TypeError, NameError, KeyError, ):
                _value = 0
            else:
                _value = 1
        except:
            rcontext.setdefault('__error__', []).append((u'exists: title', 4, 33, '<string>', _sys.exc_info()[1], ))
            raise

        econtext['has_title'] = _value
        _backup_attrs_36811840 = get('attrs', _marker)

        # <Static value=<_ast.Dict object at 0x2521b90> name=None at 2521050> -> _value
        _value = _static_38935440
        econtext['attrs'] = _value

        # <title ... (3:4)
        # --------------------------------------------------------
        append(u'<title>')
        _backup_default_38436088 = get('default', _marker)

        # <Marker name='default' at 2521490> -> _value
        _value = _marker_default
        econtext['default'] = _value

        # <Expression u'title if has_title else default' (5:24)> -> _cache_38935120
        try:
            _cache_38935120 = (getitem('title') if getitem('has_title') else getitem('default'))
        except:
            rcontext.setdefault('__error__', []).append((u'title if has_title else default', 5, 24, '<string>', _sys.exc_info()[1], ))
            raise


        # <Identity expression=<Expression u'title if has_title else default' (5:24)> value=<Marker name='default' at 2521f50> at 2521790> -> _condition
        _expression = _cache_38935120

        # <Marker name='default' at 2521f50> -> _value
        _value = _marker_default
        _condition = (_expression is _value)
        if _condition:
            _content_139955154988272 = u'Master template'
            if (_content_139955154988272 is not None):
                append(_content_139955154988272)
        else:
            _content = _cache_38935120
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
        if (_backup_default_38436088 is _marker):
            del econtext['default']
        else:
            econtext['default'] = _backup_default_38436088
        append(u'</title>')
        if (_backup_attrs_36811840 is _marker):
            del econtext['attrs']
        else:
            econtext['attrs'] = _backup_attrs_36811840
        if (_backup_has_title_38932944 is _marker):
            del econtext['has_title']
        else:
            econtext['has_title'] = _backup_has_title_38932944
    else:
        _slot_title(stream, econtext.copy(), econtext)
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</head>')
    if (_backup_attrs_38435368 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_38435368
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36813640 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x249fa90> name=None at 249fc10> -> _value
    _value = _static_38402704
    econtext['attrs'] = _value

    # <body ... (7:2)
    # --------------------------------------------------------
    append(u'<body>')
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36813496 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x261f250> name=None at 261f210> -> _value
    _value = _static_39973456
    econtext['attrs'] = _value

    # <div ... (8:4)
    # --------------------------------------------------------
    append(u'<div')
    _attr_id = u'content'
    if (_attr_id is not None):
        append((u' id="%s"' % _attr_id))
    append(u'>')
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    if (_slot_content is None):
        _content_139955154988272 = u'\n        '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
        append(u'<!-- content here -->')
        _content_139955154988272 = u'\n      '
        if (_content_139955154988272 is not None):
            append(_content_139955154988272)
    else:
        _slot_content(stream, econtext.copy(), econtext)
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_36813496 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36813496
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_36812632 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x261f890> name=None at 261fad0> -> _value
    _value = _static_39975056
    econtext['attrs'] = _value

    # <div ... (13:4)
    # --------------------------------------------------------
    append(u'<div')
    _attr_id = u'footer'
    if (_attr_id is not None):
        append((u' id="%s"' % _attr_id))
    append(u'>')
    _content_139955154988272 = u'\n      '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    if (_slot_body_footer is None):
        _backup_default_36811120 = get('default', _marker)

        # <Marker name='default' at 261f910> -> _value
        _value = _marker_default
        econtext['default'] = _value

        # <Expression u'nothing' (14:59)> -> _cache_39976784
        try:
            _cache_39976784 = getitem('nothing')
        except:
            rcontext.setdefault('__error__', []).append((u'nothing', 14, 59, '<string>', _sys.exc_info()[1], ))
            raise


        # <Identity expression=<Expression u'nothing' (14:59)> value=<Marker name='default' at 261fb50> at 261f6d0> -> _condition
        _expression = _cache_39976784

        # <Marker name='default' at 261fb50> -> _value
        _value = _marker_default
        _condition = (_expression is _value)
        if _condition:
            _content_139955154988272 = u'\n        '
            if (_content_139955154988272 is not None):
                append(_content_139955154988272)
            append(u'<!-- footer here -->')
            _content_139955154988272 = u'\n      '
            if (_content_139955154988272 is not None):
                append(_content_139955154988272)
        else:
            _content = _cache_39976784
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
        if (_backup_default_36811120 is _marker):
            del econtext['default']
        else:
            econtext['default'] = _backup_default_36811120
    else:
        _slot_body_footer(stream, econtext.copy(), econtext)
    _content_139955154988272 = u'\n    '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_36812632 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36812632
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</body>')
    if (_backup_attrs_36813640 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_36813640
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</html>')
    if (_backup_attrs_39812776 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39812776
    if (_backup_content_36741456 is _marker):
        del econtext['content']
    else:
        econtext['content'] = _backup_content_36741456

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
    render_main(stream, econtext.copy(), rcontext)
    econtext.update(rcontext)
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass