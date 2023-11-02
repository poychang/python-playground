import argparse
from bs4 import BeautifulSoup as bs
from ebooklib import epub
from rich import print
from opencc import OpenCC

class BEPUB:
    def __init__(self, epub_name):
        self.epub_name = epub_name
        self.origin_book = epub.read_epub(self.epub_name)
        self.cc = OpenCC('s2tw')

    def translate_book(self):
        new_book = epub.EpubBook()
        new_book.metadata = self.origin_book.metadata
        new_book.spine = self.origin_book.spine
        new_book.toc = self.origin_book.toc
        for i in self.origin_book.get_items():
            if i.get_type() == 9:
                # ------------------------------------------------
                soup = bs(i.content, "html.parser")
                c_list = soup.contents
                for c in c_list:
                    if c.text and not c.text.isdigit():
                        try:
                            c.string = self.cc.convert(c.text)
                        except Exception as e:
                            print(str(e), style="bold red")
                            continue
                    # Process any remaining paragraphs in the last batch
                # p_list = soup.findAll("p")
                # for p in p_list:
                #     if p.text and not p.text.isdigit():
                #         try:
                #             p.string = self.cc.convert(p.text)
                #         except Exception as e:
                #             print(str(e), style="bold red")
                #             continue
                #     # Process any remaining paragraphs in the last batch
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
        "--book_name",
        dest="book_name",
        type=str,
        help="your epub book name",
    )
    options = parser.parse_args()
    e = BEPUB(options.book_name)
    e.translate_book()
