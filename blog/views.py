import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import models

# Create your views here.


def home(request):
    # context = {"posts": models.Post.objects.all(), "title": "Home"}
    # response = render(request, "blog/home.html", context)
    # print("this is the start----------------")
    # print(response.content.decode())
    # print(response.status_code)
    # print(response.headers)
    context = {
        "site_name": "My Awesome Blog",
        "tagline": "A place for thoughts and ideas.",
        "is_featured_active": True,
        "spotlight_topic": "Django for Beginners",
        "total_posts": models.Post.objects.count(),
        "total_authors": User.objects.filter(post__isnull=False).distinct().count(),
        "features": [
            {
                "icon": "🚀",
                "title": "Fast & Modern",
                "description": "Built with the latest technologies for a great user experience.",
            },
            {
                "icon": "💡",
                "title": "Insightful Content",
                "description": "Explore a wide range of topics from our expert authors.",
            },
            {
                "icon": "💬",
                "title": "Community Driven",
                "description": "Join the conversation and share your own perspective.",
            },
            {
                "icon": "📱",
                "title": "Fully Responsive",
                "description": "Enjoy the same experience on any device, desktop or mobile.",
            },
        ],
        "featured_topics": [
            "Web Development",
            "Data Science",
            "Machine Learning",
            "Cloud Computing",
            "Software Engineering",
            "Cybersecurity",
        ],
        "current_year": datetime.datetime.now().year,
        "posts": models.Post.objects.all(),
        "page_title": "Home",
    }
    return render(request, "blog/home.html", context)


def about(request):
    """About page view - company information"""
    context = {
        "company_name": "BlogHub Team",
        "founded_year": 2025,
        "mission": "Empowering writers to share their stories with the world",
        "team_size": 15,
        "values": [
            "Creativity",
            "Community",
            "Quality Content",
            "Freedom of Expression",
        ],
        "page_title": "about",
    }
    return render(request, "blog/about.html", context)


def contact(request):
    context = {
        "email": "contact@bloghub.com",
        "phone": "+1-800-BLOGHUB",
        "address": "123 Main St, Anytown, USA",
        "business_hours": "Monday - Friday, 9am - 5pm",
        "departments": [
            {"name": "Marketing", "email": "marketing@bloghub.com"},
            {"name": "Sales", "email": "sales@bloghub.com"},
            {"name": "Support", "email": "support@bloghub.com"},
        ],
        "social_media": [
            {"platform": "Facebook", "link": "https://www.facebook.com/bloghub"},
            {"platform": "Twitter", "link": "https://twitter.com/bloghub"},
            {"platform": "Instagram", "link": "https://www.instagram.com/bloghub"},
        ],
        "page_title": "contact",
    }
    return render(request, "blog/contact.html", context)


# def posts(request):
#     posts = [
#         {
#             "title": "The Future of AI in Everyday Life",
#             "author": "Mohamed Taha",
#             "category": "Technology",
#             "excerpt": "AI is transforming industries from healthcare to education. Here’s what’s next.",
#             "published": True,
#             "date": "2025-11-01",
#         },
#         {
#             "title": "Top 5 Design Trends for 2025",
#             "author": "Lina Ahmed",
#             "category": "Design",
#             "excerpt": "Design in 2025 focuses on minimalism and accessibility. Let’s explore the top trends.",
#             "published": True,
#             "date": "2025-10-28",
#         },
#         {
#             "title": "How to Stay Productive While Traveling",
#             "author": "Omar Hassan",
#             "category": "Travel",
#             "excerpt": "Balancing work and travel isn’t easy, but these strategies make it manageable.",
#             "published": True,
#             "date": "2025-09-15",
#         },
#         {
#             "title": "Learning Django the Smart Way",
#             "author": "Sara Khaled",
#             "category": "Education",
#             "excerpt": "Building a blog website is one of the best ways to learn Django effectively.",
#             "published": True,
#             "date": "2025-08-20",
#         },
#         {
#             "title": "Exploring the Nile River: A Photographer’s Story",
#             "author": "Ahmed Nasser",
#             "category": "Travel",
#             "excerpt": "Capturing the beauty of Egypt’s Nile River through a camera lens.",
#             "published": False,  # Draft
#             "date": "2025-07-10",
#         },
#         {
#             "title": "Designing for Accessibility in 2025",
#             "author": "Mariam Adel",
#             "category": "Design",
#             "excerpt": "Why accessibility is the most important design trend for the future.",
#             "published": True,
#             "date": "2025-06-03",
#         },
#         {
#             "title": "Quantum Computing: What You Should Know",
#             "author": "Hassan Ali",
#             "category": "Technology",
#             "excerpt": "Quantum computing is no longer a dream. Here’s what it means for developers.",
#             "published": False,  # Draft
#             "date": "2025-05-12",
#         },
#         {
#             "title": "How Online Learning Changed Education Forever",
#             "author": "Fatma Zaki",
#             "category": "Education",
#             "excerpt": "E-learning platforms have reshaped how students and teachers interact globally.",
#             "published": True,
#             "date": "2025-04-25",
#         },
#     ]
#     context = {"posts": posts, "total_posts": len(posts), "page_title": "Blog posts"}
#     return render(request, "blog/posts.html", context)


class PostListView(ListView):
    model = models.Post
    # the default template_name is <app>/<model>_<viewtype>.html
    template_name = "blog/posts.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


# def post_details(request, post_id: int):
#     try:
#         post = models.Post.objects.get(id=post_id)
#     except models.Post.DoesNotExist:
#         raise Http404(f"Post with ID {post_id} not found.")

#     context = {"post": post}
#     return render(request, "blog/post_detail.html", context)


class PostDetailView(DetailView):
    model = models.Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Post
    success_url = reverse_lazy("blog:blog-home")

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
