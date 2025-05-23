from django.db import models

class MigrationTestModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    # TODO: 아래 내용을 주석 해제하고 마이그레이션을 수행해봅시다.
    # is_happy = models.BooleanField(default=False)
    # email = models.EmailField(max_length=254, null=True, blank=True)
