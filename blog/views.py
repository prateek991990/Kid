from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "Hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Jubin",
        "date": date(2021, 7, 16),
        "title": "Mountain Hiking",
        "excerpt": "There is no better place than waking in the woods",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eu tellus fermentum,
        eleifend arcu et, placerat metus. Mauris et augue ac est hendrerit interdum ut vel augue.
        Aenean a ligula est. Donec sit amet turpis ac augue feugiat pulvinar. Suspendisse ut nulla
        venenatis, semper turpis elementum, scelerisque purus. Fusce ultrices semper luctus. Duis
        nec ullamcorper felis, eget tempus turpis. Praesent venenatis nec mauris sed ultrices.
        Nulla mollis vestibulum ligula a viverra. Nulla sit amet pulvinar odio. Donec porttitor,
        enim quis facilisis fringilla, magna libero fermentum orci, sed imperdiet ante massa quis justo.
        Donec ut maximus orci. Sed condimentum fringilla suscipit
        """,

        "slug": "Life-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Jubin",
        "date": date(2021, 9, 9),
        "title": "Mountain Hiking",
        "excerpt": "There is always better place than waking in the woods",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eu tellus fermentum,
        eleifend arcu et, placerat metus. Mauris et augue ac est hendrerit interdum ut vel augue.
        Aenean a ligula est. Donec sit amet turpis ac augue feugiat pulvinar. Suspendisse ut nulla
        venenatis, semper turpis elementum, scelerisque purus. Fusce ultrices semper luctus. Duis
        nec ullamcorper felis, eget tempus turpis. Praesent venenatis nec mauris sed ultrices.
        Nulla mollis vestibulum ligula a viverra. Nulla sit amet pulvinar odio. Donec porttitor,
        enim quis facilisis fringilla, magna libero fermentum orci, sed imperdiet ante massa quis justo.
        Donec ut maximus orci. Sed condimentum fringilla suscipit
        """,
        "slug": "Nike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Jubin",
        "date": date(2021, 7, 15),
        "title": "Town Hiking",
        "excerpt": "Fear of God is no better place than waking in the woods",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eu tellus fermentum,
        eleifend arcu et, placerat metus. Mauris et augue ac est hendrerit interdum ut vel augue.
        Aenean a ligula est. Donec sit amet turpis ac augue feugiat pulvinar. Suspendisse ut nulla
        venenatis, semper turpis elementum, scelerisque purus. Fusce ultrices semper luctus. Duis
        nec ullamcorper felis, eget tempus turpis. Praesent venenatis nec mauris sed ultrices.
        Nulla mollis vestibulum ligula a viverra. Nulla sit amet pulvinar odio. Donec porttitor,
        enim quis facilisis fringilla, magna libero fermentum orci, sed imperdiet ante massa quis justo.
        Donec ut maximus orci. Sed condimentum fringilla suscipit
        """,
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        "posts": latest_posts})


def posts(request):
    return render(request, 'blog/all-posts.html',
                  {'all_posts': all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {'post': identified_post})
