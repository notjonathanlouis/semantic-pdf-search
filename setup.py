from setuptools import setup, find_packages

setup(
	name="semantic-pdf-search",
	author="notjonathanlouis",
	version="0.8.0",
	url="https://github.com/notjonathanlouis/semantic-pdf-search",
	packages=find_packages(),
	python_requires='>=3.6',
	install_requires=[
		"tkinter",
		"ttkbootstrap",
        "pymupdf",
        "webbrowser",  
        "pickle",  
        "torch",
        "sentence-transformers",  
    ],
)