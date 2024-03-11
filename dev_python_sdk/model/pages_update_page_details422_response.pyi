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


class PagesUpdatePageDetails422Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            description = schemas.StrSchema
            id = schemas.NumberSchema
            slug = schemas.StrSchema
            is_top_level_path = schemas.BoolSchema
            landing_page = schemas.BoolSchema
            
            
            class body_html(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'body_html':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class body_json(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'body_json':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            body_markdown = schemas.StrSchema
            processed_html = schemas.StrSchema
        
            @staticmethod
            def social_image() -> typing.Type['PagesUpdatePageDetails422ResponseSocialImage']:
                return PagesUpdatePageDetails422ResponseSocialImage
            template = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "description": description,
                "id": id,
                "slug": slug,
                "is_top_level_path": is_top_level_path,
                "landing_page": landing_page,
                "body_html": body_html,
                "body_json": body_json,
                "body_markdown": body_markdown,
                "processed_html": processed_html,
                "social_image": social_image,
                "template": template,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_top_level_path"]) -> MetaOapg.properties.is_top_level_path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["landing_page"]) -> MetaOapg.properties.landing_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_html"]) -> MetaOapg.properties.body_html: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_json"]) -> MetaOapg.properties.body_json: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_markdown"]) -> MetaOapg.properties.body_markdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processed_html"]) -> MetaOapg.properties.processed_html: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["social_image"]) -> 'PagesUpdatePageDetails422ResponseSocialImage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template"]) -> MetaOapg.properties.template: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "id", "slug", "is_top_level_path", "landing_page", "body_html", "body_json", "body_markdown", "processed_html", "social_image", "template", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> typing.Union[MetaOapg.properties.slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_top_level_path"]) -> typing.Union[MetaOapg.properties.is_top_level_path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["landing_page"]) -> typing.Union[MetaOapg.properties.landing_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_html"]) -> typing.Union[MetaOapg.properties.body_html, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_json"]) -> typing.Union[MetaOapg.properties.body_json, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_markdown"]) -> typing.Union[MetaOapg.properties.body_markdown, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processed_html"]) -> typing.Union[MetaOapg.properties.processed_html, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["social_image"]) -> typing.Union['PagesUpdatePageDetails422ResponseSocialImage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template"]) -> typing.Union[MetaOapg.properties.template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "id", "slug", "is_top_level_path", "landing_page", "body_html", "body_json", "body_markdown", "processed_html", "social_image", "template", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        slug: typing.Union[MetaOapg.properties.slug, str, schemas.Unset] = schemas.unset,
        is_top_level_path: typing.Union[MetaOapg.properties.is_top_level_path, bool, schemas.Unset] = schemas.unset,
        landing_page: typing.Union[MetaOapg.properties.landing_page, bool, schemas.Unset] = schemas.unset,
        body_html: typing.Union[MetaOapg.properties.body_html, None, str, schemas.Unset] = schemas.unset,
        body_json: typing.Union[MetaOapg.properties.body_json, None, str, schemas.Unset] = schemas.unset,
        body_markdown: typing.Union[MetaOapg.properties.body_markdown, str, schemas.Unset] = schemas.unset,
        processed_html: typing.Union[MetaOapg.properties.processed_html, str, schemas.Unset] = schemas.unset,
        social_image: typing.Union['PagesUpdatePageDetails422ResponseSocialImage', schemas.Unset] = schemas.unset,
        template: typing.Union[MetaOapg.properties.template, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PagesUpdatePageDetails422Response':
        return super().__new__(
            cls,
            *args,
            title=title,
            description=description,
            id=id,
            slug=slug,
            is_top_level_path=is_top_level_path,
            landing_page=landing_page,
            body_html=body_html,
            body_json=body_json,
            body_markdown=body_markdown,
            processed_html=processed_html,
            social_image=social_image,
            template=template,
            _configuration=_configuration,
            **kwargs,
        )

from dev_python_sdk.model.pages_update_page_details422_response_social_image import PagesUpdatePageDetails422ResponseSocialImage