import os

from setuptools import setup


setup(
    name="django-auditlog",
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    packages=[
        "auditlog",
        "auditlog.migrations",
        "auditlog.management",
        "auditlog.management.commands",
    ],
    url="https://github.com/toladata-software/django-auditlog",
    license="MIT",
    author="TolaData",
    description="Audit log app for Django",
    long_description="Audit log app for Django",
    long_description_content_type="text/markdown",
    install_requires=["django-jsonfield>=1.0.0", "python-dateutil>=2.6.0"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "License :: OSI Approved :: MIT License",
    ],
)
