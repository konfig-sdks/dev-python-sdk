# coding: utf-8
"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from dev_python_sdk.client_custom import ClientCustom
from dev_python_sdk.configuration import Configuration
from dev_python_sdk.api_client import ApiClient
from dev_python_sdk.type_util import copy_signature
from dev_python_sdk.apis.tags.articles_api import ArticlesApi
from dev_python_sdk.apis.tags.billboards_api import BillboardsApi
from dev_python_sdk.apis.tags.comments_api import CommentsApi
from dev_python_sdk.apis.tags.followed_tags_api import FollowedTagsApi
from dev_python_sdk.apis.tags.followers_api import FollowersApi
from dev_python_sdk.apis.tags.organizations_api import OrganizationsApi
from dev_python_sdk.apis.tags.pages_api import PagesApi
from dev_python_sdk.apis.tags.podcast_episodes_api import PodcastEpisodesApi
from dev_python_sdk.apis.tags.profile_images_api import ProfileImagesApi
from dev_python_sdk.apis.tags.reactions_api import ReactionsApi
from dev_python_sdk.apis.tags.readinglist_api import ReadinglistApi
from dev_python_sdk.apis.tags.segments_api import SegmentsApi
from dev_python_sdk.apis.tags.tags_api import TagsApi
from dev_python_sdk.apis.tags.users_api import UsersApi
from dev_python_sdk.apis.tags.videos_api import VideosApi



class Dev(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.articles: ArticlesApi = ArticlesApi(api_client)
        self.billboards: BillboardsApi = BillboardsApi(api_client)
        self.comments: CommentsApi = CommentsApi(api_client)
        self.followed_tags: FollowedTagsApi = FollowedTagsApi(api_client)
        self.followers: FollowersApi = FollowersApi(api_client)
        self.organizations: OrganizationsApi = OrganizationsApi(api_client)
        self.pages: PagesApi = PagesApi(api_client)
        self.podcast_episodes: PodcastEpisodesApi = PodcastEpisodesApi(api_client)
        self.profile_images: ProfileImagesApi = ProfileImagesApi(api_client)
        self.reactions: ReactionsApi = ReactionsApi(api_client)
        self.readinglist: ReadinglistApi = ReadinglistApi(api_client)
        self.segments: SegmentsApi = SegmentsApi(api_client)
        self.tags: TagsApi = TagsApi(api_client)
        self.users: UsersApi = UsersApi(api_client)
        self.videos: VideosApi = VideosApi(api_client)