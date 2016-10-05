import argparse
import csv

def open_input_file_and_strip_headers(file_path):
  result = []  # store in memory, not most efficient but we don't repeat code
  try:
    with open(file_path, 'rb') as csv_input:  # we assume if the file is there it's of legal format
      reader = csv.reader(csv_input)
      for row in reader:
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


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--question_file", help="question file")
  parser.add_argument("--usage_file", help="usage file")

  args = parser.parse_args()

  num_questions = get_num_questions()

  questions = open_input_file_and_strip_headers(args.question_file)
  print args.question_file
  for q in questions:
    print q

if __name__ == '__main__':
  main()
