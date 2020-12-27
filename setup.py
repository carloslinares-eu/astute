import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="as2t",
    version="0.0.1",
    author="Carlos Linares",
    author_email="contact@carloslinares.eu",
    description="Google Cloud Text to Speech App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carloslinares-eu/txt-2-speech",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
