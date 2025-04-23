import gradio as gr
from pypdf import PdfWriter

def merge_pdfs(pdf_files):
    merger = PdfWriter()
    for pdf in pdf_files:
        merger.append(pdf.name)
    output_path = "merged-pdf.pdf"
    merger.write(output_path)
    merger.close()
    return output_path
demo = gr.Interface(
    fn=merge_pdfs,
    inputs=gr.File(file_types=[".pdf"], label="Upload PDFs", file_count="multiple"),
    outputs=gr.File(label="Download Merged PDF"),
    title="PDF Merger",
    description="Upload multiple PDFs and get a single merged file."
)
demo.launch(share=True)