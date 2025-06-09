from main import *
import tkinter as tk
from tk import ttk


class SemanticSearchGUI:
    
    def __init__(self, arg):
        if(os.listdir)
        
    """
    +++++++++++++Fresh start++++++++
    User opens app, told to select Open ... -> Browse for PDF
    """
    def fresh_start(self)-> None:
        ...
    """
    +++++++++++++Open pdf+++++++++++
    User browses for and selects PDF. 
    """
    def browse_for_pdf(self)->None:
        ...

    """
    It is copied into a set location to store PDFs used by this app. 
    If a file with the same name already exists, the two file 
    hashes will be compared and the incoming file will get a numeric 
    subscript to denote that the two files are distinct. 
    """
    def store_pdf(self)->None:
        ...

    """
    A new frame is shown and the user is given a button which, 
    when pressed, presents an entry field for the user to enter a search query. 
    """
    def present_query_menu(self)->None:
        ...

    def spawn_new_query_entry(self)->None:
        ...
    
    """
    ++++++++++++++Enter query++++++++++
    The user enters a search query and taps enter. 
    """
    def handle_enter_query(self)->None:
        ...
    """
    A search progress bar is shown, increasing in progress as the number of 
    pages searched increases. 
    """
    def display_search_bar(self)->None:

    """
    Once all pages have been searched and the top 5 results have been found, 
    the pages will be shown to the user as a horizontal row of buttons labeled 
    with the resulting page numbers.         
    """
    def display_results(self)->None:

    """
    The user is given a button which, when pressed, presents an entry field for the 
    user to enter a search query. 
    (satisfied by `spawn_new_query_entry`)
    """


    """
    The query, the PDF hash, and all the results will be stored to a 
    pickle dictionary file. 
    """
    def save_queries_and_results(self)->None:




