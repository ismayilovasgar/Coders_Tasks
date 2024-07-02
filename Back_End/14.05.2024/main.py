from Packets import samitler

cumle = "  salam  necesen  neynirirsen ! 2 _ "
result = samitler.samitleri_al(cumle)
result_no_duplicates = list(dict.fromkeys(result))
# result_no_duplicates = list(dict.fromkeys([i.lower() for i in result ]))

print(result_no_duplicates)
