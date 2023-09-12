import tkinter as tk
from tkinter import ttk
from src.service.product_search_service import ProductSearchService


def search():
    query = search_entry.get()
    result.set("Resultados para: " + query)

    results = [
        ProductSearchService.search_product_in_mercadolivre,
        ProductSearchService.search_product_In_amazon
    ]

    res = ""
    for search_result in results:
        res += "\n" + str(search_result(query))
    result.set(res)

app = tk.Tk()
app.title("Pesquisa e Resultados")

# Barra de pesquisa
search_frame = ttk.Frame(app)
search_frame.pack(padx=10, pady=10)

search_label = ttk.Label(search_frame, text="Pesquisar:")
search_label.pack(side="left")

search_entry = ttk.Entry(search_frame)
search_entry.pack(side="left", fill="x", expand=True)

search_button = ttk.Button(search_frame, text="Pesquisar", command=search)
search_button.pack(side="right")

# Resultado da pesquisa
result = tk.StringVar()
result_label = ttk.Label(app, textvariable=result)
result_label.pack(padx=10, pady=5)

app.mainloop()