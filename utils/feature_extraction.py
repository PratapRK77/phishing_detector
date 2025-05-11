import re
import socket
import whois
import requests
import datetime
from urllib.parse import urlparse

def extract_features_from_url(url, return_details=False):
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    # Feature 1: having_IP_Address
    try:
        socket.inet_aton(domain)
        ip = 1
    except:
        ip = -1

    # Feature 2: URL_Length
    url_length = len(url)
    if url_length < 54:
        length = 1
    elif 54 <= url_length <= 75:
        length = 0
    else:
        length = -1

    # Feature 3: Shortining_Service
    shortening_services = r"bit\.ly|goo\.gl|shorte\.st|tinyurl\.com|ow\.ly|t\.co"
    shortener = -1 if re.search(shortening_services, url) else 1

    # Feature 4: having_At_Symbol
    at = -1 if "@" in url else 1

    # Feature 5: double_slash_redirecting
    redirecting = -1 if url.count("//") > 1 else 1

    # Feature 6: Prefix_Suffix
    prefix_suffix = -1 if "-" in domain else 1

    # Feature 7: having_Sub_Domain
    dots = domain.split(".")
    sub_domain = 1 if len(dots) == 2 else (0 if len(dots) == 3 else -1)

    # Feature 8: SSLfinal_State
    ssl = 1 if parsed.scheme == "https" else -1

    # Feature 9: Domain_registeration_length
    try:
        whois_data = whois.whois(domain)
        exp = whois_data.expiration_date
        if isinstance(exp, list):
            exp = exp[0]
        now = datetime.datetime.now()
        domain_length = 1 if exp and (exp - now).days > 365 else -1
    except:
        domain_length = -1

    # Feature 10: Favicon (static assumption)
    favicon = 1

    # Feature 11: port (static assumption)
    port = 1

    # Feature 12: HTTPS_token
    https_token = -1 if 'https' in domain else 1

    # Feature 13–30: placeholder (static values for now)
    request_url = url_of_anchor = links_in_tags = sfh = submitting_to_email = -1
    abnormal_url = redirect = on_mouseover = right_click = popup = iframe = -1
    age_of_domain = dns_record = web_traffic = page_rank = google_index = links_to_page = statistical_report = -1

    # Final list of features
    values = [
        ip, length, shortener, at, redirecting, prefix_suffix, sub_domain,
        ssl, domain_length, favicon, port, https_token, request_url,
        url_of_anchor, links_in_tags, sfh, submitting_to_email, abnormal_url,
        redirect, on_mouseover, right_click, popup, iframe, age_of_domain,
        dns_record, web_traffic, page_rank, google_index, links_to_page,
        statistical_report
    ]

    analysis = {
        "url_length": len(url),
        "domain_length": len(domain),
        "has_https": "Yes" if ssl == 1 else "No",
        "num_dots": url.count('.'),
        "num_dashes": domain.count('-'),
        "num_digits": sum(c.isdigit() for c in url),
        "num_subdomains": domain.count('.') - 1,
        "has_ip": "Yes" if ip == 1 else "No",
        "is_shortened": "Yes" if shortener == -1 else "No",
        "suspicious_tld": "Yes" if domain.split('.')[-1] in ['tk', 'ml', 'ga', 'cf', 'gq'] else "No"
    }

    if return_details:
        return {"values": values, "analysis": analysis}
    return values
