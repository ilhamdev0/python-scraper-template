from abc import ABC, abstractmethod

class Template(ABC):
    url: str
    data = None # Menampung data untuk pengolahan lebih lanjut

    def _guardclause(self) -> bool:
        if len(self.url) < 1 :
            print("url kosong!")
            return True

        if self.data is None:
            print("crawl dulu!")
            return True
        
        return False

    # mendownload halaman web
    @abstractmethod
    def crawl(self) -> None:
        pass

    # mengekstrak sesuai target yang diinginkan
    @abstractmethod
    def extract(self) -> None:
        pass

    # memformat tampilan sebelum di save
    @abstractmethod
    def format(self) -> None:
        pass

    # menyimpan data ke bentuk tertentu
    @abstractmethod
    def save(self) -> None:
        pass

class Scrap(Template):
    url = "https://example.com/"

    def crawl(self):
        self.data = ""
        if self._guardclause(): return

        import aiohttp
        import asyncio

        async def fetch():
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url) as response:
                    self.data = await response.text()
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(fetch())
    
    def extract(self):
        if self._guardclause(): return

        from bs4 import BeautifulSoup

        self.soup = BeautifulSoup(self.data, 'html.parser')

    def format(self):
        if self._guardclause(): return
                
    def save(self):
        if self._guardclause(): return