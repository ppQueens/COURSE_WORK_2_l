# from ajax_select import register, LookupChannel
# from .models import ItemField, ItemFieldTitle
#
# @register('TitleFieldsLookup')
# class TitleFieldsLookup(LookupChannel):
#
#     model = ItemFieldTitle
#     def get_query(self, q, request):
#         return self.model.objects.filter(field_title__icontains=q)[:50]
#
#     def format_item_display(self, item):
#         return "<span class='tag'>{0}</span>".format("")