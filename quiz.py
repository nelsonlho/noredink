import argparse


def get_num_questions():
  user_input = input("how many questions for the quiz   : ")
  if type(user_input) != int:
    print("we expect integers for 'number of questions'!")
    return False
  if user_input <= 0:
    print("we expect positive integers for 'number of questions'!")
    return False
  return user_input


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--useless_flag", help="what it does")
  args = parser.parse_args()

  num_questions = get_num_questions()

if __name__ == '__main__':
  main()
