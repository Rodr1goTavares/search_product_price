from cli.find_product_cli import FindProductCli
from views.app_graph_interface import search

class Main:
    @staticmethod
    def run():
        search()
        # FindProductCli.run()

if __name__ == "__main__":
    Main.run()