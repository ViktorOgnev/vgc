# -*- coding: utf-8 -*-
 
import re
from PIL import Image
from os.path import join, split
from django.db.models import ImageField
from vgc.settings import  IMG_UPLD_DIR
             
# utility functions that can possibly be common for several models
              

              
def get_image_path(instance, filename):
    instance_subdir = space_to_underscore(transliterate(instance.title[0:20]))
    return join(IMG_UPLD_DIR, instance_subdir, filename)    

def space_to_underscore(string):
    result = string.replace(' ', '_').replace('%20','_').replace('%22', '_')
    
    return result
        
def produce_resized_image(photo, size, instance_title, filename_prefix=''):

    pw = photo.width
    ph = photo.height
    nw = size[0]
    nh = size[1]
    
    # only do this if the image needs resizing
    if (pw, ph) != (nw, nh) and (filename_prefix != ''):
        filename = str(photo.path)
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
        
        
        # Save the resulting image, give it a new name by inserting a new prefix
        # and keeping in minf that our filename is infact an abs path
        folder_path, old_name = split(filename)
        newname = join(folder_path, filename_prefix + old_name)
        image.save(newname, "JPEG")
        
        # Produce the resulting path
        
        image_path = join(IMG_UPLD_DIR, instance_title, filename_prefix + old_name)
        
        # Finally, generate an Image field, so that the new images' name & path
        # could be stored in the db
        
        return ImageField(upload_to=image_path, blank=True, null=True)
        
        
        
    # If we're saving to the same filename and there are no changes to perform,
    # then we just return our input
    return photo
 
def transliterate(string):
 
    capital_letters = {u'А': u'A',
                       u'Б': u'B',
                       u'В': u'V',
                       u'Г': u'G',
                       u'Д': u'D',
                       u'Е': u'E',
                       u'Ё': u'E',
                       u'З': u'Z',
                       u'И': u'I',
                       u'Й': u'Y',
                       u'К': u'K',
                       u'Л': u'L',
                       u'М': u'M',
                       u'Н': u'N',
                       u'О': u'O',
                       u'П': u'P',
                       u'Р': u'R',
                       u'С': u'S',
                       u'Т': u'T',
                       u'У': u'U',
                       u'Ф': u'F',
                       u'Х': u'H',
                       u'Ъ': u'',
                       u'Ы': u'Y',
                       u'Ь': u'',
                       u'Э': u'E',}
 
    capital_letters_transliterated_to_multiple_letters = {u'Ж': u'Zh',
                                                          u'Ц': u'Ts',
                                                          u'Ч': u'Ch',
                                                          u'Ш': u'Sh',
                                                          u'Щ': u'Sch',
                                                          u'Ю': u'Yu',
                                                          u'Я': u'Ya',}
 
 
    lower_case_letters = { u'а': u'a',
                           u'б': u'b',
                           u'в': u'v',
                           u'г': u'g',
                           u'д': u'd',
                           u'е': u'e',
                           u'ё': u'e',
                           u'ж': u'zh',
                           u'з': u'z',
                           u'и': u'i',
                           u'й': u'y',
                           u'к': u'k',
                           u'л': u'l',
                           u'м': u'm',
                           u'н': u'n',
                           u'о': u'o',
                           u'п': u'p',
                           u'р': u'r',
                           u'с': u's',
                           u'т': u't',
                           u'у': u'u',
                           u'ф': u'f',
                           u'х': u'h',
                           u'ц': u'ts',
                           u'ч': u'ch',
                           u'ш': u'sh',
                           u'щ': u'sch',
                           u'ъ': u'',
                           u'ы': u'y',
                           u'ь': u'',
                           u'э': u'e',
                           u'ю': u'yu',
                           u'я': u'ya',}
 
    capital_and_lower_case_letter_pairs = {}
 
    for capital_letter, capital_letter_translit in \
        capital_letters_transliterated_to_multiple_letters.iteritems():
        
        for lowercase_letter, lowercase_letter_translit in lower_case_letters.iteritems():
            capital_and_lower_case_letter_pairs[u"%s%s" % (capital_letter,
                                                lowercase_letter)] = \
                u"%s%s" % (capital_letter_translit, lowercase_letter_translit)
 
    for dictionary in (capital_and_lower_case_letter_pairs,
                       capital_letters, lower_case_letters):
 
        for cyrillic_string, latin_string in dictionary.iteritems():
            string = re.sub(cyrillic_string, latin_string, string)
 
    for cyrillic_string, latin_string in \
        capital_letters_transliterated_to_multiple_letters.iteritems():
        string = re.sub(cyrillic_string, latin_string.upper(), string)
 
    return string