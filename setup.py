from setuptools import setup


setup(
    name="django-sorlimageblock",
    version="0.1.0",
    author="Columbia University's Center for Teaching and Learning",
    author_email="ccnmtl-dev@columbia.edu",
    url="https://github.com/ccnmtl/django-sorlimageblock",
    description="sorl-ified ImageBlock for django-pagetree.",
    install_requires=[
        "django-pagetree>=1.1.14",
        "sorl==3.1",
    ],
    scripts=[],
    license="GPL-2.0+",
    zip_safe=False,
    packages=['sorlimageblock'],
    include_package_data=True,
)
