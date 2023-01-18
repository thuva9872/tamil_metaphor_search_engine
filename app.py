from flask import Flask, render_template, request
from searchquery import search

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search_song():
    # return "hello world"
    if request.method == 'POST':
        query = request.form['searchTerm']
        res = search(query.strip())
        hits = res['hits']['hits']
        time = res['took']
        num_results = res['hits']['total']['value']

        return render_template('search_results.html', query=query, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        return render_template('index.html', init='True')


if __name__ == '__main__':
    app.run()
