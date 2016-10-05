from collections import defaultdict
import argparse
import csv
import random

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
    _strand_id = row[0]  # unused
    strand_name = row[1]
    _standard_id = row[2] # unused
    standard_name = row[3]
    question_id = row[4]
    difficulty = row[5]
    # we store in a hash map of a hash map with tuples of (question_id, difficulty)
    question_dict[strand_name][standard_name].append((question_id, difficulty))
  return question_dict


def generate_questions(question_dict, question_cnt, usage=None):
  # TODO: incorporate usage
  result = []
  q_cnt = 0
  # such that we do not always give the same strand a 'higher priority' when the question no.
  # is low.
  keys = question_dict.keys()
  random.shuffle(keys)
  while q_cnt < question_cnt:
    # with the constraint of time, we randomly pick a strand and over which a question question
    # random. lib should provide good long-term distribution on a per-standard and per-strand
    #  basis here.
    strand = keys[q_cnt % len(keys)]
    standards = question_dict[strand]
    standard_key = random.choice(standards.keys())
    standard = standards[standard_key]
    question_difficulty_tup = random.choice(standard)
    result.append(question_difficulty_tup[0])
    q_cnt += 1
  return result


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--question_file", help="question file")
  parser.add_argument("--usage_file", help="usage file")

  args = parser.parse_args()

  num_questions = get_num_questions()

  questions = open_input_file_and_strip_headers(args.question_file)
  my_question_dict = build_question_dicts(questions)
  print  generate_questions(my_question_dict, num_questions)

if __name__ == '__main__':
  main()
