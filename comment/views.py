from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from item.models import Item


# Create your views here.


@require_POST
def add_comment(request, item_slug):
    print(request.POST)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.item = get_object_or_404(Item, slug=item_slug)
        new_comment.save()

        return render(request, "comment.html", {"comment": new_comment})
    return render(request, "comment_form.html", {"errors": comment_form.errors})


def get_comments(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    comments = item.comments.filter(active=True)
    return render(request, "comments.html", {"comments": comments, "item_slug": item_slug})

