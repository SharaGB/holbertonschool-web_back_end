# User authentication service

<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/4cb3c8c607afc1d1582d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230217%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20230217T165418Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=4aed81173de573cdf1b009585337e92e026d8dd53ad08e28785ae3546bf424e9" alt="" loading="lazy" style=""></p>

<p>In the industry, you should <strong>not</strong> implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://flask-user.readthedocs.io/en/latest/" title="Flask-User" target="_blank">Flask-User</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="https://flask.palletsprojects.com/en/1.1.x/quickstart/" title="Flask documentation" target="_blank">Flask documentation</a></li>
<li><a href="https://requests.kennethreitz.org/en/latest/user/quickstart/" title="Requests module" target="_blank">Requests module</a></li>
<li><a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html" title="HTTP status codes" target="_blank">HTTP status codes</a></li>
</ul>

<h2>Requirements</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>You should use <code>SQLAlchemy</code> 1.3.x</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
<li>All your functions should be type annotated</li>
<li>The flask app should only interact with <code>Auth</code> and never with <code>DB</code> directly.</li>
<li>Only public methods of <code>Auth</code> and <code>DB</code> should be used outside these classes</li>
</ul>

<h2>Setup</h2>

<p>You will need to install <code>bcrypt</code></p>

<pre><code>pip3 install bcrypt
</code></pre>

  </div>
</div>