EXERCISE_1_TESTS = ["houses", "cat", "dog", "reverse", "radar", "civic"]
EXERCISE_2_AND_3_TESTS = "houses cat dog reverse radar civic"
EXPECTED_1 = ["sesuoh", "tac", "god", "esrever", "radar", "civic"]
EXPECTED_2 = "sesuoh tac god esrever radar civic"
EXPECTED_3 = "civic radar reverse dog cat houses"

def reverse(word):
    word_length = len(word)
    answer = ""
    for idx in range(word_length):
        answer += word[-(idx+1)]
    return answer

def reverseEachWord(string):
    ans = []
    splitted_string = string.split(" ")
    for word in splitted_string:
        ans.append(reverse(word))
    ans = " ".join(ans)
    return ans

def testIndividual(expected, recieved, case):
    if expected != recieved:
        print("#################    TEST FAILED    #################")
        print("Expecting: " + expected + ", but recieved: " + recieved)
    else:
        print(case + " PASS")

def testMultipleAnswers(expected, recieved):
    sample_size_expected = sample_size = len(expected)
    sample_size_recieved = len(recieved)
    if (type(sample_size_expected) != str) or (type(sample_size_recieved) != str) :
        raise Exception("Expected input is of type array")
    if sample_size_recieved != sample_size_expected:
        raise Exception("Samples sizes are not equal")
    for idx in sample_size:
        case_recieved = recieved[idx]
        case_expected = expected[idx]
        testIndividual(case_expected, case_recieved)

#### First Exercise ####

for word, expected in zip(EXERCISE_1_TESTS, EXPECTED_1):
    ans = reverse(word)
    testIndividual(expected, ans, word)

#### Second Exercise ####

testIndividual(EXPECTED_2, reverseEachWord(EXERCISE_2_AND_3_TESTS), EXERCISE_2_AND_3_TESTS)