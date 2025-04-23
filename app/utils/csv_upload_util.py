from fastapi import UploadFile
import io
import csv
import subprocess
from datetime import date
from app.configs.get_client import get_clickhouse_client

def csv_upload_util(file: UploadFile, upload_date: date):
    input_stream = io.StringIO(file.file.read().decode("ISO-8859-1"))
    output_stream = io.StringIO()

    reader = csv.reader(input_stream)
    writer = csv.writer(output_stream)

    header = next(reader, None)
    if header:
        # Append "Upload_Date" to header (57th column)
        header.append("Upload_Date")
        writer.writerow(header)

    # Skip second row
    next(reader, None)

    for row in reader:
        if len(row) == 56:  # expected CSV rows
            row.append(str(upload_date))  # Add Upload_Date as 57th column
            writer.writerow(row)

    output_stream.seek(0)
    csv_data_bytes = output_stream.getvalue().encode("ISO-8859-1")

    # client = get_clickhouse_client()
    # client.insert_csv("diamonds", output_stream.getvalue())
    subprocess.run([
        "wsl", "clickhouse-client",
        "--query=INSERT INTO diamonds FORMAT CSVWithNames"
    ], input=csv_data_bytes)