from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import UserForm,ItemForm,AdvertiseForm,RequirementForm
from .models import Item,Advertisement

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'buy_portal/login.html')
    else:
        recent_objects = Item.objects.order_by('-datetime')[:6]
        book_objects = Item.objects.filter(category='Book')[:6]
        instruments_objects = Item.objects.filter(category='Instrument')[:6]
        projects_objects = Item.objects.filter(category='Project')[:6]
        other_objects = Item.objects.filter(category='Other')[:6]
        adv_objects=Advertisement.objects.order_by('-datetime')[:3]
        adv1=adv_objects[0]
        adv2 = adv_objects[1]
        adv3 = adv_objects[2]
        context = {
            'recent_objects': recent_objects,
            'book_objects':book_objects,
            'instruments_objects':instruments_objects,
            'projects_objects':projects_objects,
            'other_objects':other_objects,
            'adv1':adv1,
            'adv2': adv2,
            'adv3': adv3,
        }
        return render(request, 'buy_portal/Home.html',context)

def item_detail(request,item_id):
    if not request.user.is_authenticated():
        return render(request, 'buy_portal/login.html')
    else:
        item=Item.objects.get(pk=item_id)
        context={
            'item':item,
        }
        return render(request, 'buy_portal/item_detail.html', context)

def adv_detail(request,adv_id):
    if not request.user.is_authenticated():
        return render(request, 'buy_portal/login.html')
    else:
        adv=Advertisement.objects.get(pk=adv_id)
        context={
            'adv':adv,
        }
        return render(request, 'buy_portal/adv_detail.html', context)


def sell(request):
    if not request.user.is_authenticated():
        return render(request, 'buy_portal/login.html')
    else:
        form = ItemForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            item = form.save(commit=False)
            item.user=request.user
            item.image = request.FILES['image']
            file_type = item.image.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'buy_portal/sell.html', context)

            mrp_price = request.POST['mrp_price']
            selling_price = request.POST['selling_price']
            item_name = request.POST['item_name']
            char=str(item_name)[0]
            print type(char)
            if int(mrp_price)<int(selling_price) :
                if char<'A'or 'Z' < char < 'a' or char> 'z':
                    context = {
                        'form': form,
                        'error_message': 'Selling price should be less than MRP And  Item name should start with character!',
                    }
                    return render(request, 'buy_portal/sell.html', context)

                context = {
                    'form': form,
                    'error_message': 'Selling price should be less than MRP!',
                }
                return render(request, 'buy_portal/sell.html', context)
            elif char<'a'or char>'z' and char<'A'or char>'Z':
                    context = {
                        'form': form,
                        'error_message': 'Item name should start with character!',
                    }
                    return render(request, 'buy_portal/sell.html', context)


            item.save()
            return render(request, 'buy_portal/success.html')
        context={
            'form':form,
        }
        return render(request, 'buy_portal/sell.html',context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'buy_portal/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('buy_portal:index')  # redirect() accepts a view name as parameter
            else:
                return render(request, 'buy_portal/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'buy_portal/login.html', {'error_message': 'Invalid login'})
    return render(request, 'buy_portal/login.html')


def create_new_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('buy_portal:index')
    context = {
             "form": form,
    }
    return render(request, 'buy_portal/create_new_user.html', context)

def advertise(request):
    if not request.user.is_authenticated():
        return render(request, 'buy_portal/login.html')
    else:
        form = AdvertiseForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            adv = form.save(commit=False)
            adv.user=request.user
            adv.image = request.FILES['image']
            file_type = adv.image.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'music/advertise.html', context)
            adv.save()
            return render(request, 'buy_portal/success.html')
        context={
            'form':form,
        }
        return render(request, 'buy_portal/advertise.html',context)

def requirement(request):
    if not request.user.is_authenticated():
        return render(request, 'buy_portal/login.html')
    else:
        form = RequirementForm(request.POST or None)
        if form.is_valid():
            req = form.save(commit=False)
            req.user=request.user
            req.save()
            return render(request, 'buy_portal/success.html')
        context={
            'form':form,
        }
        return render(request, 'buy_portal/requirement.html',context)

def my_activity(request):
    if not request.user.is_authenticated():
        return render(request, 'buy_portal/login.html')
    else:
        my_sells=Item.objects.filter(user=request.user)
        context = {
            'my_sells': my_sells,
        }
        return render(request, 'buy_portal/my_activity.html', context)
