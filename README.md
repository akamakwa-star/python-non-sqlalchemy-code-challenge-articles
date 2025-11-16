Magazine Domain Project (Summary)

Overview:
Simulates a magazine publishing system with three models: Author, Article, and Magazine. Focuses on object-oriented programming, managing relationships without a database.

Key Relationships:

Author → many Articles

Magazine → many Articles

Article → belongs to Author and Magazine

Author ↔ Magazine → many-to-many through Article

Models & Features:

Author: name (immutable), list of articles, magazines, add_article, topic_areas

Magazine: name, category, articles, contributors, article_titles, contributing_authors, top_publisher

Article: author, magazine, title (immutable)

Key Features:

Handles object associations and many-to-many relationships

Provides aggregate methods (topic areas, top contributors, article titles)

Validates input types and lengths

Interactive debugging with lib/debug.py

Usage Example:

author = Author("Jane Doe")
mag = Magazine("Tech Today", "Technology")
article = author.add_article(mag, "The Future of AI")
author.articles()      # [article]
mag.contributors()     # [author]


Testing:

Run pytest for tests

Use python lib/debug.py for interactive debugging

License: Educational purposes only