# unitest公共断言方法
def common_assert(case, response, status_code, success, message):
    case.assertEqual(status_code, response.status_code)
    case.assertEqual(success, response.json().get("success"))
    case.assertIn(message, response.json().get("message"))
