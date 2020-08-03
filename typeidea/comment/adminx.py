import xadmin

# Register your models here.
from typeidea.custom_site import custom_site
from .models import Comment


@xadmin.sites.register(Comment)
class CommentAdmin:
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')