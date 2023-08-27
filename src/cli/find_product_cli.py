from src.service.product_search_service import ProductSearchService

class FindProductCli:
    @staticmethod
    def run():
        while True:
            product_name = input("Say a product name:")
            ProductSearchService.search_product_in_mercadolivre(product_name)
            ProductSearchService.search_product_In_amazon(product_name)