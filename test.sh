cd semantic-pdf-search
python -m build
pip uninstall semantic-pdf-search 
pip install dist/semantic_pdf_search-0.8.0-py3-none-any.whl
cd ..
semantic-pdf-search 
