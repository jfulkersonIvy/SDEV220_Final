import re

# Search class
class Search:
    def __init__(self, searchValue=None):
        self.searchValue = searchValue

    # Search Method for Inventory
    def search(self, v, carList):
        search_value = v
        if search_value is None or len(search_value) == 0:
            return []
        else:
            makeList = []
            for value in search_value.split():
                search_value0 = (value).lower()
                search_value1 = (".+"+value+".+").lower()
                search_value2 = (value + ".+").lower()
                search_value3 = (".+" + value ).lower()
                for x in carList:
                    for key in x:
                        if re.search(search_value0, str(x[key]).lower()) or re.search(search_value1, str(x[key]).lower()) or re.search(search_value2, str(x[key]).lower()) or re.search(search_value3, str(x[key]).lower()):
                            makeList.append(x)
        return makeList