#-*- coding:utf-8 -*-

from docutils import nodes
from docutils.parsers import rst

class video(nodes.General, nodes.Element):
    pass

def visit(self, node):

    video_id = node.video_id
    url = u'//www.video.com/embed/{0}'.format(video_id)
    tag = u'''<iframe width="640" height="360" src="{0}" frameborder="0" allowfullscreen="1">&nbsp;</iframe>'''.format(url)


    tag = u'''<video width="320" height="240" controls>
                  <source src="{path}" type="video/mp4">
                  <source src="{path}" type="video/ogg">
                  Your browser does not support the video tag.
              </video>'''.format(path=video_id)



    self.body.append(tag)


def depart(self, node):
    pass


class VideoDirective(rst.Directive):

    name = 'video'
    node_class = video

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}


    def run(self):

        node = self.node_class()

        arg = self.arguments[0]


        node.video_id = arg

        return [node]
