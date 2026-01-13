import pickle
import streamlit as st
import requests
from pathlib import Path
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
    # initial_sidebar_state="expanded"
)

# Load external CSS
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load custom CSS from utils folder
css_file = Path(__file__).parent / "utils" / "style.css"
load_css(css_file)

# Additional CSS to force dropdown styling
st.markdown("""
<style>
    /* AGGRESSIVE: Force dropdown to be dark with white text */
    [data-baseweb="popover"],
    [data-baseweb="popover"] > div,
    [data-baseweb="menu"],
    [data-baseweb="menu"] > ul,
    div[role="listbox"],
    ul[role="listbox"] {
        background-color: #1a1a1a !important;
    }
    
    /* Force all list items to have dark background and white text */
    [data-baseweb="menu"] li,
    [data-baseweb="menu"] li > div,
    [role="option"],
    [role="option"] > div,
    [role="option"] span {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
    }
    
    /* Hover state */
    [data-baseweb="menu"] li:hover,
    [data-baseweb="menu"] li:hover > div,
    [role="option"]:hover,
    [role="option"]:hover > div {
        background-color: rgba(6, 131, 127, 0.3) !important;
        color: #ffffff !important;
    }
    
    /* Force all selectbox text to be white and LARGER */
    .stSelectbox div[role="button"] span,
    .stSelectbox div[role="button"] > div,
    .stSelectbox input,
    .stSelectbox span {
        color: #ffffff !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
    }
    
    /* Make the selectbox taller */
    .stSelectbox > div > div {
        min-height: 60px !important;
        padding: 1rem !important;
        font-size: 1.3rem !important;
    }
    
    /* Override any inline styles */
    .stSelectbox * {
        color: #ffffff !important;
        font-size: 1.3rem !important;
    }
    
    /* Increase dropdown option text size */
    [role="option"],
    [role="option"] span,
    [data-baseweb="menu"] li {
        font-size: 1.2rem !important;
        font-weight: 500 !important;
        padding: 1rem 1.25rem !important;
        line-height: 1.6 !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for search history
if 'search_history' not in st.session_state:
    st.session_state.search_history = []

# Function to fetch comprehensive movie details from TMDB API
def fetch_movie_details(movie_id):
    try:
        # Get basic movie details
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=043d2f8e55cb7563cbcf8b6402fcf484&language=en-US"
        response = requests.get(url)
        data = response.json()
        
        # Get poster
        poster_path = data.get('poster_path')
        if poster_path:
            poster_url = "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            default_poster_path = Path(__file__).parent / "utils" / "default_poster.png"
            poster_url = str(default_poster_path)
        
        # Extract details
        details = {
            'poster': poster_url,
            'rating': round(data.get('vote_average', 0), 1),
            'year': data.get('release_date', '')[:4] if data.get('release_date') else 'N/A',
            'runtime': data.get('runtime', 'N/A'),
            'genres': ', '.join([g['name'] for g in data.get('genres', [])]) or 'N/A',
            'overview': data.get('overview', 'No overview available.'),
            'vote_count': data.get('vote_count', 0),
            'popularity': round(data.get('popularity', 0), 1),
            'language': data.get('original_language', 'N/A').upper(),
            'status': data.get('status', 'N/A'),
            'tagline': data.get('tagline', '')
        }
        
        return details
    except Exception as e:
        default_poster_path = Path(__file__).parent / "utils" / "default_poster.png"
        return {
            'poster': str(default_poster_path),
            'rating': 0,
            'year': 'N/A',
            'runtime': 'N/A',
            'genres': 'N/A',
            'overview': 'Details not available.',
            'vote_count': 0,
            'popularity': 0,
            'language': 'N/A',
            'status': 'N/A',
            'tagline': ''
        }

# Sidebar
with st.sidebar:
    st.markdown("<div class='sidebar-title'>🎬 CineMatch</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
        <p style='margin: 0; font-weight: 500; color: #ffffff;'>AI-Powered Movie Recommendations</p>
        <p style='margin: 0.5rem 0 0 0; font-size: 0.85rem; color: #d1d5db;'>Discover movies similar to your favorites using machine learning.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Search History
    st.markdown("<h3 style='color: #ffffff; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.75rem;'>Recent Searches</h3>", unsafe_allow_html=True)
    if st.session_state.search_history:
        for movie, timestamp in reversed(st.session_state.search_history[-5:]):
            st.markdown(f"""
            <div class='history-item'>
                <div class='history-movie'>{movie}</div>
                <div class='history-time'>{timestamp}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #9ca3af; font-size: 0.85rem;'>No recent searches</p>", unsafe_allow_html=True)
    
    # Stats
    st.markdown("<h3 style='color: #ffffff; font-size: 1.1rem; margin-top: 1.5rem; margin-bottom: 0.75rem;'>Statistics</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='stats-box'>
        <div class='stats-number'>{len(st.session_state.search_history)}</div>
        <div class='stats-label'>Total Searches</div>
    </div>
    """, unsafe_allow_html=True)

# Main header
st.markdown("<h1>🎬 Movie Recommender</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Discover your next favorite movie with AI-powered recommendations</p>", unsafe_allow_html=True)

# Load data
movies = pickle.load(open('artificats/moive_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similary.pkl', 'rb'))

# Search interface - centered layout
st.markdown("<br>", unsafe_allow_html=True)
col_spacer1, col_main, col_spacer2 = st.columns([1, 3, 1])

with col_main:
    movies_list = movies['title'].values
    
    # Initialize session state for search
    if 'search_query' not in st.session_state:
        st.session_state.search_query = ''
    if 'selected_movie_final' not in st.session_state:
        st.session_state.selected_movie_final = movies_list[0]
    
    # Custom searchable movie selector
    st.markdown("<p style='color: #ffffff; font-weight: 600; font-size: 1.1rem; margin-bottom: 0.5rem;'>🎥 Search for a movie</p>", unsafe_allow_html=True)
    
    search_query = st.text_input(
        '',
        value=st.session_state.search_query,
        placeholder='Type to search movies...',
        key='search_input',
        label_visibility='collapsed'
    )
    
    # Filter movies based on search
    if search_query:
        filtered_movies = [m for m in movies_list if search_query.lower() in m.lower()]
        st.session_state.search_query = search_query
        
        if filtered_movies:
            # Show filtered results in radio buttons
            st.markdown("<p style='color: #ffffff; font-size: 0.9rem; margin: 0.5rem 0;'>Select from matches:</p>", unsafe_allow_html=True)
            selected_movie = st.radio(
                '',
                filtered_movies[:10],  # Show top 10 matches
                key='movie_radio',
                label_visibility='collapsed'
            )
            st.session_state.selected_movie_final = selected_movie
        else:
            st.markdown("<p style='color: #fdc100; font-size: 0.9rem;'>No movies found. Try a different search.</p>", unsafe_allow_html=True)
    else:
        # When no search, keep the last selected movie or default to first
        if 'selected_movie_final' not in st.session_state or not st.session_state.selected_movie_final:
            st.session_state.selected_movie_final = movies_list[0]
    
    # Display selected movie clearly
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #06837f, #02cecb); padding: 1.25rem; border-radius: 10px; margin: 1rem 0; box-shadow: 0 0 20px rgba(6, 131, 127, 0.3);'>
        <p style='color: #ffffff; font-size: 1.4rem; font-weight: 700; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.3);'>
            🎬 {st.session_state.selected_movie_final}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    num_recommendations = st.slider('Number of recommendations', 3, 10, 5, key='num_rec')
    
    # Recommendation button
    if st.button('🎯 Get Recommendations'):
        # Use the final selected movie
        selected_movie = st.session_state.selected_movie_final
        
        # Add to search history
        timestamp = datetime.now().strftime("%I:%M %p, %b %d")
        st.session_state.search_history.append((selected_movie, timestamp))
        
        with st.spinner('Finding perfect movies for you...'):
            # Get recommendations
            index = movies[movies['title'] == selected_movie].index[0]
            recommended_movies = []
            distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
            
            for i in distances[1:num_recommendations+1]:
                movie_id = movies.iloc[i[0]]['movie_id']
                movie_name = movies.iloc[i[0]].title
                details = fetch_movie_details(movie_id)
                details['name'] = movie_name
                recommended_movies.append(details)
        
        # Display section header
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<div class='section-header'>Recommended Movies</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Display each recommendation as an expandable row
        for idx, movie in enumerate(recommended_movies, 1):
            # Create custom expander header with poster
            col_exp1, col_exp2 = st.columns([1, 8])
            
            with col_exp1:
                st.image(movie['poster'], use_container_width=True)
            
            with col_exp2:
                with st.expander(f"**{movie['name']}** ({movie['year']}) • ⭐ {movie['rating']}/10", expanded=False):
                    # Movie details inside expander
                    st.markdown(f"<h2 style='color: #ffffff; margin-top: 0;'>{movie['name']}</h2>", unsafe_allow_html=True)
                    
                    if movie['tagline']:
                        st.markdown(f"<p style='color: #10b981; font-style: italic; font-size: 1.1rem; margin-bottom: 1.5rem;'>\" {movie['tagline']} \"</p>", unsafe_allow_html=True)
                    
                    # Meta information
                    st.markdown(f"""
                    <div style='display: flex; gap: 1.5rem; margin: 1.5rem 0; flex-wrap: wrap;'>
                        <div style='background: rgba(16, 185, 129, 0.1); padding: 0.5rem 1rem; border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.3);'>
                            <span style='color: #10b981; font-weight: 700; font-size: 1.2rem;'>⭐ {movie['rating']}/10</span>
                            <span style='color: #9ca3af; font-size: 0.9rem; margin-left: 0.5rem;'>({movie['vote_count']:,} votes)</span>
                        </div>
                        <div style='background: #1a1a1a; padding: 0.5rem 1rem; border-radius: 8px; border: 1px solid #2a2a2a;'>
                            <span style='color: #ffffff; font-weight: 600;'>📅 {movie['year']}</span>
                        </div>
                        <div style='background: #1a1a1a; padding: 0.5rem 1rem; border-radius: 8px; border: 1px solid #2a2a2a;'>
                            <span style='color: #ffffff; font-weight: 600;'>⏱️ {movie['runtime']} min</span>
                        </div>
                        <div style='background: #1a1a1a; padding: 0.5rem 1rem; border-radius: 8px; border: 1px solid #2a2a2a;'>
                            <span style='color: #ffffff; font-weight: 600;'>🌐 {movie['language']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Genres
                    st.markdown(f"<p style='color: #d1d5db; margin: 1rem 0; font-size: 1rem;'><strong style='color: #10b981;'>Genres:</strong> {movie['genres']}</p>", unsafe_allow_html=True)
                    
                    # Overview
                    st.markdown(f"<h3 style='color: #ffffff; margin-top: 1.5rem; margin-bottom: 0.75rem;'>Overview</h3>", unsafe_allow_html=True)
                    st.markdown(f"<p style='color: #d1d5db; line-height: 1.8; font-size: 1rem;'>{movie['overview']}</p>", unsafe_allow_html=True)
                    
                    # Additional info
                    st.markdown(f"""
                    <div style='margin-top: 1.5rem; padding: 1rem; background: #1a1a1a; border-radius: 8px; border: 1px solid #2a2a2a;'>
                        <p style='color: #d1d5db; margin: 0.5rem 0;'><strong style='color: #10b981;'>Status:</strong> {movie['status']}</p>
                        <p style='color: #d1d5db; margin: 0.5rem 0;'><strong style='color: #10b981;'>Popularity Score:</strong> {movie['popularity']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    <p class='footer-text' style='color: #9ca3af;'>Powered by TMDB API & Machine Learning</p>
</div>
""", unsafe_allow_html=True)