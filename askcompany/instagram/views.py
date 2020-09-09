from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import ListView
# Create your views here.

# def post_list(request):
#     qs = Post.objects.all() # 전체를 가져올 준비
#     q = request.GET.get('q', '') # q라는 이름의 인자가 있으면 가져오고(request에서 q라는 이름으로 데이터를 날리기 때문), 없으면 None
#     if q:
#         qs = qs.filter(message__icontains=q)
#         # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list' : qs,
#         'q' : q,
#     })

post_list = ListView.as_view(model=Post)
# CBV(클래스 기반 호출)로 구현


def post_detail(request : HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    # try:
    #     post = Post.objects.get(pk=pk) # 없으면 DoesNotExist 예외 발생
    #     # 앞 pk는 필드의 종류, 뒤 pk는 인자로 넘어온 값
    # except Post.DoesNotExist:
    #     raise Http404
    return render(request, 'instagram/post_detail.html',{
        'post' : post,
    })

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")