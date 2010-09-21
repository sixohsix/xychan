
import os
try:
    from subprocess import check_output
except ImportError:
    from commands import getstatusoutput
    def check_output(cmdlist):
        cmd = ' '.join(cmdlist)
        status, output = getstatusoutput(cmd)
        if status:
            raise Exception("Command [%s] failed." % cmd)

from sha import sha

from .util import num_encode


def configure_image_dir(d):
    global IMAGE_DIR, THUMBS_DIR
    IMAGE_DIR = d
    THUMBS_DIR = d + os.sep + "thumbs"
configure_image_dir("_images")


def _im_identify_type(fn):
    out = check_output(["identify", "-format", "%m\n", fn]).split('\n')[0]
    return out.strip().lower()


def _im_make_thumb(fn):
    typ = fn[fn.rindex('.') + 1:]
    if typ in ('jpg', 'jpeg'):
        check_output(["convert", fn, "-resize", "150x150", "-quality", "60",
                      THUMBS_DIR + fn[fn.rindex(os.sep):fn.rindex('.')]
                      + '.jpeg'])
    elif typ in ('gif',):
        check_output(["convert", fn + r"[0]", "-resize", "150x150",
                      THUMBS_DIR + fn[fn.rindex(os.sep):fn.rindex('.')]
                      + '.gif'])
    elif typ in ('png',):
        check_output(["convert", fn, "-resize", "150x150",
                      THUMBS_DIR + fn[fn.rindex(os.sep):fn.rindex('.')]
                      + '.png'])
    else:
        raise Exception("Unknown image type")


def store_image(image_data):
    sig = sha()
    sig.update(image_data)
    key = num_encode(int(sig.hexdigest(), 16))
    fn = IMAGE_DIR + os.sep + key
    open(fn, 'w').write(image_data)
    typ = _im_identify_type(fn)
    real_fn = fn + '.' + typ
    check_output(["mv", fn, real_fn])
    _im_make_thumb(real_fn)
    return key + '.' + typ


def fetch_image(fn):
    if fn.count(os.sep):
        raise Exception("Uh no")
    return open(IMAGE_DIR + os.sep + fn).read()


def fetch_thumb(fn):
    if fn.count(os.sep):
        raise Exception("Uh no")
    return open(THUMBS_DIR + os.sep + fn).read()


__all__ = ['fetch_image', 'fetch_thumb', 'store_image']
