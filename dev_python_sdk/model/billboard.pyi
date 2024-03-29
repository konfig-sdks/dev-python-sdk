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


class Billboard(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Billboard, aka Widget, ex. Display Ad
    """


    class MetaOapg:
        required = {
            "body_markdown",
            "name",
            "placement_area",
        }
        
        class properties:
            name = schemas.StrSchema
            body_markdown = schemas.StrSchema
            
            
            class placement_area(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SIDEBAR_LEFT(cls):
                    return cls("sidebar_left")
                
                @schemas.classproperty
                def SIDEBAR_LEFT_2(cls):
                    return cls("sidebar_left_2")
                
                @schemas.classproperty
                def SIDEBAR_RIGHT(cls):
                    return cls("sidebar_right")
                
                @schemas.classproperty
                def FEED_FIRST(cls):
                    return cls("feed_first")
                
                @schemas.classproperty
                def FEED_SECOND(cls):
                    return cls("feed_second")
                
                @schemas.classproperty
                def FEED_THIRD(cls):
                    return cls("feed_third")
                
                @schemas.classproperty
                def HOME_HERO(cls):
                    return cls("home_hero")
                
                @schemas.classproperty
                def POST_SIDEBAR(cls):
                    return cls("post_sidebar")
                
                @schemas.classproperty
                def POST_COMMENTS(cls):
                    return cls("post_comments")
            id = schemas.IntSchema
            approved = schemas.BoolSchema
            published = schemas.BoolSchema
            
            
            class organization_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'organization_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class creator_id(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'creator_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            tag_list = schemas.StrSchema
            
            
            class exclude_article_ids(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'exclude_article_ids':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            audience_segment_id = schemas.IntSchema
            
            
            class audience_segment_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MANUAL(cls):
                    return cls("manual")
                
                @schemas.classproperty
                def TRUSTED(cls):
                    return cls("trusted")
                
                @schemas.classproperty
                def POSTED(cls):
                    return cls("posted")
                
                @schemas.classproperty
                def NO_POSTS_YET(cls):
                    return cls("no_posts_yet")
                
                @schemas.classproperty
                def DARK_THEME(cls):
                    return cls("dark_theme")
                
                @schemas.classproperty
                def LIGHT_THEME(cls):
                    return cls("light_theme")
                
                @schemas.classproperty
                def NO_EXPERIENCE(cls):
                    return cls("no_experience")
                
                @schemas.classproperty
                def EXPERIENCE1(cls):
                    return cls("experience1")
                
                @schemas.classproperty
                def EXPERIENCE2(cls):
                    return cls("experience2")
                
                @schemas.classproperty
                def EXPERIENCE3(cls):
                    return cls("experience3")
                
                @schemas.classproperty
                def EXPERIENCE4(cls):
                    return cls("experience4")
                
                @schemas.classproperty
                def EXPERIENCE5(cls):
                    return cls("experience5")
        
            @staticmethod
            def target_geolocations() -> typing.Type['BillboardTargetGeolocations']:
                return BillboardTargetGeolocations
            
            
            class display_to(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALL(cls):
                    return cls("all")
                
                @schemas.classproperty
                def LOGGED_IN(cls):
                    return cls("logged_in")
                
                @schemas.classproperty
                def LOGGED_OUT(cls):
                    return cls("logged_out")
            
            
            class type_of(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def IN_HOUSE(cls):
                    return cls("in_house")
                
                @schemas.classproperty
                def COMMUNITY(cls):
                    return cls("community")
                
                @schemas.classproperty
                def EXTERNAL(cls):
                    return cls("external")
            __annotations__ = {
                "name": name,
                "body_markdown": body_markdown,
                "placement_area": placement_area,
                "id": id,
                "approved": approved,
                "published": published,
                "organization_id": organization_id,
                "creator_id": creator_id,
                "tag_list": tag_list,
                "exclude_article_ids": exclude_article_ids,
                "audience_segment_id": audience_segment_id,
                "audience_segment_type": audience_segment_type,
                "target_geolocations": target_geolocations,
                "display_to": display_to,
                "type_of": type_of,
            }
    
    body_markdown: MetaOapg.properties.body_markdown
    name: MetaOapg.properties.name
    placement_area: MetaOapg.properties.placement_area
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_markdown"]) -> MetaOapg.properties.body_markdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["placement_area"]) -> MetaOapg.properties.placement_area: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approved"]) -> MetaOapg.properties.approved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published"]) -> MetaOapg.properties.published: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization_id"]) -> MetaOapg.properties.organization_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator_id"]) -> MetaOapg.properties.creator_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_list"]) -> MetaOapg.properties.tag_list: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_article_ids"]) -> MetaOapg.properties.exclude_article_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audience_segment_id"]) -> MetaOapg.properties.audience_segment_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audience_segment_type"]) -> MetaOapg.properties.audience_segment_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_geolocations"]) -> 'BillboardTargetGeolocations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_to"]) -> MetaOapg.properties.display_to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type_of"]) -> MetaOapg.properties.type_of: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "body_markdown", "placement_area", "id", "approved", "published", "organization_id", "creator_id", "tag_list", "exclude_article_ids", "audience_segment_id", "audience_segment_type", "target_geolocations", "display_to", "type_of", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_markdown"]) -> MetaOapg.properties.body_markdown: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["placement_area"]) -> MetaOapg.properties.placement_area: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approved"]) -> typing.Union[MetaOapg.properties.approved, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published"]) -> typing.Union[MetaOapg.properties.published, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization_id"]) -> typing.Union[MetaOapg.properties.organization_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator_id"]) -> typing.Union[MetaOapg.properties.creator_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_list"]) -> typing.Union[MetaOapg.properties.tag_list, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_article_ids"]) -> typing.Union[MetaOapg.properties.exclude_article_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audience_segment_id"]) -> typing.Union[MetaOapg.properties.audience_segment_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audience_segment_type"]) -> typing.Union[MetaOapg.properties.audience_segment_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_geolocations"]) -> typing.Union['BillboardTargetGeolocations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_to"]) -> typing.Union[MetaOapg.properties.display_to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type_of"]) -> typing.Union[MetaOapg.properties.type_of, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "body_markdown", "placement_area", "id", "approved", "published", "organization_id", "creator_id", "tag_list", "exclude_article_ids", "audience_segment_id", "audience_segment_type", "target_geolocations", "display_to", "type_of", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        body_markdown: typing.Union[MetaOapg.properties.body_markdown, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        placement_area: typing.Union[MetaOapg.properties.placement_area, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        approved: typing.Union[MetaOapg.properties.approved, bool, schemas.Unset] = schemas.unset,
        published: typing.Union[MetaOapg.properties.published, bool, schemas.Unset] = schemas.unset,
        organization_id: typing.Union[MetaOapg.properties.organization_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        creator_id: typing.Union[MetaOapg.properties.creator_id, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tag_list: typing.Union[MetaOapg.properties.tag_list, str, schemas.Unset] = schemas.unset,
        exclude_article_ids: typing.Union[MetaOapg.properties.exclude_article_ids, None, str, schemas.Unset] = schemas.unset,
        audience_segment_id: typing.Union[MetaOapg.properties.audience_segment_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        audience_segment_type: typing.Union[MetaOapg.properties.audience_segment_type, str, schemas.Unset] = schemas.unset,
        target_geolocations: typing.Union['BillboardTargetGeolocations', schemas.Unset] = schemas.unset,
        display_to: typing.Union[MetaOapg.properties.display_to, str, schemas.Unset] = schemas.unset,
        type_of: typing.Union[MetaOapg.properties.type_of, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Billboard':
        return super().__new__(
            cls,
            *args,
            body_markdown=body_markdown,
            name=name,
            placement_area=placement_area,
            id=id,
            approved=approved,
            published=published,
            organization_id=organization_id,
            creator_id=creator_id,
            tag_list=tag_list,
            exclude_article_ids=exclude_article_ids,
            audience_segment_id=audience_segment_id,
            audience_segment_type=audience_segment_type,
            target_geolocations=target_geolocations,
            display_to=display_to,
            type_of=type_of,
            _configuration=_configuration,
            **kwargs,
        )

from dev_python_sdk.model.billboard_target_geolocations import BillboardTargetGeolocations
