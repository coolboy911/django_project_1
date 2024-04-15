from django.core.management.base import BaseCommand
from myapp2.models import Post


class Command(BaseCommand):
    help = 'Generate fake authors and posts.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = '\n'. join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')
