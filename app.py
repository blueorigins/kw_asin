from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('/inputs.html')

@app.route('/results', methods=['GET','POST'])
def res():
    import webbrowser as wb
    import requests as r
    import bs4
    # -*- coding: utf-8 -*-

    kw = r.form['keyword']
    kwl = kw.split(",")
    url = 'https://www.amazon.com/s/field-keywords='
    asinput = r.form['asins']
    asinlist = asinput.split(",")
    d = {}

    for i in range(len(kwl)):
        for k in range(1,5):
            p = r.get(url + kwl[i] + '&pages=' + str(k))
            pages = bs4.BeautifulSoup(p.text, "html.parser")
            results = pages.select("#s-results-list-atf")
            x = results[0].findAll("li")
            for li in x:
                for asi in range(len(asinlist)):
                    if li.attrs.get('data-asin') == asinlist[asi]:
                        d[li.attrs.get('id')] = li.attrs.get('data-asin')
                    else:
                        break
        
    print(d)

    f = open("scrape.csv","w",encoding = "utf-8")
    f.write(str(d))
    return render_template('/results.html')


if __name__ == "__main__":
    app.run(debug=True)



