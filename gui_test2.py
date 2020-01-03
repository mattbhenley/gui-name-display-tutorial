from guizero import App, Combo

app = App(title="My second GUI app", width= 300, height=200, layout="grid")

film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1, 0], align="left")

app.display()
