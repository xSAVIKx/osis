# coding=utf-8

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from envelope.views import ContactView

from web_site.forms import CustomContactForm
from web_site.models import Item, ItemImage


class GalleryView(TemplateView):
    template_name = 'web_site/gallery.html'

    def get_context_data(self, **kwargs):
        kwargs = super(GalleryView, self).get_context_data(**kwargs)
        kwargs['items_and_images'] = self.get_items_with_its_images()
        return kwargs

    @staticmethod
    def get_items_with_its_images():
        items = Item.objects.all()
        if len(items) is 0:
            return []
        item_with_images_list = []
        item_id = 1
        for item in items:
            item_images = ItemImage.objects.filter(item=item)
            item_with_images_list.append((item, item_id, item_images))
            item_id += len(item_images) + 1
        return sorted(item_with_images_list, key=lambda prjct: len(prjct[2]), reverse=True)


class ItemListView(ListView):
    model = Item
    items_in_row = 4

    def get_context_data(self, **kwargs):
        kwargs = super(ItemListView, self).get_context_data(**kwargs)
        kwargs['items_in_row'] = self.items_in_row
        kwargs['managed_items'] = self.manage_by_rows()
        return kwargs

    def manage_by_rows(self):
        managed_items = []
        item_block = []
        if len(self.object_list) < self.items_in_row:
            for item in self.object_list:
                item_block.append(item)
            managed_items.append(item_block)
        else:
            for index, item in enumerate(self.object_list):
                if index % self.items_in_row == 0 and index > 0:
                    managed_items.append(item_block)
                    item_block = []
                item_block.append(item)
        return managed_items


class ItemDetailedView(DetailView):
    model = Item
    pk_url_kwarg = 'item_id'


class AboutUsTemplateView(TemplateView):
    template_name = 'web_site/about_us.html'


class ContactUsView(ContactView):
    template_name = 'web_site/contact_us.html'
    success_url = 'index'
    form_class = CustomContactForm