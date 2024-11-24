from textblob import TextBlob

teikumi = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

def noskanas_analize(teikums):
    analize = TextBlob(teikums)
    polaritate = analize.sentiment.polarity
    if polaritate > 0:
        return "Pozitīvs"
    elif polaritate < 0:
        return "Negatīvs"
    else:
        return "Neitrāls"

for teikums in teikumi:
    rezultats = noskanas_analize(teikums)
    print(f"Teikums: \"{teikums}\" - Noskaņojums: {rezultats}")
