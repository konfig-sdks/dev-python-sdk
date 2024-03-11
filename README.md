<div align="left">

[![Visit Dev](./header.png)](https://dev.to)

# Dev<a id="dev"></a>

Access Forem articles, users and other resources via API.
        For a real-world example of Forem in action, check out [DEV](https://www.dev.to).
        All endpoints can be accessed with the 'api-key' header and a accept header, but
        some of them are accessible publicly without authentication.

        Dates and date times, unless otherwise specified, must be in
        the [RFC 3339](https://tools.ietf.org/html/rfc3339) format.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`dev.articles.create_new_article`](#devarticlescreate_new_article)
  * [`dev.articles.get_all_user_articles`](#devarticlesget_all_user_articles)
  * [`dev.articles.get_by_id`](#devarticlesget_by_id)
  * [`dev.articles.get_by_path`](#devarticlesget_by_path)
  * [`dev.articles.get_published_list`](#devarticlesget_published_list)
  * [`dev.articles.get_published_list_0`](#devarticlesget_published_list_0)
  * [`dev.articles.get_unpublished_list`](#devarticlesget_unpublished_list)
  * [`dev.articles.list_articles`](#devarticleslist_articles)
  * [`dev.articles.list_by_popularity`](#devarticleslist_by_popularity)
  * [`dev.articles.list_latest_published`](#devarticleslist_latest_published)
  * [`dev.articles.list_published_articles`](#devarticleslist_published_articles)
  * [`dev.articles.unpublish_by_id`](#devarticlesunpublish_by_id)
  * [`dev.articles.update_by_id`](#devarticlesupdate_by_id)
  * [`dev.billboards.create_new_billboard`](#devbillboardscreate_new_billboard)
  * [`dev.billboards.get_by_id`](#devbillboardsget_by_id)
  * [`dev.billboards.get_list`](#devbillboardsget_list)
  * [`dev.billboards.unpublish_billboard`](#devbillboardsunpublish_billboard)
  * [`dev.billboards.update_by_id`](#devbillboardsupdate_by_id)
  * [`dev.comments.get_all_threaded`](#devcommentsget_all_threaded)
  * [`dev.comments.get_threaded_comment`](#devcommentsget_threaded_comment)
  * [`dev.followed_tags.get_tag_list`](#devfollowed_tagsget_tag_list)
  * [`dev.followers.get_list`](#devfollowersget_list)
  * [`dev.organizations.create_new_organization`](#devorganizationscreate_new_organization)
  * [`dev.organizations.delete_by_id`](#devorganizationsdelete_by_id)
  * [`dev.organizations.get_by_id`](#devorganizationsget_by_id)
  * [`dev.organizations.get_by_username`](#devorganizationsget_by_username)
  * [`dev.organizations.list_articles`](#devorganizationslist_articles)
  * [`dev.organizations.list_of_dev`](#devorganizationslist_of_dev)
  * [`dev.organizations.list_users`](#devorganizationslist_users)
  * [`dev.organizations.update_by_id`](#devorganizationsupdate_by_id)
  * [`dev.pages.create_new_page`](#devpagescreate_new_page)
  * [`dev.pages.get_details`](#devpagesget_details)
  * [`dev.pages.list_all_details`](#devpageslist_all_details)
  * [`dev.pages.remove_page_by_id`](#devpagesremove_page_by_id)
  * [`dev.pages.update_page_details`](#devpagesupdate_page_details)
  * [`dev.podcast_episodes.list_by_descending_publication_date`](#devpodcast_episodeslist_by_descending_publication_date)
  * [`dev.profile_images.get_by_username`](#devprofile_imagesget_by_username)
  * [`dev.reactions.create_reaction`](#devreactionscreate_reaction)
  * [`dev.reactions.toggle_user_reaction`](#devreactionstoggle_user_reaction)
  * [`dev.readinglist.get_user_readinglist`](#devreadinglistget_user_readinglist)
  * [`dev.segments.add_users_to_segment`](#devsegmentsadd_users_to_segment)
  * [`dev.segments.create_manually_managed_segment`](#devsegmentscreate_manually_managed_segment)
  * [`dev.segments.delete_manually_managed_segment`](#devsegmentsdelete_manually_managed_segment)
  * [`dev.segments.get_by_id`](#devsegmentsget_by_id)
  * [`dev.segments.get_user_list_in_segment`](#devsegmentsget_user_list_in_segment)
  * [`dev.segments.list_audience_segments`](#devsegmentslist_audience_segments)
  * [`dev.segments.remove_users_from_segment`](#devsegmentsremove_users_from_segment)
  * [`dev.tags.get_tag_list`](#devtagsget_tag_list)
  * [`dev.tags.list_by_popularity`](#devtagslist_by_popularity)
  * [`dev.users.add_limited_role`](#devusersadd_limited_role)
  * [`dev.users.add_trusted_role`](#devusersadd_trusted_role)
  * [`dev.users.assign_spam_role`](#devusersassign_spam_role)
  * [`dev.users.get_all_user_articles`](#devusersget_all_user_articles)
  * [`dev.users.get_by_id_or_username`](#devusersget_by_id_or_username)
  * [`dev.users.get_information`](#devusersget_information)
  * [`dev.users.get_published_list`](#devusersget_published_list)
  * [`dev.users.get_published_list_0`](#devusersget_published_list_0)
  * [`dev.users.get_unpublished_list`](#devusersget_unpublished_list)
  * [`dev.users.invite_user`](#devusersinvite_user)
  * [`dev.users.list_users`](#devuserslist_users)
  * [`dev.users.remove_limits`](#devusersremove_limits)
  * [`dev.users.remove_spam_role`](#devusersremove_spam_role)
  * [`dev.users.remove_trusted_role`](#devusersremove_trusted_role)
  * [`dev.users.suspend_user`](#devuserssuspend_user)
  * [`dev.users.unpublish_user_articles_and_comments`](#devusersunpublish_user_articles_and_comments)
  * [`dev.videos.list_by_popularity`](#devvideoslist_by_popularity)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=DEV&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from dev_python_sdk import Dev, ApiException

dev = Dev(
    api_key="YOUR_API_KEY",
)

try:
    # Publish article
    create_new_article_response = dev.articles.create_new_article(
        article={
            "published": False,
        },
    )
    print(create_new_article_response)
except ApiException as e:
    print("Exception when calling ArticlesApi.create_new_article: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["error"])
        pprint(e.body["status"])
    if e.status == 401:
        pprint(e.body["error"])
        pprint(e.body["status"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from dev_python_sdk import Dev, ApiException

dev = Dev(
    api_key="YOUR_API_KEY",
)


async def main():
    try:
        # Publish article
        create_new_article_response = await dev.articles.acreate_new_article(
            article={
                "published": False,
            },
        )
        print(create_new_article_response)
    except ApiException as e:
        print("Exception when calling ArticlesApi.create_new_article: %s\n" % e)
        pprint(e.body)
        if e.status == 422:
            pprint(e.body["error"])
            pprint(e.body["status"])
        if e.status == 401:
            pprint(e.body["error"])
            pprint(e.body["status"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from dev_python_sdk import Dev, ApiException

dev = Dev(
    api_key="YOUR_API_KEY",
)

try:
    # Publish article
    create_new_article_response = dev.articles.raw.create_new_article(
        article={
            "published": False,
        },
    )
    pprint(create_new_article_response.body)
    pprint(create_new_article_response.body["tags"])
    pprint(create_new_article_response.body["title"])
    pprint(create_new_article_response.body["description"])
    pprint(create_new_article_response.body["type_of"])
    pprint(create_new_article_response.body["id"])
    pprint(create_new_article_response.body["readable_publish_date"])
    pprint(create_new_article_response.body["slug"])
    pprint(create_new_article_response.body["path"])
    pprint(create_new_article_response.body["url"])
    pprint(create_new_article_response.body["comments_count"])
    pprint(create_new_article_response.body["public_reactions_count"])
    pprint(create_new_article_response.body["collection_id"])
    pprint(create_new_article_response.body["published_timestamp"])
    pprint(create_new_article_response.body["positive_reactions_count"])
    pprint(create_new_article_response.body["cover_image"])
    pprint(create_new_article_response.body["social_image"])
    pprint(create_new_article_response.body["canonical_url"])
    pprint(create_new_article_response.body["created_at"])
    pprint(create_new_article_response.body["edited_at"])
    pprint(create_new_article_response.body["crossposted_at"])
    pprint(create_new_article_response.body["published_at"])
    pprint(create_new_article_response.body["last_comment_at"])
    pprint(create_new_article_response.body["reading_time_minutes"])
    pprint(create_new_article_response.body["tag_list"])
    pprint(create_new_article_response.body["body_html"])
    pprint(create_new_article_response.body["body_markdown"])
    pprint(create_new_article_response.body["user"])
    pprint(create_new_article_response.headers)
    pprint(create_new_article_response.status)
    pprint(create_new_article_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ArticlesApi.create_new_article: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["error"])
        pprint(e.body["status"])
    if e.status == 401:
        pprint(e.body["error"])
        pprint(e.body["status"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `dev.articles.create_new_article`<a id="devarticlescreate_new_article"></a>

This endpoint allows the client to create a new article.

"Articles" are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_article_response = dev.articles.create_new_article(
    article={
        "published": False,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### article: [`ArticleArticle`](./dev_python_sdk/type/article_article.py)<a id="article-articlearticledev_python_sdktypearticle_articlepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Article`](./dev_python_sdk/type/article.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesCreateNewArticleResponse`](./dev_python_sdk/pydantic/articles_create_new_article_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.get_all_user_articles`<a id="devarticlesget_all_user_articles"></a>

This endpoint allows the client to retrieve a list of all articles on behalf of an authenticated user.

"Articles" are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

It will return both published and unpublished articles with pagination.

Unpublished articles will be at the top of the list in reverse chronological creation order. Published articles will follow in reverse chronological publication order.

By default a page will contain 30 articles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_user_articles_response = dev.articles.get_all_user_articles(
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesGetAllUserArticlesResponse`](./dev_python_sdk/pydantic/articles_get_all_user_articles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/me/all` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.get_by_id`<a id="devarticlesget_by_id"></a>

This endpoint allows the client to retrieve a single published article given its `id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dev.articles.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesGetByIdResponse`](./dev_python_sdk/pydantic/articles_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.get_by_path`<a id="devarticlesget_by_path"></a>

This endpoint allows the client to retrieve a single published article given its `path`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_path_response = dev.articles.get_by_path(
    username="username_example",
    slug="slug_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

##### slug: `str`<a id="slug-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesGetByPathResponse`](./dev_python_sdk/pydantic/articles_get_by_path_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/{username}/{slug}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.get_published_list`<a id="devarticlesget_published_list"></a>

This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.

"Articles" are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

Published articles will be in reverse chronological publication order.

It will return published articles with pagination. By default a page will contain 30 articles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_published_list_response = dev.articles.get_published_list(
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesGetPublishedListResponse`](./dev_python_sdk/pydantic/articles_get_published_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.get_published_list_0`<a id="devarticlesget_published_list_0"></a>

This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.

"Articles" are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

Published articles will be in reverse chronological publication order.

It will return published articles with pagination. By default a page will contain 30 articles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_published_list_0_response = dev.articles.get_published_list_0(
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesGetPublishedList200Response`](./dev_python_sdk/pydantic/articles_get_published_list200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/me/published` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.get_unpublished_list`<a id="devarticlesget_unpublished_list"></a>

This endpoint allows the client to retrieve a list of unpublished articles on behalf of an authenticated user.

"Articles" are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

Unpublished articles will be in reverse chronological creation order.

It will return unpublished articles with pagination. By default a page will contain 30 articles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unpublished_list_response = dev.articles.get_unpublished_list(
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesGetUnpublishedListResponse`](./dev_python_sdk/pydantic/articles_get_unpublished_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/me/unpublished` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.list_articles`<a id="devarticleslist_articles"></a>

This endpoint allows the client to retrieve a list of Articles belonging to the organization

It supports pagination, each page will contain `30` users by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_articles_response = dev.articles.list_articles(
    organization_id_or_username="organization_id_or_username_example",
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id_or_username: `str`<a id="organization_id_or_username-str"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsListArticlesResponse`](./dev_python_sdk/pydantic/organizations_list_articles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/organizations/{organization_id_or_username}/articles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.list_by_popularity`<a id="devarticleslist_by_popularity"></a>

This endpoint allows the client to retrieve a list of articles that are uploaded with a video.

It will only return published video articles ordered by descending popularity.

It supports pagination, each page will contain 24 articles by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_popularity_response = dev.articles.list_by_popularity(
    page=1,
    per_page=24,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`VideosListByPopularityResponse`](./dev_python_sdk/pydantic/videos_list_by_popularity_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/videos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.list_latest_published`<a id="devarticleslist_latest_published"></a>

This endpoint allows the client to retrieve a list of articles. ordered by descending publish date.

It supports pagination, each page will contain 30 articles by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_latest_published_response = dev.articles.list_latest_published(
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesListLatestPublishedResponse`](./dev_python_sdk/pydantic/articles_list_latest_published_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/latest` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.list_published_articles`<a id="devarticleslist_published_articles"></a>

This endpoint allows the client to retrieve a list of articles.

"Articles" are all the posts that users create on DEV that typically
show up in the feed. They can be a blog post, a discussion question,
a help thread etc. but is referred to as article within the code.

By default it will return featured, published articles ordered
by descending popularity.

It supports pagination, each page will contain `30` articles by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_published_articles_response = dev.articles.list_published_articles(
    page=1,
    per_page=30,
    tag="discuss",
    tags="javascript, css",
    tags_exclude="node, java",
    username="ben",
    state="fresh",
    top=2,
    collection_id=99,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

##### tag: `str`<a id="tag-str"></a>

Using this parameter will retrieve articles that contain the requested tag. Articles will be ordered by descending popularity.This parameter can be used in conjuction with `top`.

##### tags: `str`<a id="tags-str"></a>

Using this parameter will retrieve articles with any of the comma-separated tags. Articles will be ordered by descending popularity.

##### tags_exclude: `str`<a id="tags_exclude-str"></a>

Using this parameter will retrieve articles that do _not_ contain _any_ of comma-separated tags. Articles will be ordered by descending popularity.

##### username: `str`<a id="username-str"></a>

Using this parameter will retrieve articles belonging             to a User or Organization ordered by descending publication date.             If `state=all` the number of items returned will be `1000` instead of the default `30`.             This parameter can be used in conjuction with `state`.

##### state: `str`<a id="state-str"></a>

Using this parameter will allow the client to check which articles are fresh or rising.             If `state=fresh` the server will return fresh articles.             If `state=rising` the server will return rising articles.             This param can be used in conjuction with `username`, only if set to `all`.

##### top: `int`<a id="top-int"></a>

Using this parameter will allow the client to return the most popular articles in the last `N` days. `top` indicates the number of days since publication of the articles returned. This param can be used in conjuction with `tag`.

##### collection_id: `int`<a id="collection_id-int"></a>

Adding this will allow the client to return the list of articles belonging to the requested collection, ordered by ascending publication date.

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesListPublishedArticlesResponse`](./dev_python_sdk/pydantic/articles_list_published_articles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.unpublish_by_id`<a id="devarticlesunpublish_by_id"></a>

This endpoint allows the client to unpublish an article.

The user associated with the API key must have any 'admin' or 'moderator' role.

The article will be unpublished and will no longer be visible to the public. It will remain
in the database and will set back to draft status on the author's posts dashboard. Any
notifications associated with the article will be deleted. Any comments on the article
will remain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.articles.unpublish_by_id(
    id=1,
    note="Admin requested unpublishing all articles via API",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the article to unpublish.

##### note: `str`<a id="note-str"></a>

Content for the note that's created along with unpublishing

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/{id}/unpublish` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.articles.update_by_id`<a id="devarticlesupdate_by_id"></a>

This endpoint allows the client to update an existing article.

"Articles" are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = dev.articles.update_by_id(
    id=123,
    article={
        "published": False,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the user to unpublish.

##### article: [`ArticleArticle`](./dev_python_sdk/type/article_article.py)<a id="article-articlearticledev_python_sdktypearticle_articlepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Article`](./dev_python_sdk/type/article.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesUpdateByIdResponse`](./dev_python_sdk/pydantic/articles_update_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.billboards.create_new_billboard`<a id="devbillboardscreate_new_billboard"></a>

This endpoint allows the client to create a new billboard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_billboard_response = dev.billboards.create_new_billboard(
    body=[
        {
            "name": "name_example",
            "body_markdown": "body_markdown_example",
            "placement_area": "sidebar_left",
            "audience_segment_type": "manual",
            "display_to": "all",
            "type_of": "in_house",
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BillboardsCreateNewBillboardRequest`](./dev_python_sdk/type/billboards_create_new_billboard_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BillboardsCreateNewBillboardResponse`](./dev_python_sdk/pydantic/billboards_create_new_billboard_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/billboards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.billboards.get_by_id`<a id="devbillboardsget_by_id"></a>

This endpoint allows the client to retrieve a single billboard, via its id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dev.billboards.get_by_id(
    id=123,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the billboard.

#### 🔄 Return<a id="🔄-return"></a>

[`BillboardsGetByIdResponse`](./dev_python_sdk/pydantic/billboards_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/billboards/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.billboards.get_list`<a id="devbillboardsget_list"></a>

This endpoint allows the client to retrieve a list of all billboards.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = dev.billboards.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`BillboardsGetListResponse`](./dev_python_sdk/pydantic/billboards_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/billboards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.billboards.unpublish_billboard`<a id="devbillboardsunpublish_billboard"></a>

This endpoint allows the client to remove a billboard from rotation by un-publishing it.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.billboards.unpublish_billboard(
    id=123,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the billboard to unpublish.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/billboards/{id}/unpublish` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.billboards.update_by_id`<a id="devbillboardsupdate_by_id"></a>

This endpoint allows the client to update the attributes of a single billboard, via its id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = dev.billboards.update_by_id(
    body=[
        {
            "name": "name_example",
            "body_markdown": "body_markdown_example",
            "placement_area": "sidebar_left",
            "audience_segment_type": "manual",
            "display_to": "all",
            "type_of": "in_house",
        }
    ],
    id=123,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the billboard.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BillboardsUpdateByIdRequest`](./dev_python_sdk/type/billboards_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BillboardsUpdateByIdResponse`](./dev_python_sdk/pydantic/billboards_update_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/billboards/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.comments.get_all_threaded`<a id="devcommentsget_all_threaded"></a>

This endpoint allows the client to retrieve all comments belonging to an article or podcast episode as threaded conversations.

It will return the all top level comments with their nested comments as threads. See the format specification for further details.

It supports pagination, each page will contain `50` top level comments (and as many child comments they have) by default.

If the page parameter is not passed, all comments of an article or podcast will be returned.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_threaded_response = dev.comments.get_all_threaded(
    per_page=30,
    a_id="321",
    p_id="321",
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

##### a_id: `str`<a id="a_id-str"></a>

Article identifier.

##### p_id: `str`<a id="p_id-str"></a>

Podcast Episode identifier.

##### page: `int`<a id="page-int"></a>

Pagination page

#### 🔄 Return<a id="🔄-return"></a>

[`CommentsGetAllThreadedResponse`](./dev_python_sdk/pydantic/comments_get_all_threaded_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/comments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.comments.get_threaded_comment`<a id="devcommentsget_threaded_comment"></a>

This endpoint allows the client to retrieve a comment as well as his descendants comments.

  It will return the required comment (the root) with its nested descendants as a thread.

  See the format specification for further details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_threaded_comment_response = dev.comments.get_threaded_comment(
    id=321,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Comment identifier.

#### 🔄 Return<a id="🔄-return"></a>

[`CommentsGetThreadedCommentResponse`](./dev_python_sdk/pydantic/comments_get_threaded_comment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/comments/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.followed_tags.get_tag_list`<a id="devfollowed_tagsget_tag_list"></a>

This endpoint allows the client to retrieve a list of the tags they follow.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tag_list_response = dev.followed_tags.get_tag_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`FollowedtagsGetTagListResponse`](./dev_python_sdk/pydantic/followedtags_get_tag_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/follows/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.followers.get_list`<a id="devfollowersget_list"></a>

This endpoint allows the client to retrieve a list of the followers they have.
        "Followers" are users that are following other users on the website.
        It supports pagination, each page will contain 80 followers by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = dev.followers.get_list(
    page=1,
    per_page=30,
    sort="created_at",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

##### sort: `str`<a id="sort-str"></a>

Default is 'created_at'. Specifies the sort order for the created_at param of the follow                                 relationship. To sort by newest followers first (descending order) specify                                 ?sort=-created_at.

#### 🔄 Return<a id="🔄-return"></a>

[`FollowersGetListResponse`](./dev_python_sdk/pydantic/followers_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/followers/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.organizations.create_new_organization`<a id="devorganizationscreate_new_organization"></a>

This endpoint allows the client to create an organization with the provided parameters.
        It requires a token from a user with `admin` privileges.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_organization_response = dev.organizations.create_new_organization(
    summary="string_example",
    type_of="string_example",
    username="string_example",
    name="string_example",
    twitter_username="string_example",
    github_username="string_example",
    url="string_example",
    location="string_example",
    joined_at="string_example",
    tech_stack="string_example",
    tag_line="string_example",
    story="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### summary: `str`<a id="summary-str"></a>

##### type_of: `str`<a id="type_of-str"></a>

##### username: `str`<a id="username-str"></a>

##### name: `str`<a id="name-str"></a>

##### twitter_username: `str`<a id="twitter_username-str"></a>

##### github_username: `str`<a id="github_username-str"></a>

##### url: `str`<a id="url-str"></a>

##### location: `str`<a id="location-str"></a>

##### joined_at: `str`<a id="joined_at-str"></a>

##### tech_stack: `str`<a id="tech_stack-str"></a>

##### tag_line: `Optional[str]`<a id="tag_line-optionalstr"></a>

##### story: `Optional[str]`<a id="story-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Organization`](./dev_python_sdk/type/organization.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsCreateNewOrganizationResponse`](./dev_python_sdk/pydantic/organizations_create_new_organization_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/organizations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.organizations.delete_by_id`<a id="devorganizationsdelete_by_id"></a>

This endpoint allows the client to delete a single organization, specified by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = dev.organizations.delete_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the organization.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsDeleteByIdResponse`](./dev_python_sdk/pydantic/organizations_delete_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/organizations/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.organizations.get_by_id`<a id="devorganizationsget_by_id"></a>

This endpoint allows the client to retrieve a single organization by their id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dev.organizations.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsGetByIdResponse`](./dev_python_sdk/pydantic/organizations_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/organizations/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.organizations.get_by_username`<a id="devorganizationsget_by_username"></a>

This endpoint allows the client to retrieve a single organization by their username

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_username_response = dev.organizations.get_by_username(
    username="username_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsGetByUsernameResponse`](./dev_python_sdk/pydantic/organizations_get_by_username_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/organizations/{username}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.organizations.list_articles`<a id="devorganizationslist_articles"></a>

This endpoint allows the client to retrieve a list of Articles belonging to the organization

It supports pagination, each page will contain `30` users by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_articles_response = dev.organizations.list_articles(
    organization_id_or_username="organization_id_or_username_example",
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id_or_username: `str`<a id="organization_id_or_username-str"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsListArticlesResponse`](./dev_python_sdk/pydantic/organizations_list_articles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/organizations/{organization_id_or_username}/articles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.organizations.list_of_dev`<a id="devorganizationslist_of_dev"></a>

This endpoint allows the client to retrieve a list of Dev organizations.

  It supports pagination, each page will contain 10 tags by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_of_dev_response = dev.organizations.list_of_dev(
    page=1,
    per_page=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsListOfDevResponse`](./dev_python_sdk/pydantic/organizations_list_of_dev_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/organizations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.organizations.list_users`<a id="devorganizationslist_users"></a>

This endpoint allows the client to retrieve a list of users belonging to the organization

It supports pagination, each page will contain `30` users by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_users_response = dev.organizations.list_users(
    organization_id_or_username="organization_id_or_username_example",
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id_or_username: `str`<a id="organization_id_or_username-str"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsListUsersResponse`](./dev_python_sdk/pydantic/organizations_list_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/organizations/{organization_id_or_username}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.organizations.update_by_id`<a id="devorganizationsupdate_by_id"></a>

This endpoint allows the client to update an existing organization.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = dev.organizations.update_by_id(
    id=123,
    summary="string_example",
    type_of="string_example",
    username="string_example",
    name="string_example",
    twitter_username="string_example",
    github_username="string_example",
    url="string_example",
    location="string_example",
    joined_at="string_example",
    tech_stack="string_example",
    tag_line="string_example",
    story="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the organization to update.

##### summary: `str`<a id="summary-str"></a>

##### type_of: `str`<a id="type_of-str"></a>

##### username: `str`<a id="username-str"></a>

##### name: `str`<a id="name-str"></a>

##### twitter_username: `str`<a id="twitter_username-str"></a>

##### github_username: `str`<a id="github_username-str"></a>

##### url: `str`<a id="url-str"></a>

##### location: `str`<a id="location-str"></a>

##### joined_at: `str`<a id="joined_at-str"></a>

##### tech_stack: `str`<a id="tech_stack-str"></a>

##### tag_line: `Optional[str]`<a id="tag_line-optionalstr"></a>

##### story: `Optional[str]`<a id="story-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Organization`](./dev_python_sdk/type/organization.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsUpdateByIdResponse`](./dev_python_sdk/pydantic/organizations_update_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/organizations/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.pages.create_new_page`<a id="devpagescreate_new_page"></a>

This endpoint allows the client to create a new page.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_page_response = dev.pages.create_new_page(
    title="string_example",
    description="string_example",
    slug="string_example",
    body_markdown="string_example",
    body_json="string_example",
    is_top_level_path=True,
    template="contained",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Title of the page

##### description: `str`<a id="description-str"></a>

For internal use, helps similar pages from one another

##### slug: `str`<a id="slug-str"></a>

Used to link to this page in URLs, must be unique and URL-safe

##### body_markdown: `str`<a id="body_markdown-str"></a>

The text (in markdown) of the ad (required)

##### body_json: `str`<a id="body_json-str"></a>

For JSON pages, the JSON body

##### is_top_level_path: `bool`<a id="is_top_level_path-bool"></a>

If true, the page is available at '/{slug}' instead of '/page/{slug}', use with caution

##### template: `str`<a id="template-str"></a>

Controls what kind of layout the page is rendered in

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PagesCreateNewPageRequest`](./dev_python_sdk/type/pages_create_new_page_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PagesCreateNewPageResponse`](./dev_python_sdk/pydantic/pages_create_new_page_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/pages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.pages.get_details`<a id="devpagesget_details"></a>

This endpoint allows the client to retrieve details for a single Page object, specified by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = dev.pages.get_details(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the page.

#### 🔄 Return<a id="🔄-return"></a>

[`Page`](./dev_python_sdk/pydantic/page.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/pages/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.pages.list_all_details`<a id="devpageslist_all_details"></a>

This endpoint allows the client to retrieve details for all Page objects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_details_response = dev.pages.list_all_details()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PagesListAllDetailsResponse`](./dev_python_sdk/pydantic/pages_list_all_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/pages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.pages.remove_page_by_id`<a id="devpagesremove_page_by_id"></a>

This endpoint allows the client to delete a single Page object, specified by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_page_by_id_response = dev.pages.remove_page_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the page.

#### 🔄 Return<a id="🔄-return"></a>

[`Page`](./dev_python_sdk/pydantic/page.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/pages/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.pages.update_page_details`<a id="devpagesupdate_page_details"></a>

This endpoint allows the client to retrieve details for a single Page object, specified by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_page_details_response = dev.pages.update_page_details(
    title="string_example",
    description="string_example",
    slug="string_example",
    template="contained",
    id=1,
    body_markdown="string_example",
    body_json="string_example",
    is_top_level_path=True,
    social_image={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Title of the page

##### description: `str`<a id="description-str"></a>

For internal use, helps similar pages from one another

##### slug: `str`<a id="slug-str"></a>

Used to link to this page in URLs, must be unique and URL-safe

##### template: `str`<a id="template-str"></a>

Controls what kind of layout the page is rendered in

##### id: `int`<a id="id-int"></a>

The ID of the page.

##### body_markdown: `Optional[str]`<a id="body_markdown-optionalstr"></a>

The text (in markdown) of the ad (required)

##### body_json: `Optional[str]`<a id="body_json-optionalstr"></a>

For JSON pages, the JSON body

##### is_top_level_path: `bool`<a id="is_top_level_path-bool"></a>

If true, the page is available at '/{slug}' instead of '/page/{slug}', use with caution

##### social_image: `Optional[Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="social_image-optionaldictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Page`](./dev_python_sdk/type/page.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Page`](./dev_python_sdk/pydantic/page.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/pages/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.podcast_episodes.list_by_descending_publication_date`<a id="devpodcast_episodeslist_by_descending_publication_date"></a>

This endpoint allows the client to retrieve a list of podcast episodes.
        "Podcast episodes" are episodes belonging to podcasts.
        It will only return active (reachable) podcast episodes that belong to published podcasts available on the platform, ordered by descending publication date.
        It supports pagination, each page will contain 30 articles by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_descending_publication_date_response = (
    dev.podcast_episodes.list_by_descending_publication_date(
        page=1,
        per_page=30,
        username="codenewbie",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

##### username: `str`<a id="username-str"></a>

Using this parameter will retrieve episodes belonging to a specific podcast.

#### 🔄 Return<a id="🔄-return"></a>

[`PodcastepisodesListByDescendingPublicationDateResponse`](./dev_python_sdk/pydantic/podcastepisodes_list_by_descending_publication_date_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/podcast_episodes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.profile_images.get_by_username`<a id="devprofile_imagesget_by_username"></a>

This endpoint allows the client to retrieve a user or organization profile image information by its
        corresponding username.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_username_response = dev.profile_images.get_by_username(
    username="janedoe",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

The parameter is the username of the user or the username of the organization.

#### 🔄 Return<a id="🔄-return"></a>

[`ProfileImagesGetByUsernameResponse`](./dev_python_sdk/pydantic/profile_images_get_by_username_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/profile_images/{username}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.reactions.create_reaction`<a id="devreactionscreate_reaction"></a>

This endpoint allows the client to create a reaction to a specified reactable (eg, Article, Comment, or User). For examples:
        * "Like"ing an Article will create a new "like" Reaction from the user for that Articles
        * "Like"ing that Article a second time will return the previous "like"

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_reaction_response = dev.reactions.create_reaction(
    category="like",
    reactable_id=1,
    reactable_type="Comment",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category: `str`<a id="category-str"></a>

##### reactable_id: `int`<a id="reactable_id-int"></a>

##### reactable_type: `str`<a id="reactable_type-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ReactionsCreateReactionResponse`](./dev_python_sdk/pydantic/reactions_create_reaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/reactions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.reactions.toggle_user_reaction`<a id="devreactionstoggle_user_reaction"></a>

This endpoint allows the client to toggle the user's reaction to a specified reactable (eg, Article, Comment, or User). For examples:
        * "Like"ing an Article will create a new "like" Reaction from the user for that Articles
        * "Like"ing that Article a second time will remove the "like" from the user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
toggle_user_reaction_response = dev.reactions.toggle_user_reaction(
    category="like",
    reactable_id=1,
    reactable_type="Comment",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category: `str`<a id="category-str"></a>

##### reactable_id: `int`<a id="reactable_id-int"></a>

##### reactable_type: `str`<a id="reactable_type-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ReactionsToggleUserReactionResponse`](./dev_python_sdk/pydantic/reactions_toggle_user_reaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/reactions/toggle` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.readinglist.get_user_readinglist`<a id="devreadinglistget_user_readinglist"></a>

This endpoint allows the client to retrieve a list of articles that were saved to a Users readinglist.
        It supports pagination, each page will contain `30` articles by default

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_readinglist_response = dev.readinglist.get_user_readinglist(
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ReadinglistGetUserReadinglistResponse`](./dev_python_sdk/pydantic/readinglist_get_user_readinglist_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/readinglist` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.segments.add_users_to_segment`<a id="devsegmentsadd_users_to_segment"></a>

This endpoint allows the client to add users in bulk to an audience segment specified by ID.

Successes are users that were included in the segment (even if they were already in it), and failures are users that could not be added to the segment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_users_to_segment_response = dev.segments.add_users_to_segment(
    id=1,
    user_ids=[1],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### user_ids: [`SegmentUserIdsUserIds`](./dev_python_sdk/type/segment_user_ids_user_ids.py)<a id="user_ids-segmentuseridsuseridsdev_python_sdktypesegment_user_ids_user_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SegmentUserIds`](./dev_python_sdk/type/segment_user_ids.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SegmentsAddUsersToSegmentResponse`](./dev_python_sdk/pydantic/segments_add_users_to_segment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/segments/{id}/add_users` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.segments.create_manually_managed_segment`<a id="devsegmentscreate_manually_managed_segment"></a>

This endpoint allows the client to create a new audience segment.

An audience segment is a group of users that can be targeted by a Billboard. This API only permits managing segments you create and maintain yourself.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_manually_managed_segment_response = (
    dev.segments.create_manually_managed_segment()
)
```

#### 🔄 Return<a id="🔄-return"></a>

[`SegmentsCreateManuallyManagedSegmentResponse`](./dev_python_sdk/pydantic/segments_create_manually_managed_segment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/segments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.segments.delete_manually_managed_segment`<a id="devsegmentsdelete_manually_managed_segment"></a>

This endpoint allows the client to delete an audience segment specified by ID.

Audience segments cannot be deleted if there are still any Billboards using them.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_manually_managed_segment_response = dev.segments.delete_manually_managed_segment(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SegmentsDeleteManuallyManagedSegmentResponse`](./dev_python_sdk/pydantic/segments_delete_manually_managed_segment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/segments/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.segments.get_by_id`<a id="devsegmentsget_by_id"></a>

This endpoint allows the client to retrieve a single manually-managed audience segment specified by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dev.segments.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SegmentsGetByIdResponse`](./dev_python_sdk/pydantic/segments_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/segments/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.segments.get_user_list_in_segment`<a id="devsegmentsget_user_list_in_segment"></a>

This endpoint allows the client to retrieve a list of the users in an audience segment specified by ID. The endpoint supports pagination, and each page will contain `30` users by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_list_in_segment_response = dev.segments.get_user_list_in_segment(
    id=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`SegmentsGetUserListInSegmentResponse`](./dev_python_sdk/pydantic/segments_get_user_list_in_segment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/segments/{id}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.segments.list_audience_segments`<a id="devsegmentslist_audience_segments"></a>

This endpoint allows the client to retrieve a list of audience segments.

An audience segment is a group of users that can be targeted by a Billboard. This API only permits managing segments you create and maintain yourself.

The endpoint supports pagination, and each page will contain `30` segments by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_audience_segments_response = dev.segments.list_audience_segments(
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`SegmentsListAudienceSegmentsResponse`](./dev_python_sdk/pydantic/segments_list_audience_segments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/segments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.segments.remove_users_from_segment`<a id="devsegmentsremove_users_from_segment"></a>

This endpoint allows the client to remove users in bulk from an audience segment specified by ID.

Successes are users that were removed; failures are users that weren't a part of the segment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_users_from_segment_response = dev.segments.remove_users_from_segment(
    id=1,
    user_ids=[1],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### user_ids: [`SegmentUserIdsUserIds`](./dev_python_sdk/type/segment_user_ids_user_ids.py)<a id="user_ids-segmentuseridsuseridsdev_python_sdktypesegment_user_ids_user_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SegmentUserIds`](./dev_python_sdk/type/segment_user_ids.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SegmentsRemoveUsersFromSegmentResponse`](./dev_python_sdk/pydantic/segments_remove_users_from_segment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/segments/{id}/remove_users` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.tags.get_tag_list`<a id="devtagsget_tag_list"></a>

This endpoint allows the client to retrieve a list of the tags they follow.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tag_list_response = dev.tags.get_tag_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`FollowedtagsGetTagListResponse`](./dev_python_sdk/pydantic/followedtags_get_tag_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/follows/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.tags.list_by_popularity`<a id="devtagslist_by_popularity"></a>

This endpoint allows the client to retrieve a list of tags that can be used to tag articles.

It will return tags ordered by popularity.

It supports pagination, each page will contain 10 tags by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_popularity_response = dev.tags.list_by_popularity(
    page=1,
    per_page=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`TagsListByPopularityResponse`](./dev_python_sdk/pydantic/tags_list_by_popularity_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.add_limited_role`<a id="devusersadd_limited_role"></a>

This endpoint allows the client to limit a user.

The user associated with the API key must have any 'admin' or 'moderator' role.

This specified user will be assigned the 'limited' role. Limiting a user will limit notifications
generated from new posts and comments. It doesn't delete any of the user's content or prevent them
from generating new content while limited. Users are not notified of their limits
in the UI, so if you want them to know about this, you must notify them.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.users.add_limited_role(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the user to limit.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/{id}/limited` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.add_trusted_role`<a id="devusersadd_trusted_role"></a>

This endpoint allows the client to add the trusted role to a user.
          The user associated with the API key must have an 'admin' or 'moderator' role.
          The specified user will be assigned the 'trusted' role. Adding the trusted role to a user
          allows them to upvote and downvote posts and flag content that needs investigating by admins.
          Users are notified of this change in the UI, and by email.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.users.add_trusted_role(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the user to assign the trusted role.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/{id}/trusted` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.assign_spam_role`<a id="devusersassign_spam_role"></a>

This endpoint allows the client to add the spam role to a user.

          The user associated with the API key must have any 'admin' or 'moderator' role.

          This specified user will be assigned the 'spam' role. Addding the spam role to a user will stop the
          user from posting new posts and comments. It doesn't delete any of the user's content, just
          prevents them from creating new content while having the spam role. Users are not notified of their spaminess
          in the UI, so if you want them to know about this, you must notify them

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.users.assign_spam_role(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the user to assign the spam role.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/{id}/spam` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.get_all_user_articles`<a id="devusersget_all_user_articles"></a>

This endpoint allows the client to retrieve a list of all articles on behalf of an authenticated user.

"Articles" are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

It will return both published and unpublished articles with pagination.

Unpublished articles will be at the top of the list in reverse chronological creation order. Published articles will follow in reverse chronological publication order.

By default a page will contain 30 articles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_user_articles_response = dev.users.get_all_user_articles(
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesGetAllUserArticlesResponse`](./dev_python_sdk/pydantic/articles_get_all_user_articles_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/me/all` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.get_by_id_or_username`<a id="devusersget_by_id_or_username"></a>

This endpoint allows the client to retrieve a single user, either by id
or by the user's username.

For complete documentation, see the v0 API docs: https://developers.forem.com/api/v0#tag/users/operation/getUser

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_or_username_response = dev.users.get_by_id_or_username(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetByIdOrUsernameResponse`](./dev_python_sdk/pydantic/users_get_by_id_or_username_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.get_information`<a id="devusersget_information"></a>

This endpoint allows the client to retrieve information about the authenticated user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = dev.users.get_information()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetInformationResponse`](./dev_python_sdk/pydantic/users_get_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.get_published_list`<a id="devusersget_published_list"></a>

This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.

"Articles" are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

Published articles will be in reverse chronological publication order.

It will return published articles with pagination. By default a page will contain 30 articles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_published_list_response = dev.users.get_published_list(
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesGetPublishedListResponse`](./dev_python_sdk/pydantic/articles_get_published_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.get_published_list_0`<a id="devusersget_published_list_0"></a>

This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.

"Articles" are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

Published articles will be in reverse chronological publication order.

It will return published articles with pagination. By default a page will contain 30 articles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_published_list_0_response = dev.users.get_published_list_0(
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesGetPublishedList200Response`](./dev_python_sdk/pydantic/articles_get_published_list200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/me/published` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.get_unpublished_list`<a id="devusersget_unpublished_list"></a>

This endpoint allows the client to retrieve a list of unpublished articles on behalf of an authenticated user.

"Articles" are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

Unpublished articles will be in reverse chronological creation order.

It will return unpublished articles with pagination. By default a page will contain 30 articles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unpublished_list_response = dev.users.get_unpublished_list(
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`ArticlesGetUnpublishedListResponse`](./dev_python_sdk/pydantic/articles_get_unpublished_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/articles/me/unpublished` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.invite_user`<a id="devusersinvite_user"></a>

This endpoint allows the client to trigger an invitation to the provided email address.

        It requires a token from a user with `super_admin` privileges.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.users.invite_user(
    email="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

##### name: `Optional[str]`<a id="name-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserInviteParam`](./dev_python_sdk/type/user_invite_param.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/admin/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.list_users`<a id="devuserslist_users"></a>

This endpoint allows the client to retrieve a list of users belonging to the organization

It supports pagination, each page will contain `30` users by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_users_response = dev.users.list_users(
    organization_id_or_username="organization_id_or_username_example",
    page=1,
    per_page=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### organization_id_or_username: `str`<a id="organization_id_or_username-str"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`OrganizationsListUsersResponse`](./dev_python_sdk/pydantic/organizations_list_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/organizations/{organization_id_or_username}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.remove_limits`<a id="devusersremove_limits"></a>

This endpoint allows the client to remove limits for a user.

The user associated with the API key must have any 'admin' or 'moderator' role.

This specified user will be restored to 'general' status. Users are not notified
of limits in the UI, so if you want them to know about this, you must
notify them.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.users.remove_limits(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the user to un-limit.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/{id}/limited` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.remove_spam_role`<a id="devusersremove_spam_role"></a>

This endpoint allows the client to remove the spam role for a user.

          The user associated with the API key must have any 'admin' or 'moderator' role.

          This specified user will be restored to 'general' status. Users are not notified
          of removing their spam role in the UI, so if you want them to know about this, you must
          notify them.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.users.remove_spam_role(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the user to remove the spam role from.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/{id}/spam` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.remove_trusted_role`<a id="devusersremove_trusted_role"></a>

This endpoint allows the client to remove the trusted role for a user.
          The user associated with the API key must have an 'admin' or 'moderator' role.
          The specified user will be restored to 'general' status. Users are not notified
          of removing their trusted role in the UI, so if you want them to know about this, you must
          notify them.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.users.remove_trusted_role(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the user to remove the trusted role from.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/{id}/trusted` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.suspend_user`<a id="devuserssuspend_user"></a>

This endpoint allows the client to suspend a user.

The user associated with the API key must have any 'admin' or 'moderator' role.

This specified user will be assigned the 'suspended' role. Suspending a user will stop the
user from posting new posts and comments. It doesn't delete any of the user's content, just
prevents them from creating new content while suspended. Users are not notified of their suspension
in the UI, so if you want them to know about this, you must notify them.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.users.suspend_user(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the user to suspend.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/{id}/suspend` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.users.unpublish_user_articles_and_comments`<a id="devusersunpublish_user_articles_and_comments"></a>

This endpoint allows the client to unpublish all of the articles and
comments created by a user.

The user associated with the API key must have any 'admin' or 'moderator' role.

This specified user's articles and comments will be unpublished and will no longer be
visible to the public. They will remain in the database and will set back to draft status
on the specified user's  dashboard. Any notifications associated with the specified user's
articles and comments will be deleted.

Note this endpoint unpublishes articles and comments asychronously: it will return a 204 NO CONTENT
status code immediately, but the articles and comments will not be unpublished until the
request is completed on the server.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dev.users.unpublish_user_articles_and_comments(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the user to unpublish.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/users/{id}/unpublish` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dev.videos.list_by_popularity`<a id="devvideoslist_by_popularity"></a>

This endpoint allows the client to retrieve a list of articles that are uploaded with a video.

It will only return published video articles ordered by descending popularity.

It supports pagination, each page will contain 24 articles by default.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_popularity_response = dev.videos.list_by_popularity(
    page=1,
    per_page=24,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Pagination page

##### per_page: `int`<a id="per_page-int"></a>

Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.

#### 🔄 Return<a id="🔄-return"></a>

[`VideosListByPopularityResponse`](./dev_python_sdk/pydantic/videos_list_by_popularity_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/videos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
