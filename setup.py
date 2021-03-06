from distutils.core import setup

setup(
    name = "summary",
    packages = ["summary"],
    version = "0.1.1",
    install_requires = ["chardet", "lxml==2.3.5"],
    description = "Extractor to get main content from the web page.",
    author = "Satoshi Okami",
    author_email = "me.after.12am@gmail.com",
    url = "https://github.com/after12am/summary",
    download_url = "https://github.com/after12am/summary/archive/master.zip",
    keywords = ["summary", "extract", "scraping", "web"],
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Operating System :: MacOS",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet"
    ],
    long_description = """\

Extractor to get main content from the web page.
 - title
 - body
 - candidates of main image

Install
   sudo easy_install "summary==0.1.1"

Usages
   visit at https://github.com/after12am/summary
"""
)