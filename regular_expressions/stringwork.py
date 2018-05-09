import re

get = "Arizona 479, 501, 870. California 209, 213, 650"

m = re.findall("\d",
               get,
               re.IGNORECASE)

print(m)
