import xml.sax
from xml.sax.saxutils import escape

class AlbumHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.albums = []
        self.current_album = {}
        self.in_album = False
        self.in_title = False
        self.in_year = False

    def startElement(self, name, attrs):
        if name == "album":
            self.current_album = {}
            self.current_album["title"] = ""
            self.current_album["year"] = ""
            self.in_album = True
        elif name == "titre" and self.in_album:
            self.in_title = True
        elif name == "annee" and self.in_album:
            self.in_year = True

    def characters(self, content):
        if self.in_title:
            self.current_album["title"] += content
        elif self.in_year:
            self.current_album["year"] += content

    def endElement(self, name):
        if name == "album":
            self.albums.append(self.current_album)
            self.in_album = False
        elif name == "titre":
            self.in_title = False
        elif name == "annee":
            self.in_year = False

    def get_albums(self):
        return self.albums

def generate_html(albums):
    html_content = "<html><head><title>Albums List</title></head><body>"
    html_content += "<h1>List of Albums</h1>"
    html_content += "<ul>"

    for album in albums:
        title = escape(album["title"])  # Escape HTML characters
        year = album["year"]
        html_content += f"<li>{title} - {year}</li>"

    html_content += "</ul></body></html>"
    return html_content

def main(xml_file_path, html_output_path):
    handler = AlbumHandler()
    xml.sax.parse(xml_file_path, handler)

    albums = handler.get_albums()
    html_content = generate_html(albums)

    with open(html_output_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    xml_file_path = "artisteDevoir.xml"
    html_output_path = "albums_list.html"
    main(xml_file_path, html_output_path)
    print(f"HTML page generated: {html_output_path}")
