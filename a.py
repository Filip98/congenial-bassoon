from os.path import splitext
from pdftotext import PDF
from textract import process
from chardet import detect

filenames=["Opsti-deo.pdf"]
for filename in filenames:
	no_ext = splitext(filename)[0]

	with open(no_ext+"_pdftotext.txt", "w", encoding = "utf-8") as file:
		with open(filename, "rb") as f:
			pdf = PDF(f)
			for page in pdf:
				file.write(page)

	text = process(filename, method = "pdftotext")
	text = text.decode(detect(text)["encoding"])

	with open(no_ext+"_textract.txt", "w", encoding = "utf-8") as file:
		file.write(text)
