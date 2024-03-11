import typing_extensions

from dev_python_sdk.paths import PathValues
from dev_python_sdk.apis.paths.api_articles import ApiArticles
from dev_python_sdk.apis.paths.api_articles_latest import ApiArticlesLatest
from dev_python_sdk.apis.paths.api_articles_id import ApiArticlesId
from dev_python_sdk.apis.paths.api_articles_username_slug import ApiArticlesUsernameSlug
from dev_python_sdk.apis.paths.api_articles_me import ApiArticlesMe
from dev_python_sdk.apis.paths.api_articles_me_published import ApiArticlesMePublished
from dev_python_sdk.apis.paths.api_articles_me_unpublished import ApiArticlesMeUnpublished
from dev_python_sdk.apis.paths.api_articles_me_all import ApiArticlesMeAll
from dev_python_sdk.apis.paths.api_articles_id_unpublish import ApiArticlesIdUnpublish
from dev_python_sdk.apis.paths.api_segments import ApiSegments
from dev_python_sdk.apis.paths.api_segments_id import ApiSegmentsId
from dev_python_sdk.apis.paths.api_segments_id_users import ApiSegmentsIdUsers
from dev_python_sdk.apis.paths.api_segments_id_add_users import ApiSegmentsIdAddUsers
from dev_python_sdk.apis.paths.api_segments_id_remove_users import ApiSegmentsIdRemoveUsers
from dev_python_sdk.apis.paths.api_billboards import ApiBillboards
from dev_python_sdk.apis.paths.api_billboards_id import ApiBillboardsId
from dev_python_sdk.apis.paths.api_billboards_id_unpublish import ApiBillboardsIdUnpublish
from dev_python_sdk.apis.paths.api_comments import ApiComments
from dev_python_sdk.apis.paths.api_comments_id import ApiCommentsId
from dev_python_sdk.apis.paths.api_follows_tags import ApiFollowsTags
from dev_python_sdk.apis.paths.api_followers_users import ApiFollowersUsers
from dev_python_sdk.apis.paths.api_organizations_username import ApiOrganizationsUsername
from dev_python_sdk.apis.paths.api_organizations_organization_id_or_username_users import ApiOrganizationsOrganizationIdOrUsernameUsers
from dev_python_sdk.apis.paths.api_organizations_organization_id_or_username_articles import ApiOrganizationsOrganizationIdOrUsernameArticles
from dev_python_sdk.apis.paths.api_organizations import ApiOrganizations
from dev_python_sdk.apis.paths.api_organizations_id import ApiOrganizationsId
from dev_python_sdk.apis.paths.api_pages import ApiPages
from dev_python_sdk.apis.paths.api_pages_id import ApiPagesId
from dev_python_sdk.apis.paths.api_podcast_episodes import ApiPodcastEpisodes
from dev_python_sdk.apis.paths.api_profile_images_username import ApiProfileImagesUsername
from dev_python_sdk.apis.paths.api_reactions_toggle import ApiReactionsToggle
from dev_python_sdk.apis.paths.api_reactions import ApiReactions
from dev_python_sdk.apis.paths.api_readinglist import ApiReadinglist
from dev_python_sdk.apis.paths.api_tags import ApiTags
from dev_python_sdk.apis.paths.api_users_id_suspend import ApiUsersIdSuspend
from dev_python_sdk.apis.paths.api_users_id_limited import ApiUsersIdLimited
from dev_python_sdk.apis.paths.api_users_id_spam import ApiUsersIdSpam
from dev_python_sdk.apis.paths.api_users_id_trusted import ApiUsersIdTrusted
from dev_python_sdk.apis.paths.api_users_me import ApiUsersMe
from dev_python_sdk.apis.paths.api_users_id import ApiUsersId
from dev_python_sdk.apis.paths.api_users_id_unpublish import ApiUsersIdUnpublish
from dev_python_sdk.apis.paths.api_admin_users import ApiAdminUsers
from dev_python_sdk.apis.paths.api_videos import ApiVideos

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_ARTICLES: ApiArticles,
        PathValues.API_ARTICLES_LATEST: ApiArticlesLatest,
        PathValues.API_ARTICLES_ID: ApiArticlesId,
        PathValues.API_ARTICLES_USERNAME_SLUG: ApiArticlesUsernameSlug,
        PathValues.API_ARTICLES_ME: ApiArticlesMe,
        PathValues.API_ARTICLES_ME_PUBLISHED: ApiArticlesMePublished,
        PathValues.API_ARTICLES_ME_UNPUBLISHED: ApiArticlesMeUnpublished,
        PathValues.API_ARTICLES_ME_ALL: ApiArticlesMeAll,
        PathValues.API_ARTICLES_ID_UNPUBLISH: ApiArticlesIdUnpublish,
        PathValues.API_SEGMENTS: ApiSegments,
        PathValues.API_SEGMENTS_ID: ApiSegmentsId,
        PathValues.API_SEGMENTS_ID_USERS: ApiSegmentsIdUsers,
        PathValues.API_SEGMENTS_ID_ADD_USERS: ApiSegmentsIdAddUsers,
        PathValues.API_SEGMENTS_ID_REMOVE_USERS: ApiSegmentsIdRemoveUsers,
        PathValues.API_BILLBOARDS: ApiBillboards,
        PathValues.API_BILLBOARDS_ID: ApiBillboardsId,
        PathValues.API_BILLBOARDS_ID_UNPUBLISH: ApiBillboardsIdUnpublish,
        PathValues.API_COMMENTS: ApiComments,
        PathValues.API_COMMENTS_ID: ApiCommentsId,
        PathValues.API_FOLLOWS_TAGS: ApiFollowsTags,
        PathValues.API_FOLLOWERS_USERS: ApiFollowersUsers,
        PathValues.API_ORGANIZATIONS_USERNAME: ApiOrganizationsUsername,
        PathValues.API_ORGANIZATIONS_ORGANIZATION_ID_OR_USERNAME_USERS: ApiOrganizationsOrganizationIdOrUsernameUsers,
        PathValues.API_ORGANIZATIONS_ORGANIZATION_ID_OR_USERNAME_ARTICLES: ApiOrganizationsOrganizationIdOrUsernameArticles,
        PathValues.API_ORGANIZATIONS: ApiOrganizations,
        PathValues.API_ORGANIZATIONS_ID: ApiOrganizationsId,
        PathValues.API_PAGES: ApiPages,
        PathValues.API_PAGES_ID: ApiPagesId,
        PathValues.API_PODCAST_EPISODES: ApiPodcastEpisodes,
        PathValues.API_PROFILE_IMAGES_USERNAME: ApiProfileImagesUsername,
        PathValues.API_REACTIONS_TOGGLE: ApiReactionsToggle,
        PathValues.API_REACTIONS: ApiReactions,
        PathValues.API_READINGLIST: ApiReadinglist,
        PathValues.API_TAGS: ApiTags,
        PathValues.API_USERS_ID_SUSPEND: ApiUsersIdSuspend,
        PathValues.API_USERS_ID_LIMITED: ApiUsersIdLimited,
        PathValues.API_USERS_ID_SPAM: ApiUsersIdSpam,
        PathValues.API_USERS_ID_TRUSTED: ApiUsersIdTrusted,
        PathValues.API_USERS_ME: ApiUsersMe,
        PathValues.API_USERS_ID: ApiUsersId,
        PathValues.API_USERS_ID_UNPUBLISH: ApiUsersIdUnpublish,
        PathValues.API_ADMIN_USERS: ApiAdminUsers,
        PathValues.API_VIDEOS: ApiVideos,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_ARTICLES: ApiArticles,
        PathValues.API_ARTICLES_LATEST: ApiArticlesLatest,
        PathValues.API_ARTICLES_ID: ApiArticlesId,
        PathValues.API_ARTICLES_USERNAME_SLUG: ApiArticlesUsernameSlug,
        PathValues.API_ARTICLES_ME: ApiArticlesMe,
        PathValues.API_ARTICLES_ME_PUBLISHED: ApiArticlesMePublished,
        PathValues.API_ARTICLES_ME_UNPUBLISHED: ApiArticlesMeUnpublished,
        PathValues.API_ARTICLES_ME_ALL: ApiArticlesMeAll,
        PathValues.API_ARTICLES_ID_UNPUBLISH: ApiArticlesIdUnpublish,
        PathValues.API_SEGMENTS: ApiSegments,
        PathValues.API_SEGMENTS_ID: ApiSegmentsId,
        PathValues.API_SEGMENTS_ID_USERS: ApiSegmentsIdUsers,
        PathValues.API_SEGMENTS_ID_ADD_USERS: ApiSegmentsIdAddUsers,
        PathValues.API_SEGMENTS_ID_REMOVE_USERS: ApiSegmentsIdRemoveUsers,
        PathValues.API_BILLBOARDS: ApiBillboards,
        PathValues.API_BILLBOARDS_ID: ApiBillboardsId,
        PathValues.API_BILLBOARDS_ID_UNPUBLISH: ApiBillboardsIdUnpublish,
        PathValues.API_COMMENTS: ApiComments,
        PathValues.API_COMMENTS_ID: ApiCommentsId,
        PathValues.API_FOLLOWS_TAGS: ApiFollowsTags,
        PathValues.API_FOLLOWERS_USERS: ApiFollowersUsers,
        PathValues.API_ORGANIZATIONS_USERNAME: ApiOrganizationsUsername,
        PathValues.API_ORGANIZATIONS_ORGANIZATION_ID_OR_USERNAME_USERS: ApiOrganizationsOrganizationIdOrUsernameUsers,
        PathValues.API_ORGANIZATIONS_ORGANIZATION_ID_OR_USERNAME_ARTICLES: ApiOrganizationsOrganizationIdOrUsernameArticles,
        PathValues.API_ORGANIZATIONS: ApiOrganizations,
        PathValues.API_ORGANIZATIONS_ID: ApiOrganizationsId,
        PathValues.API_PAGES: ApiPages,
        PathValues.API_PAGES_ID: ApiPagesId,
        PathValues.API_PODCAST_EPISODES: ApiPodcastEpisodes,
        PathValues.API_PROFILE_IMAGES_USERNAME: ApiProfileImagesUsername,
        PathValues.API_REACTIONS_TOGGLE: ApiReactionsToggle,
        PathValues.API_REACTIONS: ApiReactions,
        PathValues.API_READINGLIST: ApiReadinglist,
        PathValues.API_TAGS: ApiTags,
        PathValues.API_USERS_ID_SUSPEND: ApiUsersIdSuspend,
        PathValues.API_USERS_ID_LIMITED: ApiUsersIdLimited,
        PathValues.API_USERS_ID_SPAM: ApiUsersIdSpam,
        PathValues.API_USERS_ID_TRUSTED: ApiUsersIdTrusted,
        PathValues.API_USERS_ME: ApiUsersMe,
        PathValues.API_USERS_ID: ApiUsersId,
        PathValues.API_USERS_ID_UNPUBLISH: ApiUsersIdUnpublish,
        PathValues.API_ADMIN_USERS: ApiAdminUsers,
        PathValues.API_VIDEOS: ApiVideos,
    }
)
