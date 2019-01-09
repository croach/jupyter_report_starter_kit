# Create a handful of tags to use for specifying cell visibility
c.TagRemovePreprocessor.remove_all_outputs_tags = {"hide_output"}
c.TagRemovePreprocessor.remove_input_tags = {"hide_input"}
c.TagRemovePreprocessor.remove_cell_tags = {"hide_all"}

# Remove all input and output tags (e.g., In [32]: ) from the exported content
c.TemplateExporter.exclude_input_prompt = True
c.TemplateExporter.exclude_output_prompt = True