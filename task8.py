import re


def main(data_string):
    sections = ''.join(data_string.split()).split(',')[:-1]
    result = []
    for section in sections:
        matches1 = re.findall(r'to"(.*?)"</sect>', section)
        matches2 = re.findall(r'@"(.*?)"', section)
        result.append((''.join(matches1), matches2))
    return result


data_string1 = '<sect> make [@"erti_919" . @"rius" . @"aabige" ] to \
"ququce"</sect>,<sect> make[@"erbiza_837" . @"labior_177" . @"rear" ] \
to "rilabe" </sect>, <sect> make [@"isza" . @"rete_220". @"ribeus_266" \
]to "areste"</sect>, <sect> make [@"zave_459" . @"redian". @"ceriin"] \
to"esarxe_312"</sect>,'

data_string2 = '<sect>make [@"ertila_536". @"vedien_304". @"veenla" ]to"bian" \
</sect>,<sect> make [ @"tiis" . @"esma_350" ] to "edarxe" </sect>,'

print(main(data_string1))
print(main(data_string2))