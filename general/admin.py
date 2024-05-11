from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from general.models import (
    User,
    Post,
    Comment,
    Reaction,
)
from django.contrib.auth.models import Group
from rangefilter.filters import DateRangeFilter
from general.filters import AuthorFilter, PostFilter
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    )
    fields = (
        "first_name",
        "last_name",
        "username",
        "password",
        "email",
        "is_staff",
    )
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    search_fields = (
        "id",
        "username",
        "email",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        ("date_joined", DateRangeFilter),
        # ("created_at", DateRangeFilter),
    )


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "get_body",
        "created_at",
    )

    def get_body(self, obj):
        max_length = 64
        if len(obj.body) > max_length:
            return obj.body[:61] + "..."
        return obj.body

    get_body.short_description = "body"

    def get_comment_count(self, obj):
        return obj.comments.count()
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("comments")

    search_fields = (
        "id",
        "title",
        "author__username",
    )
    list_filter = (
        AuthorFilter,
        ("created_at", DateRangeFilter),
    )
    autocomplete_fields = (
        "author",
        # "post",
    )


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "post",
        "created_at",
    )
    list_display_links = (
        "id",
        # "body",
    )

    search_fields = (
        # "post__title",
        # "author__username",
    )
    list_filter = (
        PostFilter,
        AuthorFilter,
    )
    raw_id_fields = (
        "author",
    )


@admin.register(Reaction)
class ReactionModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "post",
        "value",
    )
    list_filter = (
        PostFilter,
        AuthorFilter,
        ("value", ChoiceDropdownFilter),
    )


# admin.site.register(User)
admin.site.unregister(Group)
