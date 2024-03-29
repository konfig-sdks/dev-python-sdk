# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dev_python_sdk.paths.api_articles.post import CreateNewArticle
from dev_python_sdk.paths.api_articles_me_all.get import GetAllUserArticles
from dev_python_sdk.paths.api_articles_id.get import GetById
from dev_python_sdk.paths.api_articles_username_slug.get import GetByPath
from dev_python_sdk.paths.api_articles_me.get import GetPublishedList
from dev_python_sdk.paths.api_articles_me_published.get import GetPublishedList0
from dev_python_sdk.paths.api_articles_me_unpublished.get import GetUnpublishedList
from dev_python_sdk.paths.api_organizations_organization_id_or_username_articles.get import ListArticles
from dev_python_sdk.paths.api_videos.get import ListByPopularity
from dev_python_sdk.paths.api_articles_latest.get import ListLatestPublished
from dev_python_sdk.paths.api_articles.get import ListPublishedArticles
from dev_python_sdk.paths.api_articles_id_unpublish.put import UnpublishById
from dev_python_sdk.paths.api_articles_id.put import UpdateById
from dev_python_sdk.apis.tags.articles_api_raw import ArticlesApiRaw


class ArticlesApi(
    CreateNewArticle,
    GetAllUserArticles,
    GetById,
    GetByPath,
    GetPublishedList,
    GetPublishedList0,
    GetUnpublishedList,
    ListArticles,
    ListByPopularity,
    ListLatestPublished,
    ListPublishedArticles,
    UnpublishById,
    UpdateById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ArticlesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ArticlesApiRaw(api_client)
