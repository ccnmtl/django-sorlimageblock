import factory
from factory.fuzzy import FuzzyText

from sorlimageblock.models import ImageBlock, ImagePullQuoteBlock


class ImageBlockFactory(factory.DjangoModelFactory):
    class Meta:
        model = ImageBlock

    image = factory.django.ImageField()
    caption = FuzzyText()


class ImagePullQuoteBlockFactory(factory.DjangoModelFactory):
    class Meta:
        model = ImagePullQuoteBlock

    image = factory.django.ImageField()
    caption = FuzzyText()
