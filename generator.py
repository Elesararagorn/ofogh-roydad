from content import Article


def create_html(article):

    html = f"""
<!DOCTYPE html>
<html lang="fa" dir="ltr">

<head>
<meta charset="UTF-8">
<title>{article.title}</title>
<link rel="stylesheet" href="../static/style.css">
</head>

<body>

<h1>{article.title}</h1>

<p>
{article.text}
</p>

</body>

</html>
"""

    return html
