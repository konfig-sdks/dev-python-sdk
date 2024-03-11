import typing_extensions

from dev_python_sdk.apis.tags import TagValues
from dev_python_sdk.apis.tags.users_api import UsersApi
from dev_python_sdk.apis.tags.articles_api import ArticlesApi
from dev_python_sdk.apis.tags.organizations_api import OrganizationsApi
from dev_python_sdk.apis.tags.segments_api import SegmentsApi
from dev_python_sdk.apis.tags.billboards_api import BillboardsApi
from dev_python_sdk.apis.tags.pages_api import PagesApi
from dev_python_sdk.apis.tags.comments_api import CommentsApi
from dev_python_sdk.apis.tags.tags_api import TagsApi
from dev_python_sdk.apis.tags.reactions_api import ReactionsApi
from dev_python_sdk.apis.tags.followed_tags_api import FollowedTagsApi
from dev_python_sdk.apis.tags.followers_api import FollowersApi
from dev_python_sdk.apis.tags.podcast_episodes_api import PodcastEpisodesApi
from dev_python_sdk.apis.tags.profile_images_api import ProfileImagesApi
from dev_python_sdk.apis.tags.readinglist_api import ReadinglistApi
from dev_python_sdk.apis.tags.videos_api import VideosApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USERS: UsersApi,
        TagValues.ARTICLES: ArticlesApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.BILLBOARDS: BillboardsApi,
        TagValues.PAGES: PagesApi,
        TagValues.COMMENTS: CommentsApi,
        TagValues.TAGS: TagsApi,
        TagValues.REACTIONS: ReactionsApi,
        TagValues.FOLLOWED_TAGS: FollowedTagsApi,
        TagValues.FOLLOWERS: FollowersApi,
        TagValues.PODCAST_EPISODES: PodcastEpisodesApi,
        TagValues.PROFILE_IMAGES: ProfileImagesApi,
        TagValues.READINGLIST: ReadinglistApi,
        TagValues.VIDEOS: VideosApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USERS: UsersApi,
        TagValues.ARTICLES: ArticlesApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.BILLBOARDS: BillboardsApi,
        TagValues.PAGES: PagesApi,
        TagValues.COMMENTS: CommentsApi,
        TagValues.TAGS: TagsApi,
        TagValues.REACTIONS: ReactionsApi,
        TagValues.FOLLOWED_TAGS: FollowedTagsApi,
        TagValues.FOLLOWERS: FollowersApi,
        TagValues.PODCAST_EPISODES: PodcastEpisodesApi,
        TagValues.PROFILE_IMAGES: ProfileImagesApi,
        TagValues.READINGLIST: ReadinglistApi,
        TagValues.VIDEOS: VideosApi,
    }
)
