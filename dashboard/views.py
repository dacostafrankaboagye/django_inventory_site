from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

#crud
from .models import Product, Order

from  .forms import ProductForm, OrderForm

from django.contrib.auth.models import User

#adding flash messages
from django.contrib import messages



'''
# who ever is making the order, we need to assign a user to that particular order

if form.is_valid():
	form.save()
	return redirect('dashboard-index')
		'''


@login_required(login_url='user-login')
def index(request):
	#return HttpResponse('This is the index page')
	#return HttpResponse("<h1>This also works<h1>")

	orders = Order.objects.all()
	# representation- data
	products = Product.objects.all()

	workers_count = User.objects.all().count()
	items_count = Product.objects.all().count()
	orders_count = Order.objects.all().count()


	if request.method == 'POST':
		form = OrderForm(request.POST)

		if form.is_valid():
			instance = form.save(commit=False) # we need to pause and associate a user
			# if commit=False, then we have not saved it yet
			instance.staff  = request.user
			instance.save()
			return redirect('dashboard-index')
	else:
		form = OrderForm()
	context = {
		'orders': orders,
		'form': form,
		'products':products,
		'workers_count': workers_count,
		'items_count': items_count,
		'orders_count': orders_count,
	}

	# a better way of doing it 
	return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):

	workers = User.objects.all()
	workers_count = workers.count()
	items_count = Product.objects.all().count()
	orders_count = Order.objects.all().count()
	context = {
		'workers': workers,
		'workers_count': workers_count,
		'items_count': items_count,
		'orders_count': orders_count,
	}

	#return HttpResponse('This is the staff page')
	return render(request, 'dashboard/staff.html', context)




# we want to grab a particular staff and view his or her detail
# so we put in a primary key
@login_required(login_url='user-login')
def staff_detail(request, pk):
	workers = User.objects.get(id=pk)
	context = {
		'workers': workers,
	}
	return render(request, 'dashboard/staff_detail.html', context)





@login_required(login_url='user-login')
def product(request):

	#crud
	items = Product.objects.all() # using ORM
	#items = Product.objects.raw('SELECT * FROM dashboard_product') # allows us to write normal sql

	
	items_count = items.count()
	workers_count = User.objects.all().count()
	orders_count = Order.objects.all().count()


	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			#flash msg
			product_name = form.cleaned_data.get('name') #we are grabbing the name. You can check the other fields we specified in the forms.py
			messages.success(request, f'{product_name} has been added')
			return redirect('dashboard-product')

	else:
		form = ProductForm()

	context = {
		'items': items,
		'form': form,
		'workers_count': workers_count,
		'items_count': items_count,
		'orders_count': orders_count,

	}

	return render(request, 'dashboard/product.html', context)



'''
we are going to delete a particular thing,
so we pass in a primary key (pk)
'''
@login_required(login_url='user-login')
def product_delete(request, pk):
	item = Product.objects.get(id=pk)
	if request.method == 'POST':
		item.delete()
		return redirect('dashboard-product')
	return render(request, 'dashboard/product_delete.html')


@login_required(login_url='user-login')
def product_update(request, pk):
	item = Product.objects.get(id=pk)
	if request.method == 'POST':
		form = ProductForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('dashboard-product')
	else:
		form = ProductForm(instance=item)

	# instace = item )==> makes it populated

	context	= {
		'form': form,
	}

	return render(request, 'dashboard/product_update.html', context)


@login_required(login_url='user-login')
def order(request):
	orders = Order.objects.all()
	orders_count = orders.count()
	items_count = Product.objects.all().count()
	workers_count = User.objects.all().count()
	context = {
		'orders': orders,
		'orders_count': orders_count,
		'workers_count': workers_count,
		'items_count': items_count,


	}
	return render(request, 'dashboard/order.html', context)




'''
another way to enforce log in is:

@login_required
def index(request):
	return render(request, 'dashboard/index.html')

-> then go into settings.py
LOGIN_URL = 'user-login'

'''