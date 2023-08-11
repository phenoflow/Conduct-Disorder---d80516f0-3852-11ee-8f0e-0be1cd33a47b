# Catherine Morgan, Roger T Webb, Mathew J Carr, Evangelos Kontopantelis, Jonathan Green, Carolyn A Chew-Graham, Nav Kapur, Darren M Aschcroft, 2023.

import sys, csv, re

codes = [{"code":"E284.00","system":"readv2"},{"code":"E2C4.00","system":"readv2"},{"code":"E2C4z00","system":"readv2"},{"code":"Eu92.00","system":"readv2"},{"code":"Eu92y00","system":"readv2"},{"code":"Eu92z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('conduct-disorder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["conduct-disorder-xmixed---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["conduct-disorder-xmixed---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["conduct-disorder-xmixed---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
