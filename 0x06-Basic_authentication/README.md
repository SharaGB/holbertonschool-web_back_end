#

<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Background Context</h2>

<p>In this project, you will learn what the authentication process means and implement a <strong>Basic Authentication</strong> on a simple API.</p>

<p>In the industry, you should <strong>not</strong> implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://flask-httpauth.readthedocs.io/en/latest/" title="Flask-HTTPAuth" target="_blank">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/5/6ccb363443a8f301bc2bc38d7a08e9650117de7c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230210%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20230210T213136Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=a70617accb7454e197245dcac1a73cd37bfb5f5b4e411017c0a779d45300d501" alt="" loading="lazy" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://www.youtube.com/watch?v=501dpx2IjGY&ab_channel=JavaBrains" title="REST API Authentication Mechanisms" target="_blank">REST API Authentication Mechanisms</a> </li>
<li><a href="https://docs.python.org/3.7/library/base64.html" title="Base64 in Python" target="_blank">Base64 in Python</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization" title="HTTP header Authorization" target="_blank">HTTP header Authorization</a> </li>
<li><a href="https://palletsprojects.com/p/flask/" title="Flask" target="_blank">Flask</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Base64" title="Base64 - concept" target="_blank">Base64 - concept</a> </li>
</ul>

<h3>General</h3>

<ul>
<li>What authentication means</li>
<li>What Base64 is</li>
<li>How to encode a string in Base64</li>
<li>What Basic authentication means</li>
<li>How to send the Authorization header</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

  </div>
</div>