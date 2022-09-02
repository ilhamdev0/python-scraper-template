all: help

install:
	@echo "Mulai..."
	@python -m venv env
	@source env/bin/activate && pip install -r requirements.txt
	@echo "Selesai"

help:
	@echo "Python Scraper Template"
	@echo "Gunakan command 'make install' saat pertama kali"
	@echo "Perintah diatas akan membuat virtual environment dan menginstal dependensi yang diperlukan"
	
