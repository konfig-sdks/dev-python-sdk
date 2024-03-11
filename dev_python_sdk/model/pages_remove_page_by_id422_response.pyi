# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from dev_python_sdk import schemas  # noqa: F401


class PagesRemovePageById422Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def doubled_module() -> typing.Type['PagesRemovePageById422ResponseDoubledModule']:
                return PagesRemovePageById422ResponseDoubledModule
            __expired = schemas.BoolSchema
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class __sending_message(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> '__sending_message':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "doubled_module": doubled_module,
                "__expired": __expired,
                "name": name,
                "__sending_message": __sending_message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["doubled_module"]) -> 'PagesRemovePageById422ResponseDoubledModule': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["__expired"]) -> MetaOapg.properties.__expired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["__sending_message"]) -> MetaOapg.properties.__sending_message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["doubled_module", "__expired", "name", "__sending_message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["doubled_module"]) -> typing.Union['PagesRemovePageById422ResponseDoubledModule', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["__expired"]) -> typing.Union[MetaOapg.properties.__expired, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["__sending_message"]) -> typing.Union[MetaOapg.properties.__sending_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["doubled_module", "__expired", "name", "__sending_message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        doubled_module: typing.Union['PagesRemovePageById422ResponseDoubledModule', schemas.Unset] = schemas.unset,
        __expired: typing.Union[MetaOapg.properties.__expired, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        __sending_message: typing.Union[MetaOapg.properties.__sending_message, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PagesRemovePageById422Response':
        return super().__new__(
            cls,
            *args,
            doubled_module=doubled_module,
            __expired=__expired,
            name=name,
            __sending_message=__sending_message,
            _configuration=_configuration,
            **kwargs,
        )

from dev_python_sdk.model.pages_remove_page_by_id422_response_doubled_module import PagesRemovePageById422ResponseDoubledModule
