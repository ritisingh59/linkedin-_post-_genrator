import pandas as pd

class FewShotPosts:
    def __init__(self):
        self.df = pd.DataFrame([
            {
                "Text": "Just landed my first job after 100+ rejections. Don’t give up. #jobsearch #keepgoing",
                "length": "Short",
                "language": "English",
                "tag": "Job Search"
            },
            {
                "Text": "If you’re job hunting, remember: rejection is redirection. Stay positive! #career #motivation",
                "length": "Short",
                "language": "English",
                "tag": "Job Search"
            },
            {
                "Text": "Networking changed my life. Coffee chats turned into opportunities. Reach out and connect! #networking #career",
                "length": "Short",
                "language": "English",
                "tag": "Networking"
            },
            {
                "Text": "Attended a webinar today and made 3 great connections. Online networking works! #growth #career",
                "length": "Short",
                "language": "English",
                "tag": "Networking"
            }
        ])

    def get_filtered_posts(self, length, language, tag):
        filtered = self.df[
            (self.df["length"] == length) &
            (self.df["language"] == language) &
            (self.df["tag"] == tag)
        ]
        return filtered.to_dict("records")

    def get_tags(self):
        return sorted(self.df["tag"].unique())
