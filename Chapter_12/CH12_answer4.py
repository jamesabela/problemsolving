jokes_pool = [  
    ["Why did the computer go to the hospital?", "Because it had a virus!"],  
    ["What is a programmer's favorite hangout spot?", "The Foo Bar."]  
]

with open("interactive_jokes.html", "w") as file:  
    file.write("<html><body>
<h2>Click a question to show the answer!</h2>
")  
    for question, punchline in jokes_pool:  
        # Inject expanding detail component markup explicitly  
        file.write(f"<details>
  <summary>{question}</summary>
  <p style='color:blue;'>{punchline}</p>
</details><br>
")  
    file.write("</body></html>")
