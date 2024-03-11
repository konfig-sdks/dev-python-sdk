# coding: utf-8

"""
    Forem API V1

    Access Forem articles, users and other resources via API.         For a real-world example of Forem in action, check out [DEV](https://www.dev.to).         All endpoints can be accessed with the 'api-key' header and a accept header, but         some of them are accessible publicly without authentication.          Dates and date times, unless otherwise specified, must be in         the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dev_python_sdk.paths.api_users_id_limited.put import AddLimitedRole
from dev_python_sdk.paths.api_users_id_trusted.put import AddTrustedRole
from dev_python_sdk.paths.api_users_id_spam.put import AssignSpamRole
from dev_python_sdk.paths.api_articles_me_all.get import GetAllUserArticles
from dev_python_sdk.paths.api_users_id.get import GetByIdOrUsername
from dev_python_sdk.paths.api_users_me.get import GetInformation
from dev_python_sdk.paths.api_articles_me.get import GetPublishedList
from dev_python_sdk.paths.api_articles_me_published.get import GetPublishedList0
from dev_python_sdk.paths.api_articles_me_unpublished.get import GetUnpublishedList
from dev_python_sdk.paths.api_admin_users.post import InviteUser
from dev_python_sdk.paths.api_organizations_organization_id_or_username_users.get import ListUsers
from dev_python_sdk.paths.api_users_id_limited.delete import RemoveLimits
from dev_python_sdk.paths.api_users_id_spam.delete import RemoveSpamRole
from dev_python_sdk.paths.api_users_id_trusted.delete import RemoveTrustedRole
from dev_python_sdk.paths.api_users_id_suspend.put import SuspendUser
from dev_python_sdk.paths.api_users_id_unpublish.put import UnpublishUserArticlesAndComments
from dev_python_sdk.apis.tags.users_api_raw import UsersApiRaw


class UsersApi(
    AddLimitedRole,
    AddTrustedRole,
    AssignSpamRole,
    GetAllUserArticles,
    GetByIdOrUsername,
    GetInformation,
    GetPublishedList,
    GetPublishedList0,
    GetUnpublishedList,
    InviteUser,
    ListUsers,
    RemoveLimits,
    RemoveSpamRole,
    RemoveTrustedRole,
    SuspendUser,
    UnpublishUserArticlesAndComments,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UsersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UsersApiRaw(api_client)
