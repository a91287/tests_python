import ssl
import socket
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def get_ssl_certificate_details(url):
    # Extract the hostname from the URL
    hostname = url.split("//")[-1].split("/")[0]
    
    # Get SSL certificate
    cert_pem = ssl.get_server_certificate((hostname, 443))
    
    # Load the certificate into a x509 object
    cert = x509.load_pem_x509_certificate(cert_pem.encode(), default_backend())
    
    # Extract details
    issuer = cert.issuer
    expiry_date = cert.not_valid_after_utc  # Use not_valid_after_utc

    # Format issuer information
    issuer_info = ', '.join([f"{attribute.oid}: {attribute.value}" for attribute in issuer])
    
    return {
        "issuer": issuer_info,
        "expiry_date": expiry_date
    }

def get_cert_details(url):
    details = get_ssl_certificate_details(url)
    print(f"Expiry Date: {details['expiry_date']} -> URL: {url}")


urls = [
    "https://google.com/",
    "https://g1.com.br/",
    "https://facebook.com/",
    "https://twitter.com/",
    "https://youtube.com/",
    "https://linkedin.com/",
    "https://instagram.com/",
    "https://reddit.com/",
    "https://wikipedia.org/",
    "https://github.com/",
    "https://stackoverflow.com/",
    "https://amazon.com/",
    "https://netflix.com/",
    "https://yahoo.com/",
    "https://bing.com/",
    "https://apple.com/",
    "https://microsoft.com/",
    "https://pinterest.com/",
    "https://ebay.com/",
    "https://craigslist.org/",
    "https://cnn.com/",
    "https://bbc.com/",
    "https://forbes.com/",
    "https://nytimes.com/",
    "https://theguardian.com/",
    "https://reuters.com/",
    "https://bloomberg.com/",
    "https://huffpost.com/",
    "https://usatoday.com/",
    "https://businessinsider.com/",
    "https://time.com/",
    "https://wsj.com/",
    "https://theverge.com/",
    "https://techcrunch.com/",
    "https://arstechnica.com/",
    "https://engadget.com/",
    "https://cnet.com/",
    "https://gizmodo.com/",
    "https://mashable.com/",
    "https://digitaltrends.com/",
    "https://venturebeat.com/",
    "https://ycombinator.com/",
    "https://quora.com/",
    "https://medium.com/",
    "https://tumblr.com/",
    "https://wordpress.com/",
    "https://blogspot.com/",
    "https://shopify.com/",
    "https://etsy.com/",
    "https://airbnb.com/",
    "https://uber.com/",
    "https://lyft.com/",
    "https://dropbox.com/",
    "https://box.com/",
    "https://slack.com/",
    "https://zoom.us/",
    "https://t.co/",
    "https://vimeo.com/",
    "https://dailymotion.com/",
    "https://soundcloud.com/",
    "https://spotify.com/",
    "https://pandora.com/",
    "https://applemusic.com/",
    "https://tidal.com/",
    "https://flickr.com/",
    "https://photobucket.com/",
    "https://500px.com/",
    "https://behance.net/",
    "https://dribbble.com/",
    "https://deviantart.com/",
    "https://artstation.com/",
    "https://imdb.com/",
    "https://rottentomatoes.com/",
    "https://metacritic.com/",
    "https://goodreads.com/",
    "https://bookbub.com/",
    "https://audible.com/",
    "https://duolingo.com/",
    "https://coursera.org/",
    "https://udemy.com/",
    "https://edx.org/",
    "https://khanacademy.org/",
    "https://skillshare.com/",
    "https://pluralsight.com/",
    "https://lynda.com/"
]

for u in urls:
    try:
        get_cert_details(u)    
    except Exception as e:
        print("error getting cert info for {u}")