bookmarks = [  
    ["Google Search", "https://www.google.com"],  
    ["Wikipedia Encyclopedia", "https://www.wikipedia.org"],  
    ["Python Main Documentation", "https://www.python.org"]  
]

with open("bookmarks.html", "w") as html_file:  
    html_file.write("<html><body>
<h1>My Bookmarks</h1>
<ul>
")  
    for name, url in bookmarks:  
        html_file.write(f"  <li><a href='{url}'>{name}</a></li>
")  
    html_file.write("</ul>
</body></html>")
