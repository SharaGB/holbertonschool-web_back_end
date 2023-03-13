# Redis Basic

<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p><img src="https://user-images.githubusercontent.com/90220978/224845013-37803cef-dc09-4c28-844b-1ed91847f9c8.png" alt="" loading="lazy" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="https://redis.io/commands/" title="Redis commands" target="_blank">Redis commands</a></li>
<li><a href="https://redis-py.readthedocs.io/en/stable/" title="Redis python client" target="_blank">Redis python client</a></li>
<li><a href="https://realpython.com/python-redis/" title="How to Use Redis With Python" target="_blank">How to Use Redis With Python</a></li>
<li><a href="https://www.youtube.com/watch?v=Hbt56gFj998&ab_channel=TraversyMedia" title="Redis Crash Course Tutorial" target="_blank">Redis Crash Course Tutorial</a></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>Learn how to use redis for basic operations</li>
<li>Learn how to use redis as a simple cache</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)</li>
<li>All of your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions and methods should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
<li>All your functions and coroutines must be type-annotated.</li>
</ul>

<h2>Install Redis on Ubuntu 18.04</h2>

<pre><code>$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
</code></pre>

<h2>Use Redis in a container</h2>

<p>Redis server is stopped by default - when you are starting a container, you should start it with: <code>service redis-server start</code></p>

  </div>
</div>
