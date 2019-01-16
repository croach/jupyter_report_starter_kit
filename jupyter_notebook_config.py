import os
import sys


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


def generate_report_pre_save(model, path, contents_manager, **kwargs):
    """Convert notebook to human readable PDF report before save with nbconvert
    """
    if model['type'] != 'notebook':
        return

    notebook = model['content']
    base, ext = os.path.splitext(path)
    output_filename = "{}.pdf".format(base)
    template_filename = 'custom.tplx'
    notebook_to_pdf = load_module('notebook_to_pdf', contents_manager.root_dir)
    # Make sure that we continue working even if the conversion fails
    try:
      notebook_to_pdf.convert_notebook_to_pdf(notebook, output_filename, template_filename)
    except Exception as e:
      contents_manager.log.error(e, exc_info=True)

# Uncomment the following line to turn on PDF generation upon save.
c.FileContentsManager.pre_save_hook = generate_report_pre_save


#c.ContentsManager.pre_save_hook = None