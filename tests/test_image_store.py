
from xychan.image_store import *

def test_store_and_read_image():
    image_data = open('tests/image.jpg').read()
    fn = store_image(image_data)
    assert fn
    assert fn.endswith('.jpeg')
    assert fetch_image(fn) == image_data
    assert fetch_thumb(fn)
