# 🎬 Movie Recommender System

An AI-powered movie recommendation application built with Streamlit that helps you discover your next favorite movie using machine learning-based similarity matching.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

### 🎯 Core Functionality
- **AI-Powered Recommendations**: Get personalized movie suggestions based on similarity algorithms
- **Smart Search**: Type to search through thousands of movies with instant filtering
- **Adjustable Results**: Choose between 3-10 movie recommendations
- **Expandable Details**: Click to view comprehensive information about each recommended movie

### 📊 Movie Information
Each recommendation includes:
- Movie poster from TMDB API
- Rating (⭐ X/10) with vote count
- Release year
- Runtime
- Genres
- Overview/plot summary
- Original language
- Release status
- Popularity score
- Tagline (when available)

### 🎨 User Interface
- **Dark Theme**: Professional black background with teal, gold, and cyan accents
- **Searchable Interface**: Type to filter movies or browse the full list
- **Radio Selection**: Easy selection from search results
- **Visual Feedback**: Selected movie displayed prominently with gradient background
- **Responsive Layout**: Poster thumbnails with expandable full details
- **Search History**: Track your last 5 searches with timestamps
- **Statistics**: View total search count

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Movie Recommenderation System"
   ```

2. **Install dependencies**
   ```bash
   pip install -r Requirement.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   - Open your browser and navigate to `http://localhost:8501`

## 📦 Dependencies

```
streamlit
requests
pickle
pathlib
datetime
```

All dependencies are listed in `Requirement.txt`.

## 🎨 Color Scheme

The application uses a carefully designed color palette:

- **Primary (Teal)**: `#06837f` - Main accents and borders
- **Secondary (Gold)**: `#fdc100` - Highlights and hover effects
- **Tertiary (Cyan)**: `#02cecb` - Headers and glowing elements
- **Background**: `#0a0a0a` - Pure black for main content
- **Text**: `#ffffff` - White for maximum readability

## 📁 Project Structure

```
Movie Recommenderation System/
├── app.py                          # Main Streamlit application
├── .streamlit/
│   └── config.toml                 # Streamlit theme configuration
├── utils/
│   ├── style.css                   # Custom CSS styling
│   └── default_poster.png          # Default poster for missing images
├── artificats/
│   ├── moive_list.pkl              # Preprocessed movie dataset
│   └── similary.pkl                # Similarity matrix for recommendations
├── Requirement.txt                 # Python dependencies
├── setup.py                        # Package setup configuration
└── README.md                       # This file
```

## 🔧 How It Works

### 1. Movie Selection
- Type in the search box to filter movies by name
- Select from the filtered results using radio buttons
- Your selection is displayed in a prominent gradient box

### 2. Get Recommendations
- Adjust the number of recommendations (3-10) using the slider
- Click "Get Recommendations" button
- The system uses cosine similarity to find similar movies

### 3. View Details
- Each recommendation shows a poster thumbnail and basic info
- Click the expander arrow to view full details
- Information includes plot, genres, runtime, rating, and more

### 4. Track History
- Check the sidebar for your recent searches
- View timestamps for each search
- See total search statistics

## 🎯 Usage Example

1. **Search for a movie**: Type "Avatar" in the search box
2. **Select**: Choose "Avatar" from the radio button options
3. **Adjust**: Set recommendations to 5 movies
4. **Get Results**: Click "Get Recommendations"
5. **Explore**: Expand each movie to see detailed information

## 🌐 API Integration

The application uses **The Movie Database (TMDB) API** to fetch:
- Movie posters
- Ratings and vote counts
- Release dates and runtime
- Genres and overview
- Additional metadata

**API Key**: The TMDB API key is configured in `app.py`. For production use, consider moving it to environment variables or Streamlit secrets.

## 🎨 Customization

### Changing Colors
Edit the color variables in `utils/style.css`:
```css
:root {
    --primary: #06837f;    /* Teal */
    --secondary: #fdc100;  /* Gold */
    --tertiary: #02cecb;   /* Cyan */
}
```

### Adjusting Recommendation Count
Modify the slider range in `app.py`:
```python
num_recommendations = st.slider('Number of recommendations', 3, 10, 5)
```

### Changing Theme
Edit `.streamlit/config.toml` to adjust the global theme settings.

## 🐛 Troubleshooting

### Issue: Movies not loading
- **Solution**: Check your internet connection and verify the TMDB API is accessible

### Issue: Posters not displaying
- **Solution**: Ensure the `utils/default_poster.png` file exists and the TMDB API key is valid

### Issue: Search not working
- **Solution**: Verify that `artificats/moive_list.pkl` file exists and is not corrupted

### Issue: Recommendations not appearing
- **Solution**: Check that `artificats/similary.pkl` file exists and matches the movie dataset

## 📝 Features Breakdown

### Search Functionality
- **Real-time filtering**: Instant results as you type
- **Case-insensitive**: Matches regardless of capitalization
- **Partial matching**: Finds movies containing your search term
- **Top 10 results**: Shows most relevant matches

### Recommendation Engine
- **Similarity-based**: Uses pre-computed similarity matrix
- **Adjustable count**: Choose how many recommendations to see
- **Sorted by relevance**: Most similar movies appear first

### User Experience
- **Session persistence**: Search history maintained during session
- **Visual feedback**: Clear indication of selected movie
- **Responsive design**: Works on different screen sizes
- **Loading states**: Spinner shown while fetching recommendations

## 🔮 Future Enhancements

Potential features for future versions:
- [ ] User authentication and personalized recommendations
- [ ] Save favorite movies
- [ ] Share recommendations via link
- [ ] Filter by genre, year, or rating
- [ ] Watch provider integration
- [ ] Movie trailers and clips
- [ ] User reviews and ratings
- [ ] Export recommendations to PDF

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **TMDB API**: For providing comprehensive movie data
- **Streamlit**: For the excellent web framework
- **Machine Learning**: Similarity algorithms for recommendations

## 📧 Contact

For questions, suggestions, or issues, please open an issue on the repository.

---

**Made with ❤️ using Streamlit and Python**