import pickle
import requests # type: ignore
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the movie list and similarity matrix
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        return render_template('index.html', selected_movie=selected_movie,
                               recommended_movie_names=recommended_movie_names,
                               recommended_movie_posters=recommended_movie_posters,
                               movies=movies['title'].values)
    return render_template('index.html', movies=movies['title'].values)

if __name__ == '__main__':
    app.run(debug=True)
