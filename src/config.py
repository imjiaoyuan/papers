import os
import json

RSS_FEEDS = {
    'Bioinformatics': [
        "https://connect.biorxiv.org/biorxiv_xml.php?subject=bioinformatics",
        "https://www.nature.com/subjects/bioinformatics.rss",
        "https://www.nature.com/subjects/computational-biology-and-bioinformatics.rss",
        "https://onlinelibrary.wiley.com/feed/2770596x/most-recent"
    ],
    'Genomics': [
        "https://connect.biorxiv.org/biorxiv_xml.php?subject=genomics",
        "https://www.nature.com/subjects/genomics.rss",
    ],
    'Molecular & Evolutionary Bio': [
        "https://www.nature.com/subjects/evolution.atom",
        "https://www.nature.com/subjects/molecular-biology.rss",
    ]
}

RECEIVER_EMAILS_LIST = [
    "imjiaoyuan@gmail.com"
]

EMAIL_CONFIG = {
    'smtp_server': os.getenv('SMTP_SERVER'),
    'smtp_port': int(os.getenv('SMTP_PORT', 465)),
    'sender_email': os.getenv('SENDER_EMAIL'),
    'sender_password': os.getenv('SENDER_PASSWORD'),

    'receiver_emails': RECEIVER_EMAILS_LIST
}