<<<<<<< HEAD
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
=======
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your.mail@yourhost.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
>>>>>>> 53d46912c2ab67712c2a5c7f3ceecb71d70ab98b
" > ~/.streamlit/config.toml