# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django.template import RequestContext
from django.http import HttpResponse
from mydjapp.models import Category, Post
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from forms import AddCategoryForm, AddLotProductsForm
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse_lazy
from django.db.models import F
from utils import generic_search

@login_required(login_url='/login/')
def index(request):
	context = {
		'cats' : Category.objects.all(),
        'articlesallmain' : Post.objects.all().order_by('title'),
        'allgoodieslen' : len(Post.objects.all())
	}
	return render_to_response('base.html', context, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def category(request, category_id):
    latest_news_category_list = Post.objects.filter(category=category_id).order_by('title')
    context = {
        'latest_news_category_list': latest_news_category_list,
        'cats' : Category.objects.all(),
        'category': get_object_or_404(Category, id=category_id)}
    return render_to_response('category.html', context, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required('mydjapp.add_category')
def cat_new(request):
    if request.method == 'GET':
        form = AddCategoryForm()
    else:
        form = AddCategoryForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            cat = Category.objects.create(title=title)
            return render_to_response('base.html', {'cats' : Category.objects.all()}, context_instance=RequestContext(request))

    return render_to_response('new_category.html', {'form' : form, 'cats' : Category.objects.all()}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required('mydj.add_post')
def lot_news(request):
    if request.method == 'GET':
        formm = AddLotProductsForm()
    else:
        formm = AddLotProductsForm(request.POST)

        if formm.is_valid():
            alltxt = formm.cleaned_data
            tt = alltxt.get('txt')
            mm = tt.strip().split('\n')
            for i in mm:
                f, s, t = i.split('|')
                f, s, t = f.strip(), s.strip(), t.strip()
                postt = Post.objects.create(title=f, category=Category(id=s), stock=t)
            return render_to_response('base.html', {'cats' : Category.objects.all()}, context_instance=RequestContext(request))

    return render_to_response('lot_news.html', {'formm' : formm, 'cats' : Category.objects.all()}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required("mydjapp.delete_category")
def cat_del(request, category_id):
	catt = Category.objects.get(id=category_id)
	context = {
		'caat' : catt,
        'cats' : Category.objects.all()
	}
	return render_to_response('confirm.html', context, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required("mydjapp.delete_category")
def cat_del_confirm(request, category_id):
    if request.method == 'GET':
        Category.objects.get(id=category_id).delete()
        return redirect('index')
    return render_to_response('confirm.html', {'cats' : Category.objects.all()}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def post_sell(request, post_id):
	posttt = Post.objects.get(id=post_id)
	context = {
		'poost' : posttt,
        'cats' : Category.objects.all()
	}
	return render_to_response('confirmPost.html', context, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def post_sell_confirm(request, post_id):
    if request.method == 'GET':
        stcount = Post.objects.filter(id=post_id).update(stock=F('stock') - 1)
        return redirect('index')
    return render_to_response('confirmPost.html', {'cats' : Category.objects.all()}, context_instance=RequestContext(request))

def error404(request):
    return render_to_response('404.html', status=404)

QUERY="q"

MODEL_MAP = { Post: ["title",], }

@login_required(login_url='/login/')
def search(request):

   objects = []

   for model,fields in MODEL_MAP.iteritems():
       objects += generic_search(request,model,fields,QUERY)

   return render_to_response("search_results.html",
                             {"objects":objects,
                              "cats" : Category.objects.all(),
                              "search_string" : request.GET.get(QUERY,""),}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required("mydjapp.delete_post")
def post_delete(request, post_id):
	posttt = Post.objects.get(id=post_id)
	context = {
		'poostd' : posttt,
        'cats' : Category.objects.all()
	}
	return render_to_response('confirmPostDel.html', context, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required("mydjapp.delete_post")
def post_delete_confirm(request, post_id):
    if request.method == 'GET':
        stcount = Post.objects.filter(id=post_id).delete()
        return redirect('index')
    return render_to_response('confirmPost.html', {'cats' : Category.objects.all()}, context_instance=RequestContext(request))