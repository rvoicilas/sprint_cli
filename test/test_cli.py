import mock

from unittest import TestCase

from sprint_cli.cli import Cli


class TestCli(TestCase):
    def test_show_items(self):
        """Makes sure that the items returned by sprintly's API
        are formatted as expected.
        """
        args = {
                'items': True,
                'show': True,
                '--user': 'myuser',
                '--key': 'mykey',
                '--product': 'obviously myproduct',
                '--user_id': '0101010',
                '--type': None,
                '--status': None
                }

        def side_effect():
            def inner_func(*args, **kwargs):
                return [{
                    'created_by': {
                        'email': 'foo@bar.com',
                        'created_at': '12/12/12'
                        },
                    'score': 'M',
                    'title': 'As a dev I want to make this test pass',
                    'short_url': 'http://fail.org'
                    }]
            return inner_func

        with mock.patch('sprintly.items.Items.get_items',
                new_callable=mock.PropertyMock) as mmock:
            mmock.side_effect = side_effect
            cli = Cli(args)
            data = cli.run()

        expected = """
                Item: http://fail.org
                Title: As a dev I want to make this test pass
                Created by: foo@bar.com (12/12/12)
                Size: M
                """
        expected = '\n'.join([line.lstrip() for line in expected.split('\n')])
        self.assertEqual(expected, data)
