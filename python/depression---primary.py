# South East London (SEL) Long COVID Programme, 2024.

import sys, csv, re

codes = [{"code":"609311000000100","system":"snomedct"},{"code":"609311000000100","system":"snomedct"},{"code":"35489007","system":"snomedct"},{"code":"192080009","system":"snomedct"},{"code":"231485007","system":"snomedct"},{"code":"430421000000104","system":"snomedct"},{"code":"310495003","system":"snomedct"},{"code":"35489007","system":"snomedct"},{"code":"35489007","system":"snomedct"},{"code":"35489007","system":"snomedct"},{"code":"78667006","system":"snomedct"},{"code":"1084061000000106","system":"snomedct"},{"code":"78667006","system":"snomedct"},{"code":"161469008","system":"snomedct"},{"code":"199111000000100","system":"snomedct"},{"code":"413169006","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('depression-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["depression---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["depression---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["depression---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
