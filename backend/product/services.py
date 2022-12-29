from PIL import Image
from io import BytesIO
from django.core.files import File


def get_product_thumbnail(product):
    if product.thumbnail:
        return 'http://127.0.0.1:8000' + product.thumbnail.url
    else:
        if product.image:
            product.thumbnail = make_product_thumbnail(product.image)
            product.save()
            return 'http://127.0.0.1:8000' + product.thumbnail.url
        else:
            return ''


def make_product_thumbnail(image, size=(300, 200)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=100)

    thumbnail = File(thumb_io, name='thumbnail_'+image.name)

    return thumbnail
