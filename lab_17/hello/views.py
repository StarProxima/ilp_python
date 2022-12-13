from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Brend, Chief, Guard, OnDuty, Post
from .models import Stock
from .models import Product


def main(request):
    return render(request, "main.html")


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
    item = Chief.objects.get(id=id)
    if request.method == "POST":
        item.fio = request.POST.get("fio")
        item.work_experience = request.POST.get("work_experience")
        item.save()
        return HttpResponseRedirect("/chiefs")
    return render(request, "chief.html", {"item": item})


def delete_chief(request, id):
    item = Chief.objects.get(id=id)
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
    item = Post.objects.get(id=id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.location = request.POST.get("location")
        item.save()
        return HttpResponseRedirect("/posts")
    return render(request, "post.html", {"item": item})


def delete_post(request, id):
    item = Post.objects.get(id=id)
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


def on_duties(request):
    items = OnDuty.objects.all()
    return render(request, "on_duties.html", {"items": items})


def add_on_duty(request):
    if request.method == "POST":
        item = OnDuty()
        item.guard = Guard.objects.get(id=request.POST.get("guard_id"))
        item.post = Post.objects.get(id=request.POST.get("post_id"))
        item.chief = Chief.objects.get(id=request.POST.get("chief_id"))
        item.exit_time = request.POST.get("exit_time")
        item.save()
        return HttpResponseRedirect("/on_duties")
    return render(request, "on_duty.html", {"guards": Guard.objects.all(), "posts": Post.objects.all(), "chiefs": Chief.objects.all()})


def edit_on_duty(request, id):
    item = OnDuty.objects.get(id=id)
    if request.method == "POST":
        item.guard = Guard.objects.get(id=request.POST.get("guard_id"))
        item.post = Post.objects.get(id=request.POST.get("post_id"))
        item.chief = Chief.objects.get(id=request.POST.get("chief_id"))
        item.exit_time = request.POST.get("exit_time")
        item.save()
        return HttpResponseRedirect("/on_duties")
    return render(request, "on_duty.html", {"item": item, "guards": Guard.objects.all(), "posts": Post.objects.all(), "chiefs": Chief.objects.all()})


def delete_on_duty(request, id):
    item = OnDuty.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect("/on_duties")
