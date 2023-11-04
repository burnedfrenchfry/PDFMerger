import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog

def merge_pdfs(input_folder, output_file):
    pdf_merger = PyPDF2.PdfMerger()

    # Get a list of all PDF files in the input folder
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

    # Merge all PDF files into one
    for pdf_file in pdf_files:
        with open(os.path.join(input_folder, pdf_file), 'rb') as file:
            pdf_merger.append(file)

    # Write the merged PDF to the output file
    with open(output_file, 'wb') as output:
        pdf_merger.write(output)

    print(f'Merged {len(pdf_files)} PDF files into {output_file}')

def select_input_folder():
    input_folder = filedialog.askdirectory()  # Open a folder selection dialog
    input_folder_entry.delete(0, tk.END)  # Clear the current entry field value
    input_folder_entry.insert(0, input_folder)  # Set the entry field with the selected folder path

def select_output_file():
    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    output_file_entry.delete(0, tk.END)  # Clear the current entry field value
    output_file_entry.insert(0, output_file)  # Set the entry field with the selected file path

def merge_pdf_files():
    input_folder = input_folder_entry.get()
    output_file = output_file_entry.get()
    merge_pdfs(input_folder, output_file)

# Create the main application window
root = tk.Tk()
root.title("PDF Merger")

# Input Folder Selection
input_folder_label = tk.Label(root, text="Select Input Folder:")
input_folder_label.pack()
input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.pack()
input_folder_button = tk.Button(root, text="Browse", command=select_input_folder)
input_folder_button.pack()

# Output File Selection
output_file_label = tk.Label(root, text="Select Output File:")
output_file_label.pack()
output_file_entry = tk.Entry(root, width=50)
output_file_entry.pack()
output_file_button = tk.Button(root, text="Browse", command=select_output_file)
output_file_button.pack()

# Merge Button
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdf_files)
merge_button.pack()

# Start the Tkinter main loop
root.mainloop()
