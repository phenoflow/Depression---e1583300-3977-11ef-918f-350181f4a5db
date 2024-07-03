# South East London (SEL) Long COVID Programme, 2024.

import sys, csv, re

codes = [{"code":"274948002","system":"snomedct"},{"code":"268621008","system":"snomedct"},{"code":"191610000","system":"snomedct"},{"code":"191611001","system":"snomedct"},{"code":"764611000000100","system":"snomedct"},{"code":"191613003","system":"snomedct"},{"code":"46244001","system":"snomedct"},{"code":"191616006","system":"snomedct"},{"code":"268621008","system":"snomedct"},{"code":"1976211000006100","system":"snomedct"},{"code":"1976231000006106","system":"snomedct"},{"code":"1976251000006104","system":"snomedct"},{"code":"1976271000006109","system":"snomedct"},{"code":"191616006","system":"snomedct"},{"code":"191616006","system":"snomedct"},{"code":"191616006","system":"snomedct"},{"code":"191616006","system":"snomedct"},{"code":"310495003","system":"snomedct"},{"code":"310496002","system":"snomedct"},{"code":"268621008","system":"snomedct"},{"code":"28475009","system":"snomedct"},{"code":"191613003","system":"snomedct"},{"code":"191613003","system":"snomedct"},{"code":"1086471000000103","system":"snomedct"},{"code":"698957003","system":"snomedct"},{"code":"755331000000108","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('depression-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["depression-recurr---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["depression-recurr---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["depression-recurr---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
