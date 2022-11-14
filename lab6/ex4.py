import re


def filter_xml(path, attrs):
    file = open(path, "r")
    content = file.read()

    return [
        elem
        for elem in re.findall("<\\w+.*?>", content)
        if all([re.search(key + '="' + attrs[key] + '"', elem) for key in attrs.keys()])
    ]


if __name__ == "__main__":
    print(
        filter_xml("xml.html", {"class": "url", "name": "url-form", "data-id": "item"})
    )

    print(filter_xml("xml.html", {"href": "google.com", "class": "link"}))
