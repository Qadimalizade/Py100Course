def find_common_items(last_week_purchases, current_week_purchases):
    intersrction_week = list(set(current_week_purchases).intersection(last_week_purchases))
    intersrction_week.sort()
    return intersrction_week


last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")  # TODO Распечатайте общие товары
