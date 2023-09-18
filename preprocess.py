import argparse
import text
from utils import load_filepaths_and_text
import re


def remove_tags(text):
    # This regex pattern matches any sequence of characters that is between '<' and '>'
    tag_pattern = re.compile('<.*?>')

    # Use re.sub to replace all matches with an empty string
    cleaned_text = re.sub(tag_pattern, '', text)

    return cleaned_text


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--out_extension", default="cleaned")
  parser.add_argument("--text_index", default=1, type=int)
  #parser.add_argument("--filelists", nargs="+", default=["filelists/ljs_audio_text_val_filelist.txt", "filelists/ljs_audio_text_test_filelist.txt"])
  parser.add_argument("--filelists", nargs="+", default=[
      "filelists/IEMOCAP_INTERSPEECH_filelist_train", "filelists/IEMOCAP_INTERSPEECH_filelist_val"])
  parser.add_argument("--text_cleaners", nargs="+", default=["english_cleaners2"])

  args = parser.parse_args()
    

  for filelist in args.filelists:
    print("START:", filelist)
    filepaths_and_text = load_filepaths_and_text(filelist)
    cleaned_no_disfl = load_filepaths_and_text(filelist)
    for i in range(len(filepaths_and_text)):
      original_text = filepaths_and_text[i][args.text_index]
      no_disfl_text = remove_tags(original_text)
      
      cleaned_text = text._clean_text(original_text, args.text_cleaners)
      cleaned_text_no_disfl = text._clean_text(no_disfl_text, args.text_cleaners)
      
      filepaths_and_text[i][args.text_index] = cleaned_text
      cleaned_no_disfl[i][args.text_index] = cleaned_text_no_disfl
      
    new_filelist = filelist + "." + args.out_extension
    new_filelist_no_disfl = filelist + "." + args.out_extension + '_no_disfl'
    with open(new_filelist, "w", encoding="utf-8") as f:
      f.writelines(["|".join(x) + "\n" for x in filepaths_and_text])
    with open(new_filelist_no_disfl, "w", encoding="utf-8") as f:
      f.writelines(["|".join(x) + "\n" for x in cleaned_no_disfl])