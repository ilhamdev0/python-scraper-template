# Python Scraper Template

Template ini digunakan untuk kebutuhan scraping website

## Fitur
- Mendukung Async request
- Fitur Throttler dan delay, untuk mengatur jumlah request dan jeda ke server
- Terdapat 2 strategy yaitu:
    - normal: scrap semua data dalam sekali jalan (Otomatis)
    - incremental: scrap data secara bertahap (Semi-otomatis)

## Spesifikasi Tech Stack
- Type: Command Line Application
- Language: Python 3.10