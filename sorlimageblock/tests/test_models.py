from django.test import TestCase
from sorlimageblock.models import ImageBlock, ImagePullQuoteBlock
from sorlimageblock.tests.factories import (
    ImageBlockFactory, ImagePullQuoteBlockFactory
)


class ImageBlockTest(TestCase):
    def test_is_valid_from_factory(self):
        b = ImageBlockFactory()
        b.full_clean()

    def test_add_form(self):
        f = ImageBlock.add_form()
        self.assertTrue('image' in f.fields)
        self.assertTrue('caption' in f.fields)
        self.assertTrue('alt' in f.fields)
        self.assertTrue('lightbox' in f.fields)
        self.assertFalse(f.fields['caption'].required)
        self.assertFalse(f.fields['alt'].required)

    def test_create_from_dict(self):
        d = dict(image='foo/bar/blah.jpg')
        tb = ImageBlock.create_from_dict(d)
        self.assertEqual(tb.image, 'foo/bar/blah.jpg')
        self.assertEqual(tb.caption, '')

    def test_edit_form(self):
        tb = ImageBlock.create_from_dict(dict(image='foo/bar/blah.jpg'))
        f = tb.edit_form()
        self.assertTrue('caption' in f.fields)
        self.assertFalse(f.fields['caption'].required)
        self.assertFalse(f.fields['alt'].required)

    def test_edit(self):
        tb = ImageBlock.create_from_dict(dict(image='foo/bar/blah.jpg'))
        tb.edit(dict(image='foo/bar/blah.jpg', caption='bar'), [])
        self.assertEqual(tb.caption, 'bar')

    def test_as_dict(self):
        tb = ImageBlock.create_from_dict(dict(image='foo/bar/blah.jpg'))
        self.assertEqual(
            tb.as_dict(),
            dict(image='foo/bar/blah.jpg',
                 alt='', caption='', lightbox=False))

    def test_list_resources(self):
        tb = ImageBlock.create_from_dict(dict(image='foo/bar/blah.jpg'))
        self.assertEqual(tb.list_resources(), ['foo/bar/blah.jpg'])


class ImagePullQuoteBlockTest(TestCase):
    def test_is_valid_from_factory(self):
        b = ImagePullQuoteBlockFactory()
        b.full_clean()

    def test_add_form(self):
        f = ImagePullQuoteBlock.add_form()
        self.assertTrue('image' in f.fields)
        self.assertTrue('caption' in f.fields)
        self.assertTrue('alt' in f.fields)
        self.assertFalse(f.fields['caption'].required)
        self.assertFalse(f.fields['alt'].required)

    def test_create_from_dict(self):
        d = dict(image='foo/bar/blah.jpg')
        tb = ImagePullQuoteBlock.create_from_dict(d)
        self.assertEqual(tb.image, 'foo/bar/blah.jpg')
        self.assertEqual(tb.caption, '')

    def test_edit_form(self):
        tb = ImagePullQuoteBlock.create_from_dict(
            dict(image='foo/bar/blah.jpg'))
        f = tb.edit_form()
        self.assertTrue('caption' in f.fields)
        self.assertFalse(f.fields['caption'].required)
        self.assertFalse(f.fields['alt'].required)

    def test_edit(self):
        tb = ImagePullQuoteBlock.create_from_dict(
            dict(image='foo/bar/blah.jpg'))
        tb.edit(dict(image='foo/bar/blah.jpg', caption='bar'), [])
        self.assertEqual(tb.caption, 'bar')

    def test_as_dict(self):
        tb = ImagePullQuoteBlock.create_from_dict(
            dict(image='foo/bar/blah.jpg'))
        self.assertEqual(
            tb.as_dict(),
            dict(image='foo/bar/blah.jpg',
                 alt='', caption=''))

    def test_list_resources(self):
        tb = ImagePullQuoteBlock.create_from_dict(
            dict(image='foo/bar/blah.jpg'))
        self.assertEqual(tb.list_resources(), ['foo/bar/blah.jpg'])
