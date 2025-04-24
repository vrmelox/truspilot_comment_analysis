
def retrieveComment(company, fichier, articles):
    for article in articles:
        to_csv = ""
        person = {}
        time_tag = article.find("time")
        if time_tag:
            person["time"] = time_tag.text
            to_csv += time_tag.text + ";;" + company
        else:
            to_csv += "NaN" + ";;" + company
        name_tag = article.find("span", class_="typography_heading-xs__osRhC typography_appearance-default__t8iAq")
        if name_tag:
            person["name"] = name_tag.text
            to_csv += ";;" + name_tag.text
        else:
            to_csv += ";;" + "Nan"
        rating_tag = article.find("div", class_="styles_reviewHeader__DzoAZ")
        if rating_tag:
            person["rating"] = rating_tag.get("data-service-review-rating", "N/A")
            to_csv += ";;" + rating_tag.get("data-service-review-rating", "N/A")
        else:
            to_csv += ";;" + "Nan"
        if person:
            notesTotal += int(person["rating"])
        comment_tag = article.find("p", class_=lambda c: c and "typography_body-l__v5JLj" in c)
        if comment_tag:
            person["comment"] = comment_tag.text
            to_csv += ";;" + comment_tag.text + "\n"
        else:
            to_csv += ";;" + "Nan" + "\n"
        fichier.write(to_csv)