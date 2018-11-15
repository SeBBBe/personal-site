Generating a pure HTML/CSS site using Python
2018/11/15
<p>When deciding what technology to use for a personal web site, my first thought went to the commercial providers. But then I thought <i>"isn't that quite impersonal?"</i> - being a developer by trade after all. So I decided to build something on my own, even though I am by no means a web designer.</p>
<p>After some thought, the choice fell on building a tool for generating a web site in <b>pure HTML/CSS</b>. That would perform well! I chose to use <b>Python</b> since I feel it's efficient and well suited for a small project such as this one.</p>
<p>Every page is represented by a Python class and each blog post is generated from a markdown file with a simple parser inside the template class representing a blog post.</p>