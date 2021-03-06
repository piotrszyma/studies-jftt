from lexer_test_case import LexerTestCase


class TestSecondSolution(LexerTestCase):
    FILE_LOCATION = '/task-2/lexer.o'
    maxDiff = None

    def test_should_remove_one_line_comment(self):
        text = """#include <stdio.h>
// this is a comment
int main(void) {
    return 0;
}
"""

        expected_result = b"""#include <stdio.h>
int main(void) {
    return 0;
}
"""
        response = self.runParser(text)
        self.assertEqual(response, expected_result)
#
#     def test_should_remove_escaped_two_lines_comment(self):
#         text = """#include <stdio.h>
# // this is a comment \
# lorem ipsum
# int main(void) {
#     return 0;
# }
# """
#
#         expected_result = b"""#include <stdio.h>
# int main(void) {
#     return 0;
# }
# """
#         response = self.runParser(text)
#         self.assertEqual(response, expected_result)
#
#         #
#
#     def test_should_remove_multiline_comment(self):
#         text = """#include <stdio.h>
# /* this is a multiline comment
#  * lorem ipsum dolor es
#  */
# int main(void) {
#     return 0;
# }
# """
#
#         expected_result = b"""#include <stdio.h>
# int main(void) {
#     return 0;
# }
# """
#
#         response = self.runParser(text)
#         self.assertEqual(response, expected_result)
#
#     def test_should_print_string(self):
#         text = """
# cout << "Lorem ipsum //" << endl;
# """
#         expected_result = b"""
# cout << "Lorem ipsum //" << endl;
# """
#         response = self.runParser(text)
#         self.assertEqual(response, expected_result)
