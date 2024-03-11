# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from dev_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    USERS = "users"
    ARTICLES = "articles"
    ORGANIZATIONS = "organizations"
    SEGMENTS = "segments"
    BILLBOARDS = "billboards"
    PAGES = "pages"
    COMMENTS = "comments"
    TAGS = "tags"
    REACTIONS = "reactions"
    FOLLOWED_TAGS = "followed_tags"
    FOLLOWERS = "followers"
    PODCAST_EPISODES = "podcast_episodes"
    PROFILE_IMAGES = "profile images"
    READINGLIST = "readinglist"
    VIDEOS = "videos"
