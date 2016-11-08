#-*- coding:utf-8 -*-
u'''
embedding video video to sphinx

usage:

First of all, add `video` to sphinx extension list in conf.py

.. code-block:: python

   sys.path.append(os.path.abspath('extensions'))

   extensions = ['video']


then use `video` directive.

You can specify video by relative path.

.. code-block:: rst

   .. video:: video/test.mov

      Choose :kbd:`View on site` to continue editing in the *Frontend*


finally, build your sphinx project.

.. code-block:: sh

   $ make html

'''

__version__ = '0.0.1'
__author__ = '@ohrstrom'
__license__ = 'LGPLv3'


def setup(app):

    from . import video

    app.add_node(video.video, html=(video.visit, video.depart))
    app.add_directive('video', video.VideoDirective)
