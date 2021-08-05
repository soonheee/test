from django.shortcuts import render, get_object_or_404
from .models import Review, User


def review_list(request):
    reviews = Review.objects.filter(tmp_flag=False)
    content = {'reviews': reviews}
    return render(request, 'reviewlist.html', content)


# @login_required(login_url='pass')
def review_detail(request):
    if request.method == 'GET':
        content = {'day_range': list(range(1, 31)) + [60, 90, 120]}
        return render(request, 'reviewcreate.html', content)
    else:
        Review(writer=User.objects.all()[0], title=request.POST.get("title"),
               tmp_flag=request.POST.get("tmp_flag"), d_day=request.POST.get("d_day"),
               review=request.POST.get("review")).save()
        reviews = Review.objects.filter(tmp_flag=False)
        content = {'reviews': reviews}
        return render(request, 'reviewlist.html', content)
