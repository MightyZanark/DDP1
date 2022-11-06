# Simple Multiple Choices checker program
# Inputs are assumed to be valid, i.e. the answer and answer key
# will only be "A", "B", "C", "D", or "E", or "STOP" to stop
# entering inputs


def get_ans_key_and_ans():
    """Returns the answer key and the answer from the user's input,
    both of which are lists
    """

    ans_key = []
    print("Masukkan kunci jawaban:")
    stop = False
    while not stop:
        ans_input = input()
        if ans_input == "STOP":
            stop = True
        else:
            ans_key.append(ans_input)

    print("Masukkan jawaban kamu:")
    ans = [input() for _ in range(len(ans_key))]

    return ans_key, ans


def get_score_and_right_ans(ans_key: list, ans: list, total_questions: int):
    """Returns the user's score and amount of right answers, both of which are ints"""

    right_ans = 0
    for i in range(total_questions):
        if ans_key[i] == ans[i]:
            right_ans += 1

    score = (right_ans * 100)//total_questions
    return score, right_ans


def get_expression(score: int):
    """Returns an expression based on the user's score"""

    if score >= 85:
        return "Semangat :D"

    if score >= 55:
        return "Semangat :)"

    return "nt"


if __name__ == "__main__":
    print("Selamat mencoba Program Pemeriksa Nilai Dek Depe!\n"
          "=================================================\n")

    # Gets variables from corresponding functions
    ans_key, ans = get_ans_key_and_ans()
    total_questions = len(ans_key)
    score, right_ans = get_score_and_right_ans(ans_key, ans, total_questions)
    expression = get_expression(score)

    print(f'\n{expression}\n'
          f'Total jawaban benar adalah {right_ans} dari {total_questions} soal\n'
          f'Nilai yang kamu peroleh adalah {score}')
