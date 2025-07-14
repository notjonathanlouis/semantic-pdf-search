# semantic-PDF-search
By Jordan Zedeck and Jonathan Louis

A semantic PDF searching application, written in python. This application uses ML an embedding model to encode the document and the user's query, allowing for near-matches of the query to be presented to the user. The page numbers with near-matches are shown to the user as buttons which, when clicked, will open the PDF at that page in the default browser.


### Example:

![alt text](assets/great-gatsby-search.png)
![alt text](assets/great-gatsby-result.png)

### Installation:

(tbd)

### Usage tutorial:

From the command line:
`semantic-search-gui`

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