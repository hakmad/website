#!/usr/bin/env python


import os
import markdown


md_extensions = ["meta", "tables", "fenced_code", "pymdownx.tilde"]

posts_dir = "posts"
output_dir = ".website"

template_filename = ".template.html"
template_file = open(template_filename, "r")
template = template_file.read()
template_file.close()

index_post_entry = "[{title}]({url}) ({date})\n\n"

md = markdown.Markdown(extensions=md_extensions)


def convert_and_render(file_paths, page_type):
    pages = []

    for file_path in file_paths:

        file = open(file_path, "r")

        page_data = {
            "content": md.convert(file.read()),
            "title": md.Meta["title"].pop(),
            "url": file_path.split(".")[0] + ".html",
        }

        if page_type == "post":
            page_data["date"] = md.Meta["date"].pop()
            page_data["content"] = (md.convert("Written on: " + page_data["date"]) +
                                    page_data["content"])

        file.close()

        html = template.format(**page_data)

        output_file_path = os.path.join(output_dir, page_data["url"])
        output_file = open(output_file_path, "w")
        output_file.write(html)
        output_file.close()

        pages.append(page_data)

    if page_type == "post":
        return pages 


post_files = [os.path.join(posts_dir, file) for file in os.listdir(posts_dir)]
posts = convert_and_render(post_files, "post")

posts.sort(key=lambda post: post["date"], reverse=True)

file = open("index.md", "w")
file.write("---\ntitle: Index\n---\n\n")

for post in posts:
    file.write(index_post_entry.format(**post))

file.close()

convert_and_render(["index.md", "about.md"], "meta")
