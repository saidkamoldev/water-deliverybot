import csv
from django.http import HttpResponse

from .models import User,  Offer

def export_users_csv(request):
    response = HttpResponse(content_type="text/csv")

    writer = csv.writer(response)
    writer.writerow([
    "id",
    "telegram_id",
    "name",
    "username",
    "location",
    "status",
    "phonenumber",
    "language"
    # "namecommand"
    ])
    for user in User.objects.all().values_list("id",
                                               "telegram_id",
                                               "name",
                                               "username",
                                               "location",
                                               "status",
                                               "phonenumber",
                                               "language"
                                               ):
        writer.writerow(user)

    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    return response

    response = HttpResponse(content_type="text/csv")

    writer = csv.writer(response)
    writer.writerow([
    "id",
    "category",
    "name",
    "inline_text",
    "inline_textUz",
    "status",
    "price",
    "photo",
    "creator"
    # "namecommand"
    ])
    for items in Item.objects.all().values_list("id",
                                               "category",
                                               "name",
                                               "inline_text",
                                               "inline_textUz",
                                               "status",
                                               "price",
                                               "photo",
                                               "creator"
                                               ):
        writer.writerow(items)

    response['Content-Disposition'] = 'attachment; filename="item.csv"'
    return response

def export_offer_csv(request):
    response = HttpResponse(content_type="text/csv")

    writer = csv.writer(response)
    writer.writerow([
    "id",
    "date",
    "telegram_id",
    "username",
    "status",
    "category",
    "quantity",
    "product",
    "price",
    "commentary"
    # "namecommand"
    ])
    for offer in Offer.objects.all().values_list(
                                                "id",
    "date",
    "telegram_id",
    "username",
    "status",
    "category",
    "quantity",
    "product",
    "price",
    "commentary"
                                               ):
        writer.writerow(offer)

    response['Content-Disposition'] = 'attachment; filename="offer.csv"'
    return response
