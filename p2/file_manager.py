import glob
import os
import re

files = glob.glob("*.txt")

for file in files:
    base = os.path.splitext(file)[0]

    with open(base + "_id1.csv", "w", encoding="utf-8") as f1, \
         open(base + "_id2.csv", "w", encoding="utf-8") as f2:

        header = "id,counter,RSSI,SNR\n"
        f1.write(header)
        f2.write(header)

        with open(file, "r", encoding="utf-8") as fin:
            for line_num, line in enumerate(fin, start=1):
                original = line.strip()

                if not original:
                    continue

                # Remove Arduino Serial Monitor timestamp prefix:
                # Example: 11:12:35.016 -> 2,2011,-115,-7.50
                cleaned = re.sub(r"^\d{2}:\d{2}:\d{2}\.\d{3}\s*->\s*", "", original)

                # Remove spaces everywhere inside the data part
                cleaned = cleaned.replace(" ", "")

                parts = cleaned.split(",")

                if len(parts) != 4:
                    print(f"Skipping bad row in {file} line {line_num}: {original}")
                    continue

                id_val, counter, rssi, snr = parts

                # Validate types
                try:
                    int(id_val)
                    int(counter)
                    int(rssi)
                    float(snr)
                except ValueError:
                    print(f"Skipping invalid row in {file} line {line_num}: {original}")
                    continue

                output_line = f"{id_val},{counter},{rssi},{snr}\n"

                if id_val == "1":
                    f1.write(output_line)
                elif id_val == "2":
                    f2.write(output_line)
                else:
                    print(f"Skipping unknown id in {file} line {line_num}: {original}")

print("Done.")