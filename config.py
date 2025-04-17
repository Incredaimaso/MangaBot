env_vars = {
  # Get From my.telegram.org
  "API_HASH": "ccbc3f662735abfa604ef6309ba76e67",
  # Get From my.telegram.org
  "API_ID": "22403100",
  #Get For @BotFather
  "BOT_TOKEN": "7292396392",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "cJgQZQXeMpm1O1fq@prudishly-improved-frogmouth.data-1.apse1.tembo.io",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "",
  # Force Subs Channel username without @
  "CHANNEL": "",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "Chapter {chap_num} {chap_name} @Piras_Official",
  # Put Thumb Link 
  "THUMB": "https://i.ibb.co/sphGRfPs/MANGAVERSE-20250417-220954-0000.png"
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
