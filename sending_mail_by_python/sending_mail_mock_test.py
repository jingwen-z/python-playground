# from mock import patch, call
import unittest
from unittest.mock import patch, call
from sending_mail_by_python import sending_mail as target


class SendEmailTests(unittest.TestCase):
    def test_send_email(self):
        # Mock 'smtplib.SMTP' class
        with patch("smtplib.SMTP") as smtp:
            # Build test message
            # from_address = "from@domain.com"
            # to_address = "to@domain.com"
            from_address = "adlz92@hotmail.com"
            to_address = "adlz92@hotmail.com"

            msg = target.build_email(
                from_address, [to_address], "subject", "message", 'test_df.csv')

            # Send e-mail
            target.send_email(msg, host='127.0.0.1', port=25)

            # Get instance of mocked SMTP object
            instance = smtp.return_value

            # Checks the mock has been called at least one time
            self.assertTrue(instance.sendmail.called)

            # Check the mock has been called only once
            self.assertEqual(instance.sendmail.call_count, 1)

            # Check the mock has been called with a specific list of arguments
            # and keywords
            # instance.sendmail.assert_any_call(msg.From,
            #                                   msg.To,
            #                                   msg.as_string())
            print(msg.as_string())
            print(instance.sendmail.mock_calls)

            # Check the mock has been called ONLY once the given arguments and
            # keywords
            # instance.sendmail.assert_called_once_with(msg.From,
            #                                           msg.To,
            #                                           msg.as_string())

            # Check the mock' calls are equal to a specific list of calls in a
            # specific order
            self.assertEqual(
                instance.sendmail.mock_calls,
                [call(msg.From, msg.To, msg.as_string())]
            )


if __name__ == '__main__':
    unittest.main()
