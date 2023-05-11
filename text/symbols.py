""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
DISFLUENCIES = ['uh', 'ah', 'eh', 'oh', 'um', 'em']

_pad        = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"
_breath = '<breath>'
_disfluencies = ['<disfl.' + disfl.lower() + '>' for disfl in DISFLUENCIES]

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa) + [_breath] + _disfluencies

# Special symbol ids
SPACE_ID = symbols.index(" ")
