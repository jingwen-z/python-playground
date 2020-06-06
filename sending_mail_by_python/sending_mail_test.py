# from mock import patch, call
import unittest
from unittest.mock import patch, call

from sending_mail_by_python import sending_mail as target


class SendEmailTests(unittest.TestCase):
    def test_send_email(self):
        # Mock 'smtplib.SMTP' class
        with patch("smtplib.SMTP") as smtp:
            # Build test message
            from_address = "from@domain.com"
            to_address = ["to@domain.com"]

            msg = target.build_email(
                from_address, to_address, "subject", "message")

            # Send e-mail
            target.send_email(msg)

            # Get instance of mocked SMTP object
            instance = smtp.return_value

            # Checks the mock has been called at least one time
            self.assertTrue(instance.sendmail.called)

            # Check the mock has been called only once
            self.assertEqual(instance.sendmail.call_count, 1)

            # Check built e-mail elements
            self.assertEqual(msg.From, from_address)
            self.assertEqual(msg.To, to_address)

            # Check sent e-mail elements
            self.assertEqual(instance.sendmail.mock_calls[0][1][0],
                             from_address)
            self.assertEqual(instance.sendmail.mock_calls[0][1][1], to_address)

            # Check the mock has been called with a specific list of arguments
            # and keywords
            instance.sendmail.assert_any_call(msg.From,
                                              msg.To,
                                              msg.as_string())

            # Check the mock has been called ONLY once the given arguments and
            # keywords
            instance.sendmail.assert_called_once_with(msg.From,
                                                      msg.To,
                                                      msg.as_string())

            # Check the mock' calls are equal to a specific list of calls in a
            # specific order
            self.assertEqual(
                instance.sendmail.mock_calls,
                [call(msg.From, msg.To, msg.as_string())]
            )

    def test_send_email_with_attachment(self):
        # Mock 'smtplib.SMTP' class
        with patch("smtplib.SMTP") as smtp:
            # Build test message
            from_address = "from@domain.com"
            to_address = ["to@domain.com"]
            msg = target.build_email(
                from_address, to_address, "subject", "message", 'test_df.csv')

            # Send e-mail
            target.send_email(msg)

            # Get instance of mocked SMTP object
            instance = smtp.return_value

            # Checks the mock has been called at least one time
            self.assertTrue(instance.sendmail.called)

            # Check the mock has been called only once
            self.assertEqual(instance.sendmail.call_count, 1)

            # Check built e-mail elements
            self.assertEqual(msg.From, from_address)
            self.assertEqual(msg.To, to_address)
            self.assertEqual(msg.attachments[0][0], 'test_df.csv')

            # Check sent e-mail elements
            self.assertEqual(instance.sendmail.mock_calls[0][1][0],
                             from_address)
            self.assertEqual(instance.sendmail.mock_calls[0][1][1], to_address)
            self.assertEqual(
                instance.sendmail.mock_calls[0][1][2].split('\n')[2],
                'Subject: subject')
            self.assertEqual(
                instance.sendmail.mock_calls[0][1][2].split('\n')[13],
                'message')
            self.assertEqual(
                instance.sendmail.mock_calls[0][1][2].split('\n')[18],
                'Content-Disposition: attachment; filename="test_df.csv"')


if __name__ == '__main__':
    unittest.main()
