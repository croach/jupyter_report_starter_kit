import os
import sys


def load_module(module_name, root_dir):
  """Load the notebook_to_pdf module

  Unfortunately, there are multiple ways in python to load arbitrary source code
  files depending on which version of Python you are using. The best resource
  I've found on how to do each of these is the following StackOverflow thread.

  https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path

  """
  module_filepath = os.path.join(root_dir, module_name)
  python_version = sys.version_info[:2]

  module = None
  if python_version <= (2, 7):
    import imp
    module = imp.load_source(module_name, module_filepath)
  else:
    import importlib
    loader = importlib.machinery.SourceFileLoader(module_name, module_filepath)
    if python_version <= (3, 4):
      module = loader.load_module()
    else:
      spec = importlib.util.spec_from_loader(loader.name, loader)
      module = importlib.util.module_from_spec(spec)
      loader.exec_module(module)

  return module


def script_post_save(model, os_path, contents_manager, **kwargs):
    """convert notebooks to Python script after save with nbconvert

    replaces `jupyter notebook --script`
    """
    if model['type'] != 'notebook':
        return

    # TODO: Find a better way to import the notebook_to_pdf file. Ultimately, I
    # want to be able to do so without an __init__.py file in the root directory
    # and without a .py file extension on the notebook_to_pdf file.
    sys.path.append(contents_manager.root_dir)
    import notebook_to_pdf

    log = contents_manager.log

    base, ext = os.path.splitext(os.path.basename(os_path))
    input_filename = "{}{}".format(base, ext)
    output_filename = "{}.pdf".format(base)
    template_filename = 'custom.tplx'
    notebook_to_pdf = load_module('notebook_to_pdf', contents_manager.root_dir)
    notebook_to_pdf.convert_notebook_to_pdf(input_filename, output_filename, template_filename)

# Uncomment the following line to turn on PDF generation upon save.
#c.FileContentsManager.post_save_hook = script_post_save
