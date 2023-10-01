
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = 'c14c4488603a4781a12603dfa29740cd'
CLIENT_SECRET = 'cf3de9e7debf4e0aa470bd48e7f823ff'

# Create a Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_and_recommend(query, genre):
   # Search for tracks based on the query
   results = sp.search(q=query, type='track', limit=5)
   
   if 'tracks' in results:
       print("Search results for:", query)
       for track in results['tracks']['items']:
           print(f"Track: {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
           print(f"Album: {track['album']['name']}")
           print(f"Spotify URL: {track['external_urls']['spotify']}\n")
       
       # Recommend similar tracks in the specified genre
       recommended_tracks = sp.recommendations(seed_tracks=[track['id']], limit=5, seed_genres=[genre])
       print(f"Recommended tracks in the {genre} genre:")
       for recommended_track in recommended_tracks['tracks']:
           print(f"Track: {recommended_track['name']} by {', '.join([artist['name'] for artist in recommended_track['artists']])}")
           print(f"Album: {recommended_track['album']['name']}")
           print(f"Spotify URL: {recommended_track['external_urls']['spotify']}\n")
   else:
       print("No results found for the query:", query)

if __name__ == "__main__":
   while True:
       search_query = input("Enter a music search query (or 'exit' to quit): ")
       if search_query.lower() == 'exit':
           break
       genre = input("Enter a music genre for recommendations (e.g., pop, rock, hip-hop): ")
       
       search_and_recommend(search_query, genre)
