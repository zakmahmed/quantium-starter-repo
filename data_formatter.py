import csv


def extract_contents_from_file(input_file: str) -> list[list]:
    products = []
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row[0] == 'pink morsel':
                    price = str('$'+ f"{float(row[1].replace('$', '')) * float(row[2]):.2f}")

                    products.append(
                        [price, row[3], row[4]])
    csv_file.close()

    return products


def combinator(list_1: list[list], list_2: list[list], list_3: list[list]) -> list[list]:
    combined_list = list_1 + list_2 + list_3
    return combined_list


def write_contents_to_file(contents: list[list]) -> None:
    with open('data/pink_morsel.csv', mode='w+') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['sales', 'date', 'region'])

        for row in contents:
            csv_writer.writerow(row)

    csv_file.close


products_0 = extract_contents_from_file('data/daily_sales_data_0.csv')
products_1 = extract_contents_from_file('data/daily_sales_data_1.csv')
products_2 = extract_contents_from_file('data/daily_sales_data_2.csv')


pink_morsel_list = combinator(products_0, products_1, products_2)

write_contents_to_file(pink_morsel_list)
