import re
import unicodedata
def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def text_to_id(text):
    """
    Convert input text to id.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = strip_accents(text)
    text = re.sub('[ ]+', '_', text)
    text = re.sub('[^0-9a-zA-Z_-]', '', text)
    return text

def create_speakers():
  from csv import reader
  # open file in read mode
  with open('../_data/special_sessions.csv', 'r') as read_obj:
      # pass the file object to reader() to get the reader object
      csv_reader = reader(read_obj)
      iter_csv_reader = iter(csv_reader)
      # skip first entry
      next(iter_csv_reader)
      # Iterate over each row in the csv using reader object
      for row in iter_csv_reader:
          # row variable is a list that represents a row in csv
          # title = (row[0]+row[1]).replace(" ", "_") + ".md"
          name = text_to_id(row[0] + row[1]) + ".md"
          f= open("../_data/sc/" + name ,"w")
          f.write("---\nfirst_name: %s\nlast_name: %s\nwebpage: %s\nemail: %s\nsession: %s\n---" % (row[0],row[1],row[5],row[2],row[6]))
          f.close()

def create_speakers():
  from csv import reader
  # open file in read mode
  with open('../_data/special_sessions.csv', 'r') as read_obj:
      # pass the file object to reader() to get the reader object
      csv_reader = reader(read_obj)
      iter_csv_reader = iter(csv_reader)
      # skip first entry
      next(iter_csv_reader)
      # Iterate over each row in the csv using reader object
      for row in iter_csv_reader:
          # row variable is a list that represents a row in csv
          # title = (row[0]+row[1]).replace(" ", "_") + ".md"
          name = "talk_" + text_to_id(row[0] + row[1]) + ".md"
          f= open("../_data/sc_talks/" + name ,"w")
          f.write("---\nname: Special Session -%s\nspeakers: %s%s\ncategories:\n  - Special Session\nss: true\nsession: %s\n---" % (row[1],row[0],row[1],row[6]))
          f.close()
create_speakers()
