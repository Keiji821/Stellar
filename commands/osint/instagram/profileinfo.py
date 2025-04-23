from instaloader import Instaloader, Profile
   L = Instaloader()
   profile = Profile.from_username(L.context, "usuario")
   print(f"Bio: {profile.biography} | Seguidores: {profile.followers}")
