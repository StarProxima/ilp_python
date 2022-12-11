from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Brend, Chief, Guard, Post
from .models import Stock
from .models import Product


def glavn(request):
    return render(request, "glavnaya.html")

# получение данных из бд


def index(request):
    brend = Brend.objects.all()
    return render(request, "index.html", {"brend": brend})


def index2(request):
    stock = Stock.objects.all()
    return render(request, "index2.html", {"stock": stock})


def index3(request):
    prod = Product.objects.all()
    return render(request, "index3.html", {"prod": prod})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        brend = Brend()
        brend.name_brend = request.POST.get("name_brend")
        brend.country = request.POST.get("country")
        brend.save()
    return HttpResponseRedirect("/")


def create2(request):
    if request.method == "POST":
        stock = Stock()
        stock.name_stock = request.POST.get("name_stock")
        stock.start_stock = request.POST.get("start_stock")
        stock.finish_stock = request.POST.get("finish_stock")
        stock.persent_stock = request.POST.get("persent_stock")
        stock.save()
    return HttpResponseRedirect("/")


def create3(request):
    # если запрос POST, сохраняем данные
    brend = Brend.objects.all()
    stock = Stock.objects.all()
    if request.method == "POST":
        product = Product()
        product.name_product = request.POST.get("name_product")
        product.catagory = request.POST.get("catagory")
        product.type = request.POST.get("type")
        product.brend_id = request.POST.get("brend")
        product.stock_id = request.POST.get("stock")
        product.save()
        product
        return HttpResponseRedirect("/")
    # передаем данные в шаблон

    return render(request, "create.html", {"brend": brend, "stock": stock})


def chiefs(request):
    items = Chief.objects.all()
    return render(request, "chiefs.html", {"items": items})


def add_chief(request):
    if request.method == "POST":
        item = Chief()
        item.fio = request.POST.get("fio")
        item.work_experience = request.POST.get("work_experience")
        item.save()
        return HttpResponseRedirect("/chiefs")
    return render(request, "chief.html")


def edit_chief(request, id):
    item = Chief.objects.get(ChiefID=id)
    if request.method == "POST":
        item.fio = request.POST.get("fio")
        item.work_experience = request.POST.get("work_experience")
        item.save()
        return HttpResponseRedirect("/chiefs")
    return render(request, "chief.html", {"item": item})


def delete_chief(request, id):
    item = Chief.objects.get(ChiefID=id)
    item.delete()
    return HttpResponseRedirect("/chiefs")


def posts(request):
    items = Post.objects.all()
    return render(request, "posts.html", {"items": items})


def add_post(request):
    if request.method == "POST":
        item = Post()
        item.name = request.POST.get("name")
        item.location = request.POST.get("location")
        item.save()
        return HttpResponseRedirect("/posts")
    return render(request, "post.html")


def edit_post(request, id):
    item = Post.objects.get(PostID=id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.location = request.POST.get("location")
        item.save()
        return HttpResponseRedirect("/posts")
    return render(request, "post.html", {"item": item})


def delete_post(request, id):
    item = Post.objects.get(PostID=id)
    item.delete()
    return HttpResponseRedirect("/posts")


def guards(request):
    items = Guard.objects.all()
    return render(request, "guards.html", {"items": items})


def add_guard(request):
    if request.method == "POST":
        item = Guard()

        item.fio = request.POST.get("fio")
        item.work_experience = request.POST.get("work_experience")
        item.chief = Chief.objects.get(id=request.POST.get("chief_id"))
        item.save()
        return HttpResponseRedirect("/guards")
    return render(request, "guard.html", {"chiefs": Chief.objects.all()})


def edit_guard(request, id):
    item = Guard.objects.get(id=id)
    if request.method == "POST":
        item.chief = Chief.objects.get(id=request.POST.get("chief_id"))
        item.fio = request.POST.get("fio")
        item.work_experience = request.POST.get("work_experience")
        item.save()
        return HttpResponseRedirect("/guards")
    return render(request, "guard.html", {"item": item, "chiefs": Chief.objects.all()})


def delete_guard(request, id):
    item = Guard.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect("/guards")

# изменение данных в бд


def edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.name_product = request.POST.get("name_product")
            product.catagory = request.POST.get("catagory")
            product.type = request.POST.get("type")
            product.brend_id = request.POST.get("brend")
            product.stock_id = request.POST.get("stock")
            product.save()
            return HttpResponseRedirect("/")
        else:
            brend = Brend.objects.all()
            stock = Stock.objects.all()
            return render(request, "edit.html", {"brend": brend, "stock": stock, "product": product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def allinf(request, id):
    product = Product.objects.get(id=id)
    return render(request, "all_inf.html", {"product": product})
