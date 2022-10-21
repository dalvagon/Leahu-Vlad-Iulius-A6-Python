def build_xml_element(tag, content, **elements):
    xml = ""
    xml += "<" + str(tag)
    for key in elements:
        xml += " " + str(key) + '="' + str(elements[key]) + '"'
    xml += ">" + content
    xml += "</`" + tag + ">"

    return xml


if __name__ == "__main__":
    print(
        build_xml_element(
            "a",
            "Hello there",
            href=" http://python.org ",
            _class=" my-link ",
            id=" someid ",
        )
    )
