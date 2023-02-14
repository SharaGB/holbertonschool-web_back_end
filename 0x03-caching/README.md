# Caching

<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Background Context</h2>

<p>In this project, you learn different caching algorithms. </p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29" title="Cache replacement policies - FIFO" target="_blank">Cache replacement policies - FIFO</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29" title="Cache replacement policies - LIFO" target="_blank">Cache replacement policies - LIFO</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29" title="Cache replacement policies - LRU" target="_blank">Cache replacement policies - LRU</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29" title="Cache replacement policies - MRU" target="_blank">Cache replacement policies - MRU</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29" title="Cache replacement policies - LFU" target="_blank">Cache replacement policies - LFU</a> </li>
</ul>

<h3>General</h3>

<ul>
<li>What a caching system is</li>
<li>What FIFO means </li>
<li>What LIFO means</li>
<li>What LRU means</li>
<li>What MRU means</li>
<li>What LFU means</li>
<li>What the purpose of a caching system</li>
<li>What limits a caching system have</li>
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

<h2>More Info</h2>

<h3>Parent class <code>BaseCaching</code></h3>

<p>All your classes must inherit from <code>BaseCaching</code> defined below:</p>

<pre><code>$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
</code></pre>

  </div>
</div>