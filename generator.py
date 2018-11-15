from pages import *

if __name__ == "__main__":
    home = Home()
    home.generate()
    blog = Blog()
    blog.generate()
    post = Post("content/website.md")
    post.generate()
