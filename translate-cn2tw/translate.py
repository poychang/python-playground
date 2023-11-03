import argparse
from bs4 import BeautifulSoup as bs
from ebooklib import epub
from rich import print
from opencc import OpenCC

class BEPUB:
    def __init__(self, epub_name):
        self.epub_name = epub_name
        self.origin_book = epub.read_epub(self.epub_name)
        self.cc = OpenCC('s2twp.json')

    def translate_book(self):
        new_book = epub.EpubBook()
        new_book.metadata = self.origin_book.metadata
        new_book.spine = self.origin_book.spine
        new_book.toc = self.origin_book.toc
        for i in self.origin_book.get_items():
            if i.get_type() == 9:
                # ------------------------------------------------
                soup = bs(i.content, "html.parser")
                h1_list = soup.findAll("h1")
                for h1 in h1_list:
                    if h1.text and not h1.text.isdigit():
                        try:
                            h1.string = self.cc.convert(h1.text)
                        except Exception as e:
                            print(str(e), style="bold red")
                            continue
                # ------------------------------------------------
                h2_list = soup.findAll("h2")
                for h2 in h2_list:
                    if h2.text and not h2.text.isdigit():
                        try:
                            h2.string = self.cc.convert(h2.text)
                        except Exception as e:
                            print(str(e), style="bold red")
                            continue
                # ------------------------------------------------
                h3_list = soup.findAll("h3")
                for h3 in h3_list:
                    if h3.text and not h3.text.isdigit():
                        try:
                            h3.string = self.cc.convert(h3.text)
                        except Exception as e:
                            print(str(e), style="bold red")
                            continue
                # ------------------------------------------------
                p_list = soup.findAll("p")
                for p in p_list:
                    if p.text and not p.text.isdigit():
                        try:
                            p.string = self.cc.convert(p.text)
                        except Exception as e:
                            print(str(e), style="bold red")
                            continue
                # ------------------------------------------------
                print("------------------------------ done with ", i)
                i.content = soup.prettify().encode()
            new_book.add_item(i)
        name = self.epub_name.split(".epub")[0]
        epub.write_epub(f"{name}_translated.epub", new_book, {})
        print(f"Translated book saved as '{name}_translated.epub'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file-path",
        dest="file_path",
        type=str,
        help="your epub book full path",
    )
    options = parser.parse_args()
    e = BEPUB(options.file_path)
    e.translate_book()
