from collections import defaultdict
import argparse
import csv

def open_input_file_and_strip_headers(file_path):
  result = []  # store in memory, not most efficient but we don't repeat code
  try:
    with open(file_path, 'rb') as csv_input:  # we assume if the file is there it's of legal format
      reader = csv.reader(csv_input)
      for row in reader:
        if row[0].isdigit():
          result.append(row)
    return result
  except IOError:
    print("Cannot open %s" % file_path)
    return []

def get_num_questions():
  user_input = input("how many questions for the quizz   : ")
  if type(user_input) != int:
    print("we expect integers for 'number of questions'!")
    return False
  if user_input <= 0:
    print("we expect positive integers for 'number of questions'!")
    return False
  return user_input

def build_question_dicts(question_rows):
  question_dict = defaultdict(lambda: defaultdict(list))
  for row in question_rows:
    strand_id = row[0]
    strand_name = row[1]
    standard_id = row[2]
    standard_name = row[3]
    question_id = row[4]
    difficulty = row[5]
    # we store in a hash map of a hash map with tuples of (question_id, difficulty)
    question_dict[strand_name][standard_name].append((question_id, difficulty))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--question_file", help="question file")
  parser.add_argument("--usage_file", help="usage file")

  args = parser.parse_args()

  num_questions = get_num_questions()

  questions = open_input_file_and_strip_headers(args.question_file)
  for q in questions:
    print q

if __name__ == '__main__':
  main()
