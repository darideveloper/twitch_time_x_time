import json
import requests

def get_tokens (client_id:str, client_secret:str, login_code:str, direct_url:str):
     """ Get tokens from twitch api, at the endpoint: https://id.twitch.tv/oauth2/token

     Args:
         client_id (str): twitch client id
         client_secret (str): twitch client secret
         login_code (str): code generated by twitch after login
         direct_url (str): url who twitch redirect after login

     Returns:
         tuple: access_token, refresh_token
     """
     
     # Get twitch token for ganarate login url
     token_url = "https://id.twitch.tv/oauth2/token"
     params = {
          "client_id": client_id,
          "client_secret": client_secret,
          "code": login_code,
          "grant_type": "authorization_code",
          "redirect_uri": direct_url,
     }
     res = requests.post (token_url, data=params)
     json_data = json.loads (res.content)
     
     # Extract variables
     access_token = json_data.get("access_token", "")
     refresh_token = json_data.get("refresh_token", "")
     return (access_token, refresh_token)

def get_user_info (user_token:str):
     """ Get user information using user access token

     Args:
         user_token (str): token of the user already logged to the app

     Returns:
         tuple: user_id, user_email, user_picture, user_name
     """
     headers = {
          "Content-Type": "application/json",
          "Authorization": f"Bearer {user_token}"
     }
     
     res = requests.get ("https://id.twitch.tv/oauth2/userinfo", headers=headers)
     json_data = json.loads (res.content)
     user_id = json_data.get ("sub", "")
     user_email = json_data.get ("email", "")
     user_picture = json_data.get ("picture", "")
     user_name = json_data.get("preferred_username", "")
     
     return (user_id, user_email, user_picture, user_name)

def get_twitch_login_link (client_id:str, redirect_url:str):
     """ Generate link for login with twitch

     Args:
         client_id (str): twitch client id
         redirect_url (str): url to redirect after login

     Returns:
         str: twitch login link
     """
          
     
     # Generate link
     url_params = {
        "client_id": client_id,
        "redirect_uri": redirect_url,
        "response_type": "code",
        "force_verify": "true",
        "scope": "openid user:read:email",
        "state": "sample_string",
        "claims": '{"userinfo":{"picture":null, "email":null, "name":null, "user": null, "preferred_username": null}}'
     }
     encoded_params = "&".join([f"{param_key}={param_value}" for param_key, param_value in url_params.items()])
     twitch_link = f"https://id.twitch.tv/oauth2/authorize?{encoded_params}"
     
     return twitch_link