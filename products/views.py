from django.views.generic import ListView
from products.models import ProductModel, CategoryModel, ProductTagModel, BrandModel


class ProductsListView(ListView):
    template_name = 'shop.html'
    paginate_by = 3

    # filter
    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort')

        # search
        if q:
            qs = qs.filter(title__icontains=q)

        # category
        if cat:
            qs = qs.filter(category_id=cat)

        # brand
        if brand:
            qs = qs.filter(brand_id=brand)

        # tag
        if tag:
            qs = qs.filter(tags__id=tag)

        # sort
        if sort:
            if sort == 'price':
                qs = sorted(qs, key=lambda i: i.get_price())
            elif sort == '-price':
                qs = sorted(qs, key=lambda i: i.get_price(), reverse=True)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()

        return context
