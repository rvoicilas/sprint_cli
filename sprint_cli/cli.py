import io

from sprintly.items import Items


class Cli(object):
    def __init__(self, args):
        self._args = args

    def _handle_args(self, args):
        if args['items']:
            return self._format_items_request(
                    self._handle_items_request(args))

    def _handle_items_request(self, args):
        user = args['--user']
        key = args['--key']
        product = args['--product']

        items = Items(user, key, product)

        if args['show']:
            assigned_to = args['--user_id']

            # Item type defaults to tasks
            item_type = args['--type']
            if item_type is None:
                item_type = 'task'

            # Item status defaults to in-progress
            item_status = args['--status']
            if item_status is None:
                item_status = 'in-progress'

            return items.get_items(
                    item_type=item_type,
                    status=item_status,
                    assigned_to=assigned_to)

    def _format_items_request(self, data):
        output = io.BytesIO()
        for item in data:
            out = {
                    'created_by': item['created_by']['email'],
                    'created_at': item['created_by']['created_at'],
                    'size': item['score'],
                    'title': item['title'],
                    'short_url': item['short_url']
                    }
            string = """
            Item: {short_url}
            Title: {title}
            Created by: {created_by} ({created_at})
            Size: {size}
            """.format(**out)
            output.write('\n'.join([line.lstrip() for line in string.split('\n')]))
        value = output.getvalue()
        output.close()
        return value

    def run(self):
        try:
            return self._handle_args(self._args)
        except Exception, exc:
            if 'FORBIDDEN' in exc.message:
                return "You are not allowed to make this request"
            raise
