

# PJT05 - Pair Project

### team & role

- 이은성 
  -  views.py: `index` , `create` 
  -  html : `index`, `create`
- 송상빈 
  - 기본 구조 구축(model, form, base.html, urls) 
  - views.py : `detail` , `create` , `delete`
  - html : `detail`, `update`



## Project 진행과정

* 은성
  * 주로 네비게이터 역할을 진행했다.
  * 중간에 역할을 분담하고 상빈님과 역할을 바꿔 views.py와 html을 작성했다.
* 상빈
  * 주로 드라이버 역할 진행.
  * 서로 의견을 주고받으며 기본 구조 구축 후 분담하여 프로젝트를 진행했다.



### 기본 구조 구축

#### models.py

```python
from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

#### forms.py

```python
from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    
    class Meta:
        model = Movies
        fields = '__all__'
```

#### movies/urls.py

```python
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
]
```

#### pjt05/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
]
```

#### base.html(네비게이션 바 포함)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
  <title>Document</title>
</head>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="{% url 'movies:index' %}">Home</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="{% url 'movies:create' %}">Create</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
<body>
  <div class="container">
    {% block base %}
    {% endblock base %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
</body>
</html>
```

<hr>



### views.py 작성

##### (은성)

```python
@require_safe
def index(request):
    movies = Movies.objects.order_by('-pk')
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()   
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)
```

##### (상빈)

```python
@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movies,pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, movie_pk):
    movie = get_object_or_404(Movies,pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form
    }
    return render(request, 'movies/update.html', context)


@require_POST
def delete(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    movie.delete()
    return redirect('movies:index')
```



### html 작성

##### detail.html (상빈)

![image-20210910200200498](README.assets/image-20210910200200498.png)

```html
{% extends 'base.html' %}

{% block base %}
  <h1>{{ movie.title }}</h1>
  <hr>
  <p>줄거리 : {{ movie.overview }}</p>
  <hr>
  <img src="{{ movie.poster_path }}" alt=""><br>
  <hr>
  <form action="{% url 'movies:update' movie.pk %}"><button>수정</button></form>
  
  <form action="{% url 'movies:delete' movie.pk %}" method="POST">
    {% csrf_token %}
    <button>[DELETE]</button>
  </form>
  <hr>
  <form action="{% url 'movies:index' %}"><button>BACK</button></form>
{% endblock base %}
```

##### update.html (상빈)

![image-20210910200214329](README.assets/image-20210910200214329.png)

```html
{% extends 'base.html' %}

{% block base %}
  <form action="{% url 'movies:update' movie.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>수정</button>
  </form>
  <a href="{% url 'movies:detail' movie.pk %}">[BACK]</a>
{% endblock base %}
```

##### index.html (은성)

![image-20210910200056618](README.assets/image-20210910200056618.png)

```html
{% extends 'base.html' %}

{% block base %}
  <h1>전체 영화 목록</h1>
  <a href="{% url 'movies:create' %}">[CREATE]</a>
  <ol>
    {% for movie in movies %}
      <li>
        <a href="{% url 'movies:detail' movie.pk %}">제목: {{ movie.title }}</a>
      </li>
    {% endfor %}
  </ol>
  
{% endblock base %}
```

##### create.html (은성)

![image-20210910200111738](README.assets/image-20210910200111738.png)

```html
{% extends 'base.html' %}

{% block base %}
  <h1>create</h1>
  <form action="{% url 'movies:create' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="작성">
  </form>
  <a href="{% url 'movies:index' %}">[BACK]</a>
{% endblock base %}
```



## Pair Project 소감 - 은성

프로젝트를 수시로 git을 통해 공유하고 **역할을 분담해서** 페어 프로젝트를 진행했다.

이번 관통 프로젝트의 목표는 기존에 공부했던 자료를 보지 않고 **협업을 통해** 한 명은 코드를 작성(드라이버)하고 

다른 한명은 코드작성을 도와주고 에러 해결에 도움을 줍니다(네비게이터).

---

pair project의 장점은

- `error` 을 서로 공유하고 빠르게 찾아볼 수 있다
- 서로 잘 아는 부분을 공유함으로써 공부에 도움이 되었다
- git을 통해 버전을 관리하면서 서로의 `local`로의 파일이동이 빠르고 편했다. 



아쉬운 점은

- 처음 pair project를 진행해서 더 좋은 코드를 찾기보다 기존의 코드를 공부하는 방향으로 진행되었다.



서로 같이 배우는 싸피 동료, 친구로서 다양한 페어프로젝트를 통해 서로의 실력을 쌓아나갈 수 있는 기회를 더욱 가지고 싶다.



## Pair Project 소감 - 상빈

프로젝트를 `git`을 통해 주고받으며 `git`이 협업시 굉장히 편리하다는 것을 체감할 수 있었다.

두명이서 같은 화면을 보며 코드를 작성하니 틀린 부분이나 오탈자를 바로바로 수정할 수 있었고, 에러가 발생했을 때도 빠르게 문제를 찾아낼 수 있었다.

알아놓기만 하고 실제로 활용하지 못하던 몇몇 `django` 요소들을 팀원의 도움덕에 활용할 수 있게 되었다.

어렴풋이 알았던 내용은 팀원에게 설명하며 확실히 정리할 수 있었고, 잘 몰랐던 내용은 팀원 덕에 알 수 있었다.