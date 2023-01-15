import json

class buildProductRequestBody:
    json
    
def buildRequest(productName, productType, productVersion):
    product = {
        "product_name": productName,
        "product_type": productType,
        "product_version": productVersion
    }    
    product_json = json.dumps(product)    
    return product_json
    

