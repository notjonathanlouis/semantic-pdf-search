from main import *
import tkinter as tk
from typing import Optional
from tkinter import ttk
import os
from pathlib import Path
import webbrowser

PDFS_DIR = Path(__file__).parent.parent / Path("pdfs")


class SemanticSearchGUI:
    


    def __init__(self):
        self.state = self.load_state()
        self.pdfs = self.get_stored_pdfs()
        self.main_window=tk.Tk()
        self.queries_results_frame=ttk.Frame(self.main_window)
        
        self.populate_file_dialogue()
        
            
    def get_stored_pdfs(self) -> list[str]: 
        return [str(child) for child in PDFS_DIR.iterdir()]
        

        
    def populate_file_dialogue(self) -> None:
        menu=tk.Menu(self.main_window)
        self.main_window.config(menu=menu)
        for path in self.pdfs:
            name = Path(path).name
            menu.add_command(label=name, command=lambda: self.load_known_pdf(path))
        menu.add_command(label="Open PDF", command=self.load_unknown_pdf)
    
    def get_previous_queries(self, pdf_path: str) -> None:
        if self.state != None: 

            self.queries_results_frame.columnconfigure(0,weight=1)
            self.queries_results_frame.columnconfigure(1,weight=1)
            
            for i,query in enumerate(self.state[pdf_path]):
                #add new row to grid here
                self.queries_results_frame.rowconfigure(i,weight=1)
                #add query as Label here
                query_label = ttk.Label(self.queries_results_frame,text=query)
                query_label.grid(column=0,row=i,sticky=tk.EW,padx=10,pady=10)
                query_results=ttk.Frame(self.queries_results_frame)
                query_results.grid(column=1,row=i,sticky=tk.EW,padx=10,pady=10)
                for j,result in enumerate(self.state[pdf_path][query]):
                    #add result as button 
                    query_result = ttk.Button(query_results,text=str(result), command = lambda: self.open_pdf(pdf_path, result))
                    query_result.pack(side=tk.LEFT)
                    
    def load_known_pdf(self,pdf_path:str)-> None:
        self.get_previous_queries(pdf_path)
        self.present_query_entry_field()
        ...
    def load_unknown_pdf(self)-> None:
        ...
    def open_pdf(self, pdf_path: str, page : int)-> None:
        """
        TODO: handle mac opening pdfs in webbrowser by using local server to host the PDF 
        """
        webbrowser.open(f"{pdf_path}#page={page}")

    def fresh_start(self)-> None:
        """
        +++++++++++++Fresh start++++++++
        User opens app, told to select Open ... -> Browse for PDF
        """
        ...
    
    def browse_for_pdf(self)->None:
        """
        +++++++++++++Open pdf+++++++++++
        User browses for and selects PDF. 
        """
        ...

    
    def store_pdf(self)->None:
        """
        It is copied into a set location to store PDFs used by this app. 
        If a file with the same name already exists, the two file 
        hashes will be compared and the incoming file will get a numeric 
        subscript to denote that the two files are distinct. 
        """
        ...

    
    def present_query_entry_field(self)->None:
        """
        A new frame is shown and the user is given a button which, 
        when pressed, presents an entry field for the user to enter a search query. 
        """
        query_entry_field = ttk.Entry(self.main_window,"Type query and press enter!")
        query_entry_field.bind("<Return>", lambda event: self.handle_enter_query(query_entry_field.get()))
        query_entry_field.pack(side=tk.BOTTOM)

    def handle_enter_query(self, entry:str )->None:
        """
        ++++++++++++++Enter query++++++++++
        The user enters a search query and taps enter. 
        """
        ...
    
    def display_search_bar(self)->None:
        """
        A search progress bar is shown, increasing in progress as the number of 
        pages searched increases. 
        """
        ...

    def display_results(self)->None:
        """
        Once all pages have been searched and the top 5 results have been found, 
        the pages will be shown to the user as a horizontal row of buttons labeled 
        with the resulting page numbers.         
        """
        ...


        """
        The user is given a button which, when pressed, presents an entry field for the 
        user to enter a search query. 
        (satisfied by `spawn_new_query_entry`)
        """

    def save_state(self)-> None:
        """
        The query, the PDF hash, and all the results will be stored to a 
        pickle dictionary file. 
        """
        
    def load_state(self) -> Optional[dict[str, dict[str, list[int]]]]:
        """
        Load state from pickle file and returns a dictionary representation. If there is no saved state, 
        returns None.
        """



gui = SemanticSearchGUI()
gui.main_window.mainloop()
print(gui.get_stored_pdfs())