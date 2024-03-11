# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from dev_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_ARTICLES = "/api/articles"
    API_ARTICLES_LATEST = "/api/articles/latest"
    API_ARTICLES_ID = "/api/articles/{id}"
    API_ARTICLES_USERNAME_SLUG = "/api/articles/{username}/{slug}"
    API_ARTICLES_ME = "/api/articles/me"
    API_ARTICLES_ME_PUBLISHED = "/api/articles/me/published"
    API_ARTICLES_ME_UNPUBLISHED = "/api/articles/me/unpublished"
    API_ARTICLES_ME_ALL = "/api/articles/me/all"
    API_ARTICLES_ID_UNPUBLISH = "/api/articles/{id}/unpublish"
    API_SEGMENTS = "/api/segments"
    API_SEGMENTS_ID = "/api/segments/{id}"
    API_SEGMENTS_ID_USERS = "/api/segments/{id}/users"
    API_SEGMENTS_ID_ADD_USERS = "/api/segments/{id}/add_users"
    API_SEGMENTS_ID_REMOVE_USERS = "/api/segments/{id}/remove_users"
    API_BILLBOARDS = "/api/billboards"
    API_BILLBOARDS_ID = "/api/billboards/{id}"
    API_BILLBOARDS_ID_UNPUBLISH = "/api/billboards/{id}/unpublish"
    API_COMMENTS = "/api/comments"
    API_COMMENTS_ID = "/api/comments/{id}"
    API_FOLLOWS_TAGS = "/api/follows/tags"
    API_FOLLOWERS_USERS = "/api/followers/users"
    API_ORGANIZATIONS_USERNAME = "/api/organizations/{username}"
    API_ORGANIZATIONS_ORGANIZATION_ID_OR_USERNAME_USERS = "/api/organizations/{organization_id_or_username}/users"
    API_ORGANIZATIONS_ORGANIZATION_ID_OR_USERNAME_ARTICLES = "/api/organizations/{organization_id_or_username}/articles"
    API_ORGANIZATIONS = "/api/organizations"
    API_ORGANIZATIONS_ID = "/api/organizations/{id}"
    API_PAGES = "/api/pages"
    API_PAGES_ID = "/api/pages/{id}"
    API_PODCAST_EPISODES = "/api/podcast_episodes"
    API_PROFILE_IMAGES_USERNAME = "/api/profile_images/{username}"
    API_REACTIONS_TOGGLE = "/api/reactions/toggle"
    API_REACTIONS = "/api/reactions"
    API_READINGLIST = "/api/readinglist"
    API_TAGS = "/api/tags"
    API_USERS_ID_SUSPEND = "/api/users/{id}/suspend"
    API_USERS_ID_LIMITED = "/api/users/{id}/limited"
    API_USERS_ID_SPAM = "/api/users/{id}/spam"
    API_USERS_ID_TRUSTED = "/api/users/{id}/trusted"
    API_USERS_ME = "/api/users/me"
    API_USERS_ID = "/api/users/{id}"
    API_USERS_ID_UNPUBLISH = "/api/users/{id}/unpublish"
    API_ADMIN_USERS = "/api/admin/users"
    API_VIDEOS = "/api/videos"
