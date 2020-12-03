import os

def search(start_dir, searched_name):
    result = []
    dirs_to_search = [start_dir]

    while dirs_to_search:
        current_dir = dirs_to_search.pop(0)

        for name in os.listdir(current_dir):
            item_name = os.path.join(current_dir, name)
            if name == searched_name:
                result.append(current_dir)

            if os.path.isdir(item_name):
                dirs_to_search.append(item_name)

    return result


#print(search('/home/zorell/python/python-academy/Python 4.Základy scrapingu/Importovanie', 'zoli'))
print(search('/home/zorell/python/python-academy', 'test.py'))
