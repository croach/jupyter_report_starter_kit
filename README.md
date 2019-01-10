# Jupyter Report Starter Kit

This repository is a simple starter kit for using Jupyter notebooks for writing
human readable reports.

Though Jupyter notebooks are fantastic for performing ad-hoc analyses and making
research repeatable, they're not a particularly great format for sharing results
with decision makers who may not have the technical expertise to run a Jupyter
notebook and/or understand the code. This starter kit provides the data
scientist with the tools they need to craft beautiful reports without all the
unnecessary code, intermediate output, etc. that may muddy the report's central
message.

## Setup and Usage

To get started, simply clone or copy the repository to your local machine and
create a new Jupyter notebook for your analysis. Once you have results and are
ready to share your analysis with your colleagues, just run the
`notebook_to_pdf` script (as the example shows below) to convert your notebook
to a PDF report complete with handy defaults such as syntax highlighted code,
figure centering, and clumsy elements such as the input and output prompts
removed.

```
notebook_to_pdf notebook_name.ipynb --template custom.tplx --output output.pdf
```

To accomplish more complex tasks, such as hiding the input and/or output of a
specific cell, you just need to update that cell's metadata. To edit a cell's
metadata, you must first reveal the "Edit Metadata" buttons on each cell by
selecting View > Cell Toolbar > Edit Metadata in the Jupyter notebook window.
Then, simply click on a cell's "Edit Metadata" button and modify the metadata
for that cell. As an example, let's assume that I have a bit of code that
creates a histogram of some data I'm investigating and I want the visualization
to show up in the report, but the code it not needed. In this specific case I
would want to hide the input (i.e., the code), but still show the generated
visualization. To do so, I would simply add the "hide_input" tag to the cell's
metadata, like so.

```json
{
  "tags": [
    "hide_input"
  ]
}
```

The `jupyter_nbconvert_config.py` file contains the configuration for the
nbconvert command and you'll find the tag that you just used in the example
above defined in this file. In this file there are three tags defined in total:
hide_input, hide_output, and hide_all.

Even more interesting is the ability to move all of the code within a notebook
to an appendix. Doing so keeps the report itself very clean, while still
including the code for the reader's review.

## Moving Code to an Appendix

To use the appendix feature, just add a "label" to any cell's metadata, and then
reference that label in the "ref_labels" list of the metadata of the cell where
you want to display the contents later in the notebook. To also hide the
contents of the cell inline, add a "hide_all" tag to its metadata. An example of
the metadata for a cell that both adds a label (for later reference) and hides
the contents of the cell inline can be seen below.

```json
{
  "tags": [
    "hide_all"
  ],
  "label": "appendix"
}
```

To display the cell's contents in an appendix, simply add a cell later in the
notebook where you want the code to be displayed and add the labels of the cells
that you want to display in the "ref_labels" list. An example of the metadata of
a cell that displays the labeled cell's contents is given below.

```json
{
  "ref_labels": [
    "appendix"
  ]
}
```

The labeled cell's contents will be stitched together in order of their
appearance in the document.
