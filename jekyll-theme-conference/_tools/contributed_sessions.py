import re
speaker_pattern_comma = re.compile(""" *([^,]+) *\*""")
speaker_pattern_and = re.compile(""" *and +([^,]+) *""")

def find_speaker(speakers):
  match_comma = re.search(speaker_pattern_comma,speakers)
  partial_match = ""
  if match_comma:
      partial_match = match_comma.group(1)
  else:
      partial_match = speakers
  match_and = re.search(speaker_pattern_and, partial_match)
  if match_and:
      return match_and.group(1)
  else:
      return partial_match
  
def create_talks():
  import csv
  C_NUMBER = 0 # Same as S_GROUP
  C_DATE = 1
  C_START = 2
  C_END = 3
  C_ROOM = 4
  contributed_file = open('../_data/contributed.csv', newline='')
  contributed = csv.reader(contributed_file, delimiter=',', quotechar='"')
  
  S_NAME = 0
  S_EMAIL = 1
  S_HERE = 2
  S_NOTES = 3
  S_THEME = 4
  S_GROUP = 5
  S_TITLE = 6
  contributed_speakers_file = open('../_data/contributed_speakers.csv', newline='')
  contributed_speakers = csv.reader(contributed_speakers_file, delimiter=',', quotechar='"')
  iter_contributed_speakers = iter(contributed_speakers)
  # skip first entry
  next(iter_contributed_speakers)
  for index,row in enumerate(contributed_speakers):
    name = "talk_" + str(index+1) + ".md"
    f= open("../_data/ct/" + name ,"w")
    f.write("---\nname: %s\nspeakers: %s\ncategories: Talk\n---" % (row[S_TITLE],find_speaker(row[S_NAME])))
    f.close()

def create_speakers():
  import csv
  from slugify import slugify
  C_NUMBER = 0 # Same as S_GROUP
  C_DATE = 1
  C_START = 2
  C_END = 3
  C_ROOM = 4
  contributed_file = open('../_data/contributed.csv', newline='')
  contributed = csv.reader(contributed_file, delimiter=',', quotechar='"')
  
  S_NAME = 0
  S_EMAIL = 1
  S_HERE = 2
  S_NOTES = 3
  S_THEME = 4
  S_GROUP = 5
  S_TITLE = 6
  contributed_speakers_file = open('../_data/contributed_speakers.csv', newline='')
  contributed_speakers = csv.reader(contributed_speakers_file, delimiter=',', quotechar='"')
  iter_contributed_speakers = iter(contributed_speakers)
  # skip first entry
  next(iter_contributed_speakers)
  for index,row in enumerate(contributed_speakers):
    speaker = find_speaker(row[S_NAME])
    if ' ' in speaker:
      first,*middle,last_name = speaker.split()
      if middle:
        first_name = first + ' ' + ' '.join(middle)
      else:
        first_name = first
    else:
      print(speaker)
    name = slugify(speaker) + ".md"
    f= open("../_data/speakers/" + name ,"w")
    f.write("---\nname: %s\nfirst_name: %s\nlast_name: %s\n---" % (speaker,first_name,last_name))
    f.close()

# def speaker_name_pdf():
#   import os
#   from pathlib import Path
#   for root, dirs, files in os.walk(os.path.abspath("/home/benzox/Documents/Recherche/Conférences/LC2022/jekyll-theme-conference/ct/")):
#     for filename in files:
#       if filename.endswith(".pdf"):

def htmlize_talks():
  import os
  from pathlib import Path
  for root, dirs, files in os.walk(os.path.abspath("/home/benzox/Documents/Recherche/Conférences/LC2022/jekyll-theme-conference/_data/contributed_abstracts/")):
    for filename in files:
      if filename.endswith(".tex"):
        source_file = os.path.join(root, filename)
        target_file = os.path.join(root,Path(filename).with_suffix('.html'))
        print(source_file)
        print(target_file)
        os.system("""hevea article.hva "/home/benzox/Documents/Recherche/Conférences/LC2022/jekyll-theme-conference/_data/contributed_abstracts/asl.hva" """ + source_file)

create_speakers()

# htmlize_talks()
# for row in contributed:
#   schedule[row[C_DATE]][row[C_ROOM]][]
# schedule = {}
# for date in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
#   for room in ['A','B','C','D','E']:
#     schedule 
# Iterate over each row in the csv using reader object
# for row in iter_contributed_speakers:
#   talk_group = group[row['Group']]
#   schedule[talk_group['Date']][talk_group['Room']][talk_group['Start']].setdefault(talks,[]).append(row)
  # schedule[]
  # print(row['Title'])
  # print(find_speaker(row[0]))
# for row in iter_contributed:
  # group[row[C_NUMBER]] = {'Date': row[C_DATE], 'Start': row[C_START], 'End': row[C_END], 'Room': row[C_ROOM]}
