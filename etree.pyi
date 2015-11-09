# Hand-written stub for lxml.etree as used by mypy.report.
# This is *far* from complete, and the stubgen-generated ones crash mypy.
# Any use of `Any` below means I couldn't figure out the type.

import typing
from typing import Any, Dict, List, Tuple, Union
from typing import SupportsBytes


# We do *not* want `typing.AnyStr` because it is a `TypeVar`, which is an
# unnecessary constraint. It seems reasonable to constrain each
# List/Dict argument to use one type consistently, though, and it is
# necessary in order to keep these brief.
AnyStr = Union[str, bytes]
ListAnyStr = Union[List[str], List[bytes]]
DictAnyStr = Union[Dict[str, str], Dict[bytes, bytes]]
Dict_Tuple2AnyStr_Any = Union[Dict[Tuple[str, str], Any], Tuple[bytes, bytes], Any]


class _Element:
    def addprevious(self, element: '_Element') -> None:
        pass

class _ElementTree:
    def write(self,
              file: Union[AnyStr, typing.IO],
              encoding: AnyStr = ...,
              method: AnyStr = ...,
              pretty_print: bool = ...,
              xml_declaration: Any = ...,
              with_tail: Any = ...,
              standalone: bool = ...,
              compression: int = ...,
              exclusive: bool = ...,
              with_comments: bool = ...,
              inclusive_ns_prefixes: ListAnyStr = ...) -> None:
        pass

class _XSLTResultTree(SupportsBytes):
    pass

class _XSLTQuotedStringParam:
    pass

class XMLParser:
    pass

class XMLSchema:
    def __init__(self,
                 etree: Union[_Element, _ElementTree] = ...,
                 file: Union[AnyStr, typing.IO] = ...) -> None:
        pass

    def assertValid(self,
                    etree: Union[_Element, _ElementTree]) -> None:
        pass

class XSLTAccessControl:
    pass

class XSLT:
    def __init__(self,
                 xslt_input: Union[_Element, _ElementTree],
                 extensions: Dict_Tuple2AnyStr_Any = ...,
                 regexp: bool = ...,
                 access_control: XSLTAccessControl = ...) -> None:
        pass

    def __call__(self,
                 _input: Union[_Element, _ElementTree],
                 profile_run: bool = ...,
                 **kwargs: Union[AnyStr, _XSLTQuotedStringParam]) -> _XSLTResultTree:
        pass

    @staticmethod
    def strparam(s: AnyStr) -> _XSLTQuotedStringParam:
        pass

def Element(_tag: AnyStr,
            attrib: DictAnyStr = ...,
            nsmap: DictAnyStr = ...,
            **extra: AnyStr) -> _Element:
    pass

def SubElement(_parent: _Element, _tag: AnyStr,
               attrib: DictAnyStr = ...,
               nsmap: DictAnyStr = ...,
               **extra: AnyStr) -> _Element:
    pass

def ElementTree(element: _Element = ...,
                file: Union[AnyStr, typing.IO] = ...,
                parser: XMLParser = ...) -> _ElementTree:
    pass

def ProcessingInstruction(target: AnyStr, text: AnyStr = ...) -> _Element:
    pass

def parse(source: Union[AnyStr, typing.IO],
          parser: XMLParser = ...,
          base_url: AnyStr = ...) -> _ElementTree:
    pass
