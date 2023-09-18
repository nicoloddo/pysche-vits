""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
DISFLUENCIES = [
    "ah", "eh", "mm", "oo", "uh", "er", "um", "oh", 
    "ooh", "eeh", "ohh", "ehh", "ahh", "hum", "huh", "mhm", "erm", "huh", "shh", "uhm", "ehm", "uhh", "hmm",
    "oops", "phew", "psst", "yoo-hoo", "zing", "yikes", "uh-huh", "ouch", "tsk-tsk", "uh-oh", "ahem", "mmhmm"
]

_pad        = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"
_breaths = ['<breath>', '<long_breath'>
_disfluencies = ['<disfl.' + disfl.lower() + '>' for disfl in DISFLUENCIES]

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa) + _breaths + _disfluencies

# Special symbol ids
SPACE_ID = symbols.index(" ")
