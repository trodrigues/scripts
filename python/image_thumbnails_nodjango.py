import os
try:
    from PIL import Image
except ImportError:
    import Image

def img_thumb(photo, alt_path=None, size=(200, 200)):
    """
        REQUIRES:
            1. 'from PIL import Image'
        
        DOES:
            1. check to see if the image needs to be resized
            2. check how to resize the image based on its aspect ratio
            3. resize the image accordingly
        
        ABOUT:
            based loosely on djangosnippet #688
            http://www.djangosnippets.org/snippets/688/
        
        VERSIONS I'M WORKING WITH:
            Django 1.0
            Python 2.5.1
        
        BY:
            Tanner Netterville
            tanner@cabedge.com
    """
    image = Image.open(photo)
    pw = image.size[0]
    ph = image.size[1]
    nw = size[0]
    nh = size[1]
    
    # only do this if the image needs resizing
    if (pw, ph) > (nw, nh):
        if alt_path is not None:
            filename = str(alt_path) + str(os.path.basename(photo.name))
        else:
            filename = str(photo)
        image = Image.open(filename)
        pr = float(pw) / float(ph)
        nr = float(nw) / float(nh)
        
        if pr > nr:
            # photo aspect is wider than destination ratio
            tw = int(round(nh * pr))
            image = image.resize((tw, nh), Image.ANTIALIAS)
            l = int(round(( tw - nw ) / 2.0))
            image = image.crop((l, 0, l + nw, nh))
        elif pr < nr:
            # photo aspect is taller than destination ratio
            th = int(round(nw / pr))
            image = image.resize((nw, th), Image.ANTIALIAS)
            t = int(round(( th - nh ) / 2.0))
            #print((0, t, nw, t + nh))
            image = image.crop((0, t, nw, t + nh))
        else:
            # photo aspect matches the destination ratio
            image = image.resize(size, Image.ANTIALIAS)
            
        image.save(filename)
