import pandas as pd

from datetime import datetime
from django.core.files.base import ContentFile
from dataset.models import DataSet


def build_dataframe(data_types, row_qty, faker):
    df = pd.DataFrame(data={})
    for data_type in data_types:
        values_lst = []
        match data_type.data_type:
            case "FN":
                for _ in range(row_qty):
                    values_lst.append(faker.get_fullname())
            case "EM":
                for _ in range(row_qty):
                    values_lst.append(faker.get_email())
            case "BR":
                for _ in range(row_qty):
                    values_lst.append(
                        faker.get_birthday_date(
                            data_type.range_from, data_type.range_to
                        )
                    )
            case "DM":
                for _ in range(row_qty):
                    values_lst.append(faker.get_full_domain())
            case "AD":
                for _ in range(row_qty):
                    values_lst.append(faker.get_address())
            case "PN":
                for _ in range(row_qty):
                    values_lst.append(faker.get_phone_number())
            case "AG":
                for _ in range(row_qty):
                    values_lst.append(
                        faker.get_age(data_type.range_from, data_type.range_to)
                    )
            case "TX":
                for _ in range(row_qty):
                    values_lst.append(
                        faker.get_text(data_type.range_from, data_type.range_to)
                    )
        df[data_type.column_name] = values_lst
    return df


def create_data_set(schema, df):
    uniq_code = datetime.now()
    file_name = f"{schema.name}_{uniq_code}.csv"
    file = ContentFile(df.to_csv(sep=schema.column_separator), name=file_name)
    data_set = DataSet.objects.create(schema=schema, csv_data=file, is_done=True)
    return data_set
