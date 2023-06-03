from django.urls import include, path

urlpatterns = [
    path("auth/", include(("styleguide_example.authentication.urls", "authentication"))),
    path("users/", include(("styleguide_example.users.urls", "users"))),
    path("files/", include(("styleguide_example.files.urls", "files"))),
]
