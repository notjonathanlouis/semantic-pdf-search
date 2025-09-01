# semantic-pdf-search

**A semantic PDF searching application, written in Python.** 🔎

By Jordan Zedeck and Jonathan Louis

-----

## 📖 Overview

The **semantic-pdf-search** application utilizes machine learning and an embedding model to encode both a PDF document and a user's query. This process enables the application to find **near-matches** to the query within the document, much like an internet search engine would for web-pages. The page number results are displayed as buttons which can be clicked to open the PDF directly to the page in your default web browser.

## ✨ Features

  * **Semantic Search:** Finds near-matches and related concepts, not just exact keywords.
  * **Offline Operability:** Once semantic-pdf-search is installed, it can be used completely offline.
  * **Cross-Platform:** Supports Linux, Windows and macOS.

## 💻 Installation

### Prerequisites

This package requires **Tkinter**. If you run the command `python -m tkinter` and a new window does not appear, you will need to install it manually.

  * **Windows:** Re-run the [Python installer](https://www.python.org/downloads/windows/) and ensure the **tcl/tk** checkbox is ticked.
  * **macOS:** Install Tkinter using Homebrew with the following command:
    ```
    brew install python-tk
    ```
  * **Linux:** Varies depending on package manager:
  	* **Debian:**:
	    ```
	    sudo apt install python3-tk
	    ```
	* **Fedora:**:
	    ```
	    sudo dnf install python3-tkinter
	    ```
	* **Arch:** (note that pip installing packages on Arch requires using a venv):
	    ```
	    sudo pacman -S tk
	    ```

### From PyPI

The easiest way to install the package is using `pip`.

```
pip install semantic-pdf-search
```

### From Source

To install from the GitHub repository, follow these steps:

```
cd semantic-pdf-search
python -m build
pip install dist/semantic_pdf_search-0.8.0-py3-none-any.whl
```

-----

## 🚀 Launching semantic-pdf-search

Once installed, run the application from your command line:

```
semantic-pdf-search
```

### Basic Usage Guide

1.  **Browse for a PDF:** The application window will open. Click on "File" -> "Open ..." -> "Browse for PDF" to select a PDF file.
2.  **Select and Open:** Navigate to your PDF, select it, and click "Open".
3.  **Wait for Embeddings:** The application will process the document and create embeddings. This may take a moment, especially for large files.
4.  **Enter a Query:** Once the document is loaded, type your query into the search bar and press **Enter**.
5.  **View Results:** The application will display a list of page numbers that contain near-matches to your query.
6.  **Open the Page:** Click on any of the result buttons to open the PDF directly to that page in your default web browser.

-----

## 🖼️ Example

**Query:** 
<p align="center">
    <img src="assets/great-gatsby-search.png" alt="landing" height=530 />
</p>

**Result:**
<p align="center">
    <img src="assets/great-gatsby-result.png" alt="landing" height=530 />
</p>





# semantic-pdf-search
By Jordan Zedeck and Jonathan Louis

A semantic PDF searching application, written in python. This application uses ML an embedding model to encode the document and the user's query, allowing for near-matches of the query to be presented to the user. The page numbers with near-matches are shown to the user as buttons which, when clicked, will open the PDF at that page in the default browser.



### Example:

![alt text](assets/great-gatsby-search.png)

![alt text](assets/great-gatsby-result.png)
## This package requires tkinter!!!!
## See the section below for instructions on installing tkinter on macOS and Windows
### Installing tkinter on macOS and Windows:
If the following command does not open a new tk window, 
`python -m tkinter`
Then you must install tkinter manually:

#### Windows
Run the [python installer](https://www.python.org/downloads/windows/)
Ensure the tcl/tk checkbox is ticked

#### macOS
With brew:
`brew install python-tk`

### Installation:
From pip:
`pip install semantic-pdf-search`
Install from source:
(in the root directory of the github project)
```
cd semantic-pdf-search
python -m build
pip install dist/semantic_pdf_search-0.8.0-py3-none-any.whl
```

### Usage tutorial:

From the command line:

`semantic-pdf-search`

Browse for a new PDF:

![alt text](assets/open_pdf.png)

Select a PDF and click 'Open':

![alt text](assets/open_pdf_part_2.png)

Wait for the embeddings to be created and/or loaded:

![alt text](assets/loading_embeddings.png)

Type a query and press enter:

![alt text](assets/enter_query.png)

Click on any of the results to open the PDF to that page in your default web-browser:

![alt text](assets/search_result.png)

![alt text](assets/open_pdf_in_browser.png)