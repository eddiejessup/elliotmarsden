from glob import glob
from os.path import join, splitext, basename
from distutils.dir_util import copy_tree

from jinja2 import Environment, Markup, FileSystemLoader, TemplateNotFound
import markdown

in_path = 'templates'
out_path = 'public'

env = Environment(loader=FileSystemLoader(in_path))


def mark_down_file(file_path):
    return Markup(markdown.markdown(open(file_path).read(),
                                    extensions=['markdown.extensions.fenced_code']))


markdown_files = glob(join(in_path, '*.md'))
markdown_files = [splitext(basename(s))[0] for s in markdown_files]
html_files = ['index', 'cv']


if __name__ == "__main__":
    # Static.
    copy_tree(join(in_path, 'static'), join(out_path, 'static'))

    # Markdown.
    for md_file in markdown_files:
        title = md_file[0].upper() + md_file[1:]
        content = mark_down_file(join(in_path, md_file + '.md'))
        context = {'content': content, 'title': title}
        template_file_name = md_file + '.html'
        try:
            template = env.get_template(template_file_name)
        except TemplateNotFound:
            template = env.get_template('markdown_default.html')
        open(join(out_path, template_file_name), 'w').write(template.render(context))
    # HTML.
    for html_file in html_files:
        template_file_name = html_file + '.html'
        template = env.get_template(template_file_name)
        open(join(out_path, template_file_name), 'w').write(template.render())
