from tinyhtml import *
    
def HTML_template(contents):

    html_content = html(lang="en")(
        h("head")(
            h("title")("Page Title"),
            h("link", rel="stylesheet", href="style.css")
        ),
        h("body")(
            h("nav")(
                h("h1")("Page Title")
            ),
            h("main")(
                h("md-block")(
                    f"{contents}"
                )
            )
        )
    )  

    return html_content.render()
    print(html_content.render()) 