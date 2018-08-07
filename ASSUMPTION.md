# Assumption

1. Reinventing the wheel should be avoided. The same way we use web frameworks
to create online services, similar libraries exist to scrape web pages.
2. XML, and JSON aren't good formats for long files. They require the whole
document to be loaded in memory. CSV, or JSON lines can be read line by line.
3. The first occurence of a link, or image is kept. Duplicates didn't seem
to offer much value for the sitemap. Furthermore, filtering out records added
another component to my submission, `Pipeline`. This object must keep track
of all occurencenses. It increases memory usage, but also allows flexibility.
