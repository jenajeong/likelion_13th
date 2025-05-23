from django.contrib import admin

from .models import MigrationTestModel

# 방법 1
# 간단하게 모델을 등록하는 방법
admin.site.register(MigrationTestModel)


# 방법 2
# 모델을 커스터마이징하여 등록하는 방법

# @admin.register(MigrationTestModel)
# class MigrationTestModelAdmin(admin.ModelAdmin):
#     # 페이지당 항목 수
#     list_per_page = 10
#     # 필드 목록
#     list_display = (
#         'id',
#         'name',
#         'is_happy',
#         'email',
#         'created_at',
#         'updated_at',
#     )
#     # 검색 필드
#     search_fields = (
#         'name',
#         'email',
#     )
#     # 필터링
#     list_filter = (
#         'is_happy',
#         'created_at',
#     )
#     # 정렬
#     ordering = (
#         'id',
#         'name',
#     )
