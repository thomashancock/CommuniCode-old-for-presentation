import gitlab
from django.conf import settings

git = gitlab.Gitlab(settings.SECRET_GITLAB_HOST, token=settings.SECRET_GITLAB_TOKEN)
