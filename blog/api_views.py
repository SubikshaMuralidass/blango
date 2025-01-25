"""from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Post
import json

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        # Retrieve all posts
        posts = Post.objects.all()
        data = [{"id": post.id, "title": post.title, "content": post.content, "slug": post.slug} for post in posts]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        # Create a new post
        data = json.loads(request.body)
        post = Post.objects.create(title=data['title'], content=data['content'], slug=data['slug'])
        return JsonResponse({"id": post.id, "title": post.title, "content": post.content, "slug": post.slug}, status=201)

@csrf_exempt
def post_detail(request, pk):
    # Retrieve, update, or delete a single post
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'GET':
        data = {"id": post.id, "title": post.title, "content": post.content, "slug": post.slug}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        post.title = data['title']
        post.content = data['content']
        post.slug = data['slug']
        post.save()
        return JsonResponse({"id": post.id, "title": post.title, "content": post.content, "slug": post.slug})
    
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({"message": "Post deleted successfully"}, status=204)
"""
import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post


def post_to_dict(post):
    return {
        "pk": post.pk,
        "author_id": post.author_id,
        "created_at": post.created_at,
        "modified_at": post.modified_at,
        "published_at": post.published_at,
        "title": post.title,
        "slug": post.slug,
        "summary": post.summary,
        "content": post.content,
    }


@csrf_exempt
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        posts_as_dict = [post_to_dict(p) for p in posts]
        return JsonResponse({"data": posts_as_dict})
    elif request.method == "POST":
        post_data = json.loads(request.body)
        post = Post.objects.create(**post_data)
        return HttpResponse(
            status=HTTPStatus.CREATED,
            headers={"Location": reverse("api_post_detail", args=(post.pk,))},
        )

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
        return JsonResponse(post_to_dict(post))
    elif request.method == "PUT":
        post_data = json.loads(request.body)
        for field, value in post_data.items():
            setattr(post, field, value)
        post.save()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])