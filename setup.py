import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()



__version__ = "0.0.0"

REPO_NAME = "Text Summarizer Project"
AUTHOR_USER_NAME = "davidcibeabuchi"
SRC_REPO = "text_summariser"
AUTHOR_EMAIL = "davidcibeabuchi@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description=REPO_NAME,
        long_description=long_description,
        long_description_content_type="text/markdown",
                url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
                project_urls={
                    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
                    "Documentation": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/blob/main/README.md",
                    "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
                },
                package_dir={"": "src"},
                packages=setuptools.find_packages(where='src'),
                
)