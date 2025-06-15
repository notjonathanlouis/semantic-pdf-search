from main import *
import sys
import os
import webbrowser
import platform

if __name__ == "__main__":
    """
    python3 cli <pdf name> <query>+
    """
    if len(sys.argv) < 2:
        raise Exception("Missing pdf file name")
    if len(sys.argv) < 3:
        raise Exception("Missing query")
    pdf_name = sys.argv[1]
    if pdf_name[0] == '"':
        pdf_name = pdf_name[1:-2]
    query = " ".join(sys.argv[2:])
    if query[0] == '"':
        query = query[1:-2]
    search = Searcher.forPDF(
        SentenceEncoder(
            SentenceEncoder.MODEL1),
        pdf_name)
    page_nums = search(query,  None)
    

    for page in page_nums:
        cmd = f"file://{os.getcwd()}/{pdf_name}#page={page}"
        print(cmd)
        webbrowser.open_new_tab(cmd)
        input(">>>")
