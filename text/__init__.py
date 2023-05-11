""" from https://github.com/keithito/tacotron """
from text import cleaners
from text.symbols import symbols

import re


# Mappings from symbol to numeric ID and vice versa:
_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}

def split_string_with_spaces(s):
    return [x for x in re.split(r'(\s)', s) if x]

def text_to_sequence(text, cleaner_names):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
      cleaner_names: names of the cleaner functions to run the text through
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence = []

  clean_text = _clean_text(text, cleaner_names)
  for symbol in clean_text:
    symbol_id = _symbol_to_id[symbol]
    sequence += [symbol_id]
  return sequence


def cleaned_text_to_sequence(cleaned_text):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  split_text = split_string_with_spaces(cleaned_text)
  
  sequence = []
  for word in split_text:
      if word.startswith("<"): # it's a disfluency tag
          sequence += [_symbol_to_id[word]]
      else:
          sequence += [_symbol_to_id[symbol] for symbol in word]
          
  return sequence


def sequence_to_text(sequence):
  '''Converts a sequence of IDs back to a string'''
  result = ''
  for symbol_id in sequence:
    s = _id_to_symbol[symbol_id]
    result += s
  return result


def _clean_text(text, cleaner_names):
    # This regex pattern splits the text by '<' and '>', keeping the delimiters and also capturing spaces around '<word>'
    split_text = re.split('(\s*\<.*?\>\s*)', text)
    
    # Remove the empty strings from the list
    split_text = [part for part in split_text if part != '']

    for i in range(len(split_text)):
        # If the part is not between '<' and '>', apply cleaners
        if not (split_text[i].strip().startswith('<') and split_text[i].strip().endswith('>')):
            for name in cleaner_names:
                cleaner = getattr(cleaners, name)
                if not cleaner:
                    raise Exception('Unknown cleaner: %s' % name)
                split_text[i] = cleaner(split_text[i])

    # Combine the cleaned parts back into a single string
    return ''.join(split_text)
