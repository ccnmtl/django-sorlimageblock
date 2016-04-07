from django.db import models
from django.conf import settings
from sorl.thumbnail.fields import ImageWithThumbnailsField
from django import forms
import os
from django.template.defaultfilters import slugify
from datetime import datetime
from pagetree.generic.models import BasePageBlock


class ImageBlock(BasePageBlock):
    """
    ImageBlock allows the user to upload an image to
    the block, and includes automatic thumbnailing.
    """
    image = ImageWithThumbnailsField(
        upload_to="images/%Y/%m/%d",
        thumbnail={
            'size': (65, 65)
        },
        extra_thumbnails={
            'admin': {
                'size': (70, 50),
                'options': ('sharpen',),
            }
        })
    caption = models.TextField(blank=True)
    alt = models.CharField(max_length=100, null=True, blank=True)
    lightbox = models.BooleanField(default=False)
    template_file = "pageblocks/imageblock.html"
    display_name = "Image Block"
    summary_template_file = "pageblocks/imageblock_summary.html"

    def edit_form(self):
        class EditForm(forms.Form):
            image = forms.FileField(label="replace image")
            caption = forms.CharField(
                initial=self.caption,
                required=False,
                widget=forms.widgets.Textarea(),
            )
            alt = forms.CharField(
                initial=self.alt,
                required=False,
            )
            lightbox = forms.BooleanField(initial=self.lightbox)
        return EditForm()

    @staticmethod
    def add_form():
        class AddForm(forms.Form):
            image = forms.FileField(label="select image")
            caption = forms.CharField(widget=forms.widgets.Textarea(),
                                      required=False)
            alt = forms.CharField(required=False)
            lightbox = forms.BooleanField()
        return AddForm()

    @classmethod
    def create(cls, request):
        if 'image' in request.FILES:
            ib = cls.objects.create(
                alt=request.POST.get('alt', ''),
                caption=request.POST.get('caption', ''),
                lightbox=request.POST.get('lightbox', False),
                image="")
            ib.save_image(request.FILES['image'])
            return ib
        return None

    @classmethod
    def create_from_dict(cls, d):
        # since it's coming from a dict, not a request
        # we assume that some other part is handling the writing of
        # the image file to disk and we just get a path to it
        return cls.objects.create(
            image=d.get('image', ''),
            alt=d.get('alt', ''),
            lightbox=d.get('lightbox', False),
            caption=d.get('caption', ''))

    def edit(self, vals, files):
        self.caption = vals.get('caption', '')
        self.alt = vals.get('alt', '')
        self.lightbox = vals.get('lightbox', False)
        if 'image' in files:
            self.save_image(files['image'])
        self.save()

    def save_image(self, f):
        ext = f.name.split(".")[-1].lower()
        basename = slugify(f.name.split(".")[-2].lower())[:20]
        if ext not in ['jpg', 'jpeg', 'gif', 'png']:
            # unsupported image format
            return None
        now = datetime.now()
        path = "images/%04d/%02d/%02d/" % (now.year, now.month, now.day)
        full_filename = path + "%s.%s" % (basename, ext)

        try:
            os.makedirs(settings.MEDIA_ROOT + "/" + path)
            fd = self.image.storage.open(
                settings.MEDIA_ROOT + "/" + full_filename, 'wb')
        except:
            fd = self.image.storage.open(full_filename, 'wb')

        for chunk in f.chunks():
            fd.write(chunk)
        fd.close()
        self.image = full_filename
        self.save()

    def as_dict(self):
        return dict(image=self.image.name,
                    alt=self.alt,
                    lightbox=self.lightbox,
                    caption=self.caption)

    def list_resources(self):
        return [self.image.url]


class ImagePullQuoteBlock(BasePageBlock):
    image = ImageWithThumbnailsField(
        upload_to="images/%Y/%m/%d",
        thumbnail={
            'size': (65, 65)
        },
        extra_thumbnails={
            'admin': {
                'size': (70, 50),
                'options': ('sharpen', ),
            }
        })
    caption = models.TextField(blank=True)
    alt = models.CharField(max_length=100, null=True, blank=True)

    template_file = "pageblocks/imagepullquoteblock.html"
    summary_template_file = "pageblocks/imagepullquoteblock_summary.html"
    display_name = "Image Pullquote"

    def edit_form(self):
        class EditForm(forms.Form):
            image = forms.FileField(label="replace image")
            caption = forms.CharField(initial=self.caption,
                                      required=False,
                                      widget=forms.widgets.Textarea())
            alt = forms.CharField(initial=self.alt, required=False)
        return EditForm()

    @classmethod
    def add_form(cls):
        class AddForm(forms.Form):
            image = forms.FileField(label="select image")
            caption = forms.CharField(widget=forms.widgets.Textarea(),
                                      required=False)
            alt = forms.CharField(required=False)
        return AddForm()

    @classmethod
    def create(cls, request):
        if 'image' in request.FILES:
            ib = cls.objects.create(
                caption=request.POST.get('caption', ''),
                image="",
                alt=request.POST.get('alt', ''))
            ib.save_image(request.FILES['image'])
            return ib
        else:
            return None

    @classmethod
    def create_from_dict(cls, d):
        # since it's coming from a dict, not a request
        # we assume that some other part is handling the writing of
        # the image file to disk and we just get a path to it
        return cls.objects.create(
            image=d.get('image', ''),
            alt=d.get('alt', ''),
            caption=d.get('caption', ''))

    def edit(self, vals, files):
        self.caption = vals.get('caption', '')
        self.alt = vals.get('alt', '')
        if 'image' in files:
            self.save_image(files['image'])
        self.save()

    def save_image(self, f):
        ext = f.name.split(".")[-1].lower()
        basename = slugify(f.name.split(".")[-2].lower())[:20]
        if ext not in ['jpg', 'jpeg', 'gif', 'png']:
            # unsupported image format
            return None
        now = datetime.now()
        path = "images/%04d/%02d/%02d/" % (now.year, now.month, now.day)
        try:
            os.makedirs(settings.MEDIA_ROOT + "/" + path)
        except:
            pass
        full_filename = path + "%s.%s" % (basename, ext)
        fd = open(settings.MEDIA_ROOT + "/" + full_filename, 'wb')
        for chunk in f.chunks():
            fd.write(chunk)
        fd.close()
        self.image = full_filename
        self.save()

    def as_dict(self):
        return dict(image=self.image.name,
                    alt=self.alt,
                    caption=self.caption)

    def list_resources(self):
        return [self.image.url]
