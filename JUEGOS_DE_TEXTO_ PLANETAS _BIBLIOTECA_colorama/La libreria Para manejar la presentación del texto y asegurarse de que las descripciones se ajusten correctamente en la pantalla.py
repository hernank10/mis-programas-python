import textwrap

description = "Estás en una habitación oscura. Las paredes están cubiertas de musgo y hay una puerta al norte."
wrapped_text = textwrap.fill(description, width=50)
print(wrapped_text)
