from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import News
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from .forms import NewsForm


class NewsListView(ListView):
    """
   @see https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/
   """
    model = News
    paginate_by = 2
    template_name = 'news/news.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-date')


class AuthorBookList(ListView):
    model = News
    template_name = "news/author_book.html"

    def get_queryset(self):
        self.author_name = get_object_or_404(User, username=self.kwargs['author_name'])
        # @see https://djangotricks.blogspot.com/2018/05/queryset-filters-on-many-to-many-relations.html
        return News.objects.filter(user__username=self.author_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author_name
        return context


def ex(request):
    news = News.objects.order_by('-date')[:2]
    context = {
        'news': news
    }

    return render(request, 'news/ex.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = "Ошибка валидации"
    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
