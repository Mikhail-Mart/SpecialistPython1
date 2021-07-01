# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def pagination2(num_items, items_on_page):
    if num_items % items_on_page == 0:
        return items_on_page
    elif num_items < items_on_page:
        return num_items
    return num_items % items_on_page  
