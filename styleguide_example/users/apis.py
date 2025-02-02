from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import LimitOffsetPagination

from styleguide_example.users.models import BaseUser


class UserListApi(GenericAPIView, ListModelMixin):
    pagination_class = LimitOffsetPagination
    filterset_fields = ("id", "is_admin", "email")
    queryset = BaseUser.objects.all()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = BaseUser
            fields = ("id", "email", "is_admin")

    serializer_class = OutputSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
