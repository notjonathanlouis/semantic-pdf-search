import tkinter as tk
from typing import Optional
import ttkbootstrap as ttk
from tkinter import filedialog
import os
import shutil
from pathlib import Path
import webbrowser
import pymupdf
PDFS_DIR = Path(__file__).parent.parent / Path("pdfs")




class SemanticSearchGUI:
    def __init__(self):
        self.state = self.load_state()
        if self.state == None:
            self.fresh_start()
        else:
            self.pdfs = self.get_stored_pdfs()
        self.main_window=tk.Tk()
        ttk.Style().theme_use('sandstone')
        self.query_frame = ttk.Frame(self.main_window)
        self.queries_results_frame=ttk.Frame(self.main_window)
        
        self.populate_file_dialogue()
        
            
    def get_stored_pdfs(self) -> list[str]: 
        return [str(child) for child in PDFS_DIR.iterdir()]
        

        
    def populate_file_dialogue(self) -> None:
        self.menubar=tk.Menu(self.main_window)
        submenu=tk.Menu(self.menubar,tearoff=0)
        self.main_window.config(menu=self.menubar)
        self.menubar.add_cascade(label="Open ...",menu=submenu)
        self.menubar.add_command(label="")
        for path in self.pdfs:
            name = Path(path).name
            submenu.add_command(label=name, command=lambda path=path: self.load_known_pdf(path))
        submenu.add_separator()
        submenu.add_command(label="Open PDF", command=self.browse_for_pdf)
    
    def get_previous_queries(self, pdf_path: str) -> None:
        if self.state != None and pdf_path in self.state: 
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
                    query_result = ttk.Button(query_results,text=str(result), command = lambda pdf_path=pdf_path,result=result: self.open_pdf(pdf_path, result))
                    query_result.pack(side=tk.LEFT)
            self.queries_results_frame.pack()  
    def load_known_pdf(self,pdf_path:str)-> None:
        self.queries_results_frame.destroy()
        self.queries_results_frame=ttk.Frame(self.main_window)
        self.query_frame.destroy()
        
        progress_bar= ttk.Progressbar(self.main_window,orient="horizontal",mode="determinate")
        progress_bar.pack(side=tk.BOTTOM,padx=20,pady=20,fill='x',anchor='center')
        progress_text= ttk.Label(self.main_window,text="Importing Libraries")
        progress_text.pack(side=tk.BOTTOM)
        progress_bar.step(5)
        self.main_window.update()
        from main import Searcher,SentenceEncoder
        MODEL = SentenceEncoder.MODEL1
        
        progress_bar.step(15)
        self.main_window.update()
        self.current_pdf_path=pdf_path
        progress_text.configure(text="Loading Previous Queries")
        progress_bar.step(5)
        self.main_window.update()
        self.get_previous_queries(pdf_path)
        progress_bar.step(10)
        progress_text.configure(text="Loading Embeddings")
        self.main_window.update()
        self.search = Searcher.forPDF(
        SentenceEncoder(
            MODEL),pdf_path)
        progress_bar.step(40)
        progress_text.configure(text="Finalizing")
        
        self.main_window.update()
        self.main_window.title(f"Semantic search: {Path(pdf_path).name}")
        self.menubar.delete(2)
        self.menubar.add_command(label=f"Current PDF: {Path(pdf_path).name}")
        progress_bar.destroy()
        self.show_search_bar()
        progress_text.destroy()
        ...
    def browse_for_pdf(self)-> None:
        """
        +++++++++++++Open pdf+++++++++++
        User browses for and selects PDF. 

        This function will open the file dialog, and allow the user to select a PDF. The selected
        PDF will get hashed and if the hash does not match any known hash, then the PDF will get copied into 
        our PDF directory and the embeddings will get created.
        """
        
        filepath = filedialog.askopenfilename(title='Select a PDF file', initialdir=os.getcwd(), filetypes=(('PDF', '*.pdf'), ))
        from main import Corpus,Constants
        MODEL = Constants.MODEL1
        EMBEDDINGS_DIR = Path(__file__).parent.parent / Path("embeddings") / Path(f"Encoder: {MODEL}")
        if filepath:
            reader = pymupdf.open(filepath)
            pages = [reader.load_page(i) for i in range(len(reader))]
            corpus = Corpus([page.get_text() for page in pages])
            corpus_hash=corpus.__hash__
            embedding = (EMBEDDINGS_DIR / Path(str(corpus_hash)))
            if embedding not in  EMBEDDINGS_DIR.iterdir():
                if(Path(filepath) not in PDFS_DIR.iterdir()):
                    new_path = PDFS_DIR / Path(filepath).name
                    shutil.copy(filepath,PDFS_DIR)
                    self.load_known_pdf(str(new_path))
                else:
                    new_path = PDFS_DIR / Path(f"{Path(filepath).name}_")
                    shutil.copy(filepath,new_path)
                    self.load_known_pdf(str(new_path))
            reader.close()


    def open_pdf(self, pdf_path: str, page : int)-> None:
        """
        TODO: handle mac opening pdfs in webbrowser by using local server to host the PDF 
        """
        webbrowser.open(f"file://{pdf_path}#page={page}")

    def fresh_start(self)-> None:
        """
        +++++++++++++Fresh start++++++++
        User opens app, told to select Open ... -> Browse for PDF
        """
        intro = ttk.Label(self.queries_results_frame, text="To start a search, first select a PDF. \n " \
        "Click on Open ... -> Browse for PDF.")
        intro.grid(column=1,row=1)
        ...
    
    
    
    def store_pdf(self)->None:
        """
        It is copied into a set location to store PDFs used by this app. 
        If a file with the same name already exists, the two file 
        hashes will be compared and the incoming file will get a numeric 
        subscript to denote that the two files are distinct. 
        """
        ...

    
    def show_search_bar(self)->None:
        """
        A new frame is shown and the user is given a button which, 
        when pressed, presents an entry field for the user to enter a search query. 
        """
        self.query_frame = ttk.Frame(self.main_window)
        self.query_frame.pack(side=tk.BOTTOM,pady=50)
        entry_text=tk.StringVar()
        query_entry_field = ttk.Entry(self.query_frame,textvariable=entry_text)
        query_entry_instructions = ttk.Label(self.query_frame,text="Enter query:")
        query_entry_instructions.pack(side=tk.LEFT,padx=20)
        query_entry_field.bind("<Return>", lambda event: self.handle_enter_query(entry_text.get()))
        query_entry_field.pack(side=tk.BOTTOM)

    def handle_enter_query(self, entry:str )->None:
        """
        ++++++++++++++Enter query++++++++++
        The user enters a search query and taps enter. 
        """
        if self.state != None:
            if self.current_pdf_path not in self.state:
                self.state[self.current_pdf_path]={entry:self.search(entry,top_k=5)}
            else:
                self.state[self.current_pdf_path][entry]=self.search(entry,top_k=5)
        self.get_previous_queries(self.current_pdf_path)
        ...
    


    def display_results(self,query:str, results: list[int])->None:
        """
        Once all pages have been searched and the top 5 results have been found, 
        the pages will be shown to the user as a horizontal row of buttons labeled 
        with the resulting page numbers.         
        """
        #add new row to grid here
        self.queries_results_frame.rowconfigure(0,weight=1)
        self.queries_results_frame.columnconfigure(1, weight=3)
        #add query as Label here
        query_label = ttk.Label(self.queries_results_frame, text=query)        
        query_label.grid(column=0, row=0, sticky=tk.EW, padx=10, pady=10)
        query_results=ttk.Frame(self.queries_results_frame)
        query_results.grid(column=1, row=0, sticky=tk.EW, padx=10, pady=10)

        for j,result in enumerate(results):
            #add result as button 
            query_result = ttk.Button(query_results,text=str(result), command = lambda result=result: self.open_pdf(self.current_pdf_path, result), style='Accent.TButton', padding=0)
            query_result.pack(side=tk.RIGHT)
        self.queries_results_frame.pack()


    # """
    # The user is given a button which, when pressed, presents an entry field for the 
    # user to enter a search query. 
    # (satisfied by `spawn_new_query_entry`)
    # """

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
        state=dict[str,dict[str,list[int]]]()
        return state



gui = SemanticSearchGUI()
gui.main_window.mainloop()
#print(gui.get_stored_pdfs())