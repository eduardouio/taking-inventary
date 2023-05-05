# Load images in database
# 1. run script download_images.py
# 3. run this script
from django.core.files import File
import json
import os

current_path = os.path.dirname(os.path.abspath(__file__))
base_dir = '/app/images/products/'
report_file = open(current_path + "/images/report.json", "r")
report = json.loads(report_file.read())
query_update = []
for item in report:
    if item["url_img"]:
        query = "UPDATE products_product SET image_front = '" + base_dir + \
            item["url_img"].split("/")[-1] + "' WHERE account_code = '" + \
                str(item["account_code"]) + "';"
        query_update.append(query)

open("query.sql", "w").write(json.dumps(query_update))
