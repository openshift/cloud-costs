# -*- coding: utf-8 -*-
pass
import sys as _sys
pass
_static_39101904 = {u'checked': u'True', }
_static_39101136 = {u'checked': u'False', }
_static_38932624 = {u'selected': u'None', }
_static_38934992 = {u'selected': u'True', }
_static_38934864 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
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
    _backup_attrs_39545024 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2521950> name=None at 2521e90> -> _value
    _value = _static_38934864
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
    _backup_attrs_39545672 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x25219d0> name=None at 2521610> -> _value
    _value = _static_38934992
    econtext['attrs'] = _value

    # <option ... (3:2)
    # --------------------------------------------------------
    append(u'<option')
    _backup_default_39545096 = get('default', _marker)
    _value = None
    econtext['default'] = _value

    # <Expression u'True' (3:35)> -> _attr_selected
    try:
        _attr_selected = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 3, 35, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_selected is None):
        pass
    else:
        if (_attr_selected is False):
            _attr_selected = None
        else:
            _tt = type(_attr_selected)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_selected = unicode(_attr_selected)
            else:
                try:
                    if (_tt is str):
                        _attr_selected = decode(_attr_selected)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_selected = _attr_selected.__html__
                            except:
                                _attr_selected = convert(_attr_selected)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_selected = _attr_selected()
                else:
                    if ((_attr_selected is not None) and (re_needs_escape(_attr_selected) is not None)):
                        if ('&' in _attr_selected):
                            if (';' in _attr_selected):
                                _attr_selected = re_amp.sub('&amp;', _attr_selected)
                            else:
                                _attr_selected = _attr_selected.replace('&', '&amp;')
                        if ('<' in _attr_selected):
                            _attr_selected = _attr_selected.replace('<', '&lt;')
                        if ('>' in _attr_selected):
                            _attr_selected = _attr_selected.replace('>', '&gt;')
                        if ('"' in _attr_selected):
                            _attr_selected = _attr_selected.replace('"', '&#34;')
    if (_attr_selected is not None):
        append((u' selected="%s"' % _attr_selected))
    if (_backup_default_39545096 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39545096
    append(u'>')
    append(u'</option>')
    if (_backup_attrs_39545672 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39545672
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39594032 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x2521090> name=None at 25215d0> -> _value
    _value = _static_38932624
    econtext['attrs'] = _value

    # <option ... (4:2)
    # --------------------------------------------------------
    append(u'<option')
    _backup_default_39594608 = get('default', _marker)
    _value = None
    econtext['default'] = _value

    # <Expression u'None' (4:35)> -> _attr_selected
    try:
        _attr_selected = None
    except:
        rcontext.setdefault('__error__', []).append((u'None', 4, 35, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_selected is None):
        pass
    else:
        if (_attr_selected is False):
            _attr_selected = None
        else:
            _tt = type(_attr_selected)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_selected = unicode(_attr_selected)
            else:
                try:
                    if (_tt is str):
                        _attr_selected = decode(_attr_selected)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_selected = _attr_selected.__html__
                            except:
                                _attr_selected = convert(_attr_selected)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_selected = _attr_selected()
                else:
                    if ((_attr_selected is not None) and (re_needs_escape(_attr_selected) is not None)):
                        if ('&' in _attr_selected):
                            if (';' in _attr_selected):
                                _attr_selected = re_amp.sub('&amp;', _attr_selected)
                            else:
                                _attr_selected = _attr_selected.replace('&', '&amp;')
                        if ('<' in _attr_selected):
                            _attr_selected = _attr_selected.replace('<', '&lt;')
                        if ('>' in _attr_selected):
                            _attr_selected = _attr_selected.replace('>', '&gt;')
                        if ('"' in _attr_selected):
                            _attr_selected = _attr_selected.replace('"', '&#34;')
    if (_attr_selected is not None):
        append((u' selected="%s"' % _attr_selected))
    if (_backup_default_39594608 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39594608
    append(u'>')
    append(u'</option>')
    if (_backup_attrs_39594032 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39594032
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39595400 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x254a5d0> name=None at 254a750> -> _value
    _value = _static_39101904
    econtext['attrs'] = _value

    # <input ... (5:2)
    # --------------------------------------------------------
    append(u'<input')
    _backup_default_40174800 = get('default', _marker)
    _value = None
    econtext['default'] = _value

    # <Expression u'True' (5:33)> -> _attr_checked
    try:
        _attr_checked = True
    except:
        rcontext.setdefault('__error__', []).append((u'True', 5, 33, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_checked is None):
        pass
    else:
        if (_attr_checked is False):
            _attr_checked = None
        else:
            _tt = type(_attr_checked)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_checked = unicode(_attr_checked)
            else:
                try:
                    if (_tt is str):
                        _attr_checked = decode(_attr_checked)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_checked = _attr_checked.__html__
                            except:
                                _attr_checked = convert(_attr_checked)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_checked = _attr_checked()
                else:
                    if ((_attr_checked is not None) and (re_needs_escape(_attr_checked) is not None)):
                        if ('&' in _attr_checked):
                            if (';' in _attr_checked):
                                _attr_checked = re_amp.sub('&amp;', _attr_checked)
                            else:
                                _attr_checked = _attr_checked.replace('&', '&amp;')
                        if ('<' in _attr_checked):
                            _attr_checked = _attr_checked.replace('<', '&lt;')
                        if ('>' in _attr_checked):
                            _attr_checked = _attr_checked.replace('>', '&gt;')
                        if ('"' in _attr_checked):
                            _attr_checked = _attr_checked.replace('"', '&#34;')
    if (_attr_checked is not None):
        append((u' checked="%s"' % _attr_checked))
    if (_backup_default_40174800 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_40174800
    append(u' />')
    if (_backup_attrs_39595400 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39595400
    _content_139955154988272 = u'\n  '
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    _backup_attrs_39593744 = get('attrs', _marker)

    # <Static value=<_ast.Dict object at 0x254a2d0> name=None at 254a210> -> _value
    _value = _static_39101136
    econtext['attrs'] = _value

    # <input ... (6:2)
    # --------------------------------------------------------
    append(u'<input')
    _backup_default_39066584 = get('default', _marker)
    _value = None
    econtext['default'] = _value

    # <Expression u'False' (6:33)> -> _attr_checked
    try:
        _attr_checked = False
    except:
        rcontext.setdefault('__error__', []).append((u'False', 6, 33, '<string>', _sys.exc_info()[1], ))
        raise

    if (_attr_checked is None):
        pass
    else:
        if (_attr_checked is False):
            _attr_checked = None
        else:
            _tt = type(_attr_checked)
            if ((_tt is int) or (_tt is float) or (_tt is long)):
                _attr_checked = unicode(_attr_checked)
            else:
                try:
                    if (_tt is str):
                        _attr_checked = decode(_attr_checked)
                    else:
                        if (_tt is not unicode):
                            try:
                                _attr_checked = _attr_checked.__html__
                            except:
                                _attr_checked = convert(_attr_checked)
                            else:
                                raise RuntimeError
                except RuntimeError:
                    _attr_checked = _attr_checked()
                else:
                    if ((_attr_checked is not None) and (re_needs_escape(_attr_checked) is not None)):
                        if ('&' in _attr_checked):
                            if (';' in _attr_checked):
                                _attr_checked = re_amp.sub('&amp;', _attr_checked)
                            else:
                                _attr_checked = _attr_checked.replace('&', '&amp;')
                        if ('<' in _attr_checked):
                            _attr_checked = _attr_checked.replace('<', '&lt;')
                        if ('>' in _attr_checked):
                            _attr_checked = _attr_checked.replace('>', '&gt;')
                        if ('"' in _attr_checked):
                            _attr_checked = _attr_checked.replace('"', '&#34;')
    if (_attr_checked is not None):
        append((u' checked="%s"' % _attr_checked))
    if (_backup_default_39066584 is _marker):
        del econtext['default']
    else:
        econtext['default'] = _backup_default_39066584
    append(u' />')
    if (_backup_attrs_39593744 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39593744
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
    append(u'</div>')
    if (_backup_attrs_39545024 is _marker):
        del econtext['attrs']
    else:
        econtext['attrs'] = _backup_attrs_39545024
    _content_139955154988272 = u'\n'
    if (_content_139955154988272 is not None):
        append(_content_139955154988272)
pass